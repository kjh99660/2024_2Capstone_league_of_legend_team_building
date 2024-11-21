from flask import Flask, request, jsonify, make_response
from riot_api import getUserAccount, getMatchIDByPuuid, getMatchByMatchId
import csv

app = Flask(__name__) 

def getUserFeature(match_info_list):
    mean_and_std_file = open("MeanAndStd.csv", "r")
    reader = csv.reader(mean_and_std_file)

    header = next(reader)
    mean_data = next(reader)
    std_data = next(reader)
    
    count = len(match_info_list)
    user_feature_data = {
        "aggressive" : 0, #killsNearEnemyTurret/kills
        "defensive" : 0, #killsUnderOwnTurret/kills

        "split" : 0, #damageDealtToBuildings/totalDamageDealt
        "teamfight" : 0, #totalDamageDealtToChampions/totalDamageDealt

        "roamness" : 0 #soloKills/kills
    }
    for i in range(count):
        participants = match_info_list[i]["participants"]
        challenges = participants["challenges"]

        kills = participants["kills"]
        totalDamageDealt = participants["totalDamageDealt"]

        if kills != 0 and kills != None:
            user_feature_data["aggressive"] += challenges["killsNearEnemyTurret"] / kills
            user_feature_data["defensive"] += challenges["killsUnderOwnTurret"] / kills
            user_feature_data["roamness"] += challenges["soloKills"] / kills
        
        if totalDamageDealt != 0 and totalDamageDealt != None:
            user_feature_data["split"] += participants["damageDealtToBuildings"] / totalDamageDealt
            user_feature_data["teamfight"] += participants["totalDamageDealtToChampions"] / totalDamageDealt
    
    user_feature_data["aggressive"] = user_feature_data["aggressive"] / count
    user_feature_data["defensive"] = user_feature_data["defensive"] / count
    user_feature_data["split"] = user_feature_data["split"] / count
    user_feature_data["teamfight"] = user_feature_data["teamfight"] / count
    user_feature_data["roamness"] = user_feature_data["roamness"] / count

    user_feature_data["aggressive"] = (user_feature_data["aggressive"] - mean_data[0]) / std_data[0]
    user_feature_data["defensive"] = (user_feature_data["defensive"] - mean_data[1]) / std_data[1]
    user_feature_data["split"] = (user_feature_data["split"] - mean_data[2]) / std_data[2]
    user_feature_data["teamfight"] = (user_feature_data["teamfight"] - mean_data[3]) / std_data[3]
    user_feature_data["roamness"] = (user_feature_data["roamness"] - mean_data[4]) / std_data[4]
    
    #기준점으로 세구간으로 나누기
    for key, value in user_feature_data.items():
        if value > 1:
            user_feature_data[value] = 1
        elif value < -1:
            user_feature_data[value] = -1
        else:
            user_feature_data[value] = 0
    
    user_feature_data["aggressive"] -= user_feature_data["defensive"]
    user_feature_data["split"] -= user_feature_data["teamfight"]
    user_feature_data["roamness"] *= -1
    del user_feature_data['defensive']
    del user_feature_data['teamfight']

    mean_and_std_file.close()
    return user_feature_data

def getCharacterAndChampion(match_info_list):
    champion_cluster_file = open("championCluster.csv", "r")
    reader = csv.reader(champion_cluster_file)

    user_feature = getUserFeature(match_info_list)
    champion_name = ''
    score = 0

    #정해진 기준대로 유저 feature와 챔피언별 feature를 비교하여 적합한 챔피언 찾기

    characteristics = {
        'aggression': user_feature["aggressive"],
        'roamness': user_feature["roamness"],
        'backdoor': user_feature["split"],
    }

    return characteristics, champion_name, score

@app.route('/api/analyze', methods=['GET'])
def getRecommandInfo():
    data = {
        'characteristics':{
            'aggression': -1, #공격성 : 1, 0, -1 (세분류 : 높음, 중간, 낮음)
            'roamness': -1, #로밍성 : 1, 0, -1
            'backdoor': -1, #백도어? : 1, 0, -1
        },
        'recommends':{
            'champion_name': '',
            'score' : 0
        }
    }
    region = request.args.get('region')
    nickname = request.args.get('nickname')

    line = request.args.get('line')
    
    split_list = nickname.split('#')
    if len(split_list) != 2:
        response = make_response(jsonify(data))
        response.status_code = 400
        return response
    
    puuid = getUserAccount(region, split_list[0], split_list[1])
    if puuid == -1:
        response = make_response(jsonify(data))
        response.status_code = 404
        return response
    
    match_id_list = getMatchIDByPuuid(region, puuid)
    if match_id_list == -1:
        response = make_response(jsonify(data))
        response.status_code = 404
        return response
    elif match_id_list == 0:
        #data에 초보자 추천 챔피언을 추가
        response = make_response(jsonify(data))
        response.status_code = 200
        return response
    
    match_info_list = getMatchByMatchId(region, match_id_list)
    if match_info_list == -1:
        response = make_response(jsonify(data))
        response.status_code = 404
        return response
    
    characteristics, champion_name, score = getCharacterAndChampion(match_info_list)
    data['characteristics'] = characteristics
    data['recommends']['champion_name'] = champion_name
    data['recommends']['score'] = score

    response = make_response(jsonify(data))
    response.status_code = 200
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090)
