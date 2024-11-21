import requests
import time

api_key = "key"
header = {"X-Riot-Token" : api_key}
request_time = 0
numbering = 1

def getUserAccount(region, summoner_name, tag_line):
    base = f"https://{region}.api.riotgames.com"
    end_point = f"/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag_line}"
    url = base + end_point

    response = requests.get(url, headers=header)

    time.sleep(0.05)
    if response.status_code == 200:
        data = response.json()
        return data["puuid"]
    else:
        print("Request failed with status code:", response.status_code)
        return -1

def getMatchIDByPuuid(region, puuid):
    base = f"https://{region}.api.riotgames.com"
    end_point = f"/lol/match/v5/matches/by-puuid/{puuid}/ids"
    url = base + end_point

    response = requests.get(url, headers=header)

    time.sleep(0.05)
    if response.status_code == 200:
        data = response.json()
        if len(data) < 10:
            return 0
        return data
    else:
        print("Request failed with status code:", response.status_code)
        return -1

def getMatchByMatchId(region, match_id_list):
    match_list = []
    base = f"https://{region}.api.riotgames.com"
    for i in range(len(match_id_list)):
        match_id = match_id_list[i]
        end_point = f"/lol/match/v5/matches/{match_id}"
        url = base + end_point
        response = requests.get(url, headers=header)
        
        if response.status_code == 200:
            data = response.json()
            match_list.append(data)
        else:
            print("Request failed with status code:", response.status_code)
        time.sleep(0.05)
    
    if len(match_list) < 10:
        #10이하는 미리 걸렀으니 10이상이 안나오면 데이터를 못찾은거
        return -1
    else:
        return match_list