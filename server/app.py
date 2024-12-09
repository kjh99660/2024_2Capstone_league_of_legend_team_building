from flask import Flask, request, jsonify, make_response, render_template
from riot_api import getUserAccount, getMatchIDByPuuid, getMatchByMatchId
import csv
from random import shuffle

import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<region>/<nickname>")
def recommend(region, nickname):
    return render_template('recommend.html', region=region, nickname=nickname)

with open("ChampionLineAverages_user.csv", mode="r", encoding="utf-8") as file:
    CHAMPION_LINE_DATA = [row for row in csv.reader(file)]

with open("championDivision.csv", mode="r", encoding="utf-8") as file:
    CHAMPION_DIVISION_DATA = [row for row in csv.reader(file)]

with open("championByRole.csv", mode="r", encoding="utf-8") as file:
    CHAMPION_ROLE_DATA = [row for row in csv.reader(file)]

with open("beginner_recommend.txt", mode="r", encoding="utf-8") as file:
    BEGINNER_RECOMMEND_DATA = [line.strip() for line in file]

def getMeanAndVar(most_champion, most_line):
    for row in CHAMPION_LINE_DATA[1:]:
        if row[0].lower() == most_champion and row[1] == most_line:
            return row[2:7], row[7:12]
    return -1, -1

def getUserFeature(match_info_list, mean_data, std_data):
    user_feature_data = {
        "aggressive" : 0, #killsNearEnemyTurret/kills
        "defensive" : 0, #killsUnderOwnTurret/kills

        "teamfight" : 0, #totalDamageDealtToChampions/totalDamageDealt
        "split" : 0, #damageDealtToBuildings/totalDamageDealt

        "roamness" : 0 #soloKills/kills
    }

    for participant in match_info_list:
        challenges = participant["challenges"]

        kills = participant.get("kills", 0)
        totalDamageDealt = participant.get("totalDamageDealt", 0)

        if kills:
            user_feature_data["aggressive"] += challenges.get("killsNearEnemyTurret", 0) / kills
            user_feature_data["defensive"] += challenges.get("killsUnderOwnTurret", 0) / kills
            user_feature_data["roamness"] += challenges.get("soloKills", 0) / kills
        
        if totalDamageDealt:
            user_feature_data["split"] += participant.get("damageDealtToBuildings", 0) / totalDamageDealt
            user_feature_data["teamfight"] += participant.get("totalDamageDealtToChampions", 0) / totalDamageDealt
    
    count = len(match_info_list)
    for index, (key, value) in enumerate(user_feature_data.items()):
        user_feature_data[key] = (value / count - float(mean_data[index])) / float(std_data[index])

    return normalizeFeature(user_feature_data)

def normalizeFeature(features):
    #기준점으로 세구간으로 나누기
    bounds = {"upper": [0.26, 0.1, 0.22, 0.2, 0.09], "lower": [-0.01, -0.09, -0.24, -0.21, -0.29]}
    for index, key in enumerate(features):
        feature = features[key]
        if feature >= bounds["upper"][index]:
            features[key] = 1
        elif feature <= bounds["lower"][index]:
            features[key] = -1
        else:
            features[key] = 0
    
    #[-2, -1, 0, 1, 2] -> [-1, 0, 1]
    aggressive = features["aggressive"] - features["defensive"]
    if aggressive >= 1:
        aggressive = 1
    elif aggressive <= -1:
        aggressive = -1
    else:
        aggressive = 0
    features["aggressive"] = aggressive
    
    split = features["split"] - features["teamfight"]
    if split >= 1:
        split = 1
    elif split <= -1:
        split = -1
    else:
        split = 0
    features["split"] = split

    features["roamness"] *= -1
    return features

def getCharacterAndChampion(match_info_list, most_champion, most_line, max_recommend):
    mean, variance = getMeanAndVar(most_champion, most_line)
    if mean == -1:
        return -1, [], []
    
    user_feature = getUserFeature(match_info_list, mean, variance)
    characteristics = {
        'aggression': user_feature["aggressive"],
        'roamness': user_feature["roamness"],
        'backdoor': user_feature["split"],
    }

    recommend_champion_list = []
    line_list = []
    for row in CHAMPION_DIVISION_DATA[1:]:
        if (int(row[2]) == characteristics["aggression"] and
            int(row[3]) == characteristics["backdoor"] and
            int(row[4]) == characteristics["roamness"]):
            recommend_champion_list.append(row[0])
            line_list.append(row[1])
        if len(recommend_champion_list) >= max_recommend:#최대 추천수 까지만
            break
    return characteristics, recommend_champion_list, line_list

