import requests
import time

api_key = "RGAPI-7c91809e-7d18-4a43-b3ff-fe578746a4b5"
header = {"X-Riot-Token" : api_key}

API_LIMIT_TIME = 0.05

def getUserAccount(region, summoner_name, tag_line):
    base = f"https://{region}.api.riotgames.com"
    end_point = f"/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag_line}"
    url = base + end_point

    response = requests.get(url, headers=header)
    time.sleep(API_LIMIT_TIME)
    
    if response.status_code == 200:
        data = response.json()
        return data["puuid"]
    else:
        print("Request failed with status code:", response.status_code)
        return -1

def getMatchIDByPuuid(region, puuid):
    base = f"https://{region}.api.riotgames.com"
    end_point = f"/lol/match/v5/matches/by-puuid/{puuid}/ids?count=98"
    url = base + end_point

    response = requests.get(url, headers=header)
    time.sleep(API_LIMIT_TIME)

    if response.status_code == 200:
        data = response.json()
        if len(data) < 50:
            return 0
        return data
    else:
        print("Request failed with status code:", response.status_code)
        return -1

def getMatchByMatchId(region, puuid, match_id_list):
    match_list = []
    temp_list = []
    champion_line_count = {}

    start = time.time()
    base = f"https://{region}.api.riotgames.com"
    for i in range(len(match_id_list)):
        match_id = match_id_list[i]
        end_point = f"/lol/match/v5/matches/{match_id}"
        url = base + end_point

        response = requests.get(url, headers=header)
        if response.status_code == 200:
            data = response.json()
            for participant in data["info"]["participants"]:#경기당 10명의 플레이어
                if participant["puuid"] == puuid:
                    champion_name = participant["championName"].lower()
                    teamPosition = participant["teamPosition"]
                    key = champion_name + '-' + teamPosition

                    #챔피언과 라인을 묶어서 카운팅
                    champion_line_count[key] = champion_line_count.get(key, 0) + 1
                    temp_list.append(participant)
        else:
            print("Request failed with status code:", response.status_code)
        time.sleep(API_LIMIT_TIME)
    
    most_key = max(champion_line_count, key=champion_line_count.get)
    result = most_key.split('-')
    match_list = [m for m in temp_list if m["championName"].lower() == result[0] and m["teamPosition"] == result[1]]
    
    end = time.time()
    print(f"get match data time : {end - start:.5f} sec")

    if len(match_list) < 5:
        return -1, -1, -1
    else:
        return match_list, result[0], result[1]