def getChampionByRole(most_champion, most_line, max_recommend):
    recommend_champion_list = []
    line_list = []

    role_champion_list = []

    index = 0
    change_point = 0
    pre_role = '0'
    target_role = '0'
    for row in CHAMPION_ROLE_DATA[1:]:
        champion_name = row[0]
        role = row[2]
        if pre_role != role:
            pre_role = role
            change_point = index
        if most_champion == champion_name:
            target_role = role
            break
        index += 1
    start = index
    for row in CHAMPION_ROLE_DATA[start:]:#조건문 뺴고 이어서
        if target_role != row[2]:
            break
        index += 1
    role_champion_list = CHAMPION_ROLE_DATA[change_point+1:index]

    for element in role_champion_list:
        recommend_champion_list.append(element[0])
        line_list.append(element[1])
        if len(recommend_champion_list) >= max_recommend:#최대 추천수 까지만
            break
    
    return recommend_champion_list, line_list

def getBeginnerChampion(max_recommend):
    champion_list = BEGINNER_RECOMMEND_DATA[::2]
    line_list = BEGINNER_RECOMMEND_DATA[1::2]

    random_list = list(zip(champion_list, line_list))
    shuffle(random_list)
    return zip(*random_list[:max_recommend])

@app.route('/api/analyze', methods=['GET'])
def getRecommandInfo():
    max_recommend = 20

    data = {
        'method': '',
        'characteristics':{
            'aggression': -2, #공격성 : 1, 0, -1 (세분류 : 높음, 중간, 낮음)
            'roamness': -2, #로밍성 : 1, 0, -1
            'backdoor': -2, #백도어? : 1, 0, -1
        },
        'recommends':{
            'champion_list': [],
            'line_list': []
        }
    }

    region = request.args.get('region')
    nickname = request.args.get('nickname')

    split_list = nickname.split('#')
    if len(split_list) != 2:
        print('잘못된 요청')
        return make_response(jsonify(data), 400)
    
    puuid = getUserAccount(region.lower(), split_list[0], split_list[1])
    if puuid == -1:
        print("지역 : " + region + "닉네임1 : " + split_list[0] + "닉네임2 : " + split_list[1])
        print('유저를 찾지 못함')
        return make_response(jsonify(data), 404)
    
    match_id_list = getMatchIDByPuuid(region, puuid)
    if match_id_list == -1:
        print('경기기록 요청에 문제 발생')
        return make_response(jsonify(data), 404)
    elif match_id_list == 0:
        champion_list, line_list = getBeginnerChampion(max_recommend)
        data["method"] = "newbie"
        data["recommends"].update({"champion_list": champion_list, "line_list": line_list})
        print('경기기록이 50경기를 못넘음, 초보자 추천 루트')
        return make_response(jsonify(data), 200)
    
    match_info_list, most_champion, most_line = getMatchByMatchId(region, puuid, match_id_list)
    if match_info_list == -1:
        champion_list, line_list = getBeginnerChampion(max_recommend)
        data["method"] = "newbie"
        data["recommends"].update({"champion_list": champion_list, "line_list": line_list})
        print('많이 플레이한 챔피언-라인 기록이 기준치를 못넘김, 초보자 추천 루트')
        return make_response(jsonify(data), 200)
    
    characteristics, champion_list, line_list = getCharacterAndChampion(match_info_list, most_champion, most_line, max_recommend)
    if len(champion_list) < 1:
        if characteristics != -1:
            data['characteristics'] = characteristics
        champion_list, line_list = getChampionByRole(most_champion, most_line, max_recommend)
        if len(champion_list) < 1:
            print('역할군 추천도 불가')
            return make_response(jsonify(data), 404)
        
        data["method"] = "class"
        data["recommends"].update({"champion_list": champion_list, "line_list": line_list})
        print('성향에 맞는 챔피언이 없음, 역할군 기반 추천 루트')
        return make_response(jsonify(data), 200)
    
    data["method"] = "analyze"
    data['characteristics'] = characteristics
    data["recommends"].update({"champion_list": champion_list, "line_list": line_list})
    print('성향에 맞는 챔피언을 찾음!')
    return make_response(jsonify(data), 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090)
