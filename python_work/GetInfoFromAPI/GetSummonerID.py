import requests
import json
import csv
import time

api_key = "KEY"
header = {"X-Riot-Token" : api_key}
request_time = 0

def GetSummonerID(tier, division, page):
    queue = "RANKED_FLEX_SR"

    url = "https://kr.api.riotgames.com/lol/league/v4/entries/" + queue + "/" + tier + "/" + division + "?page=" + str(page)

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        data = response.json()
        #print(json.dumps(data, ensure_ascii=False ,indent=3))

    else:
        print("Request failed with status code:", response.status_code)

    for i in range(len(data)):
        writer.writerow([tier, division, i, data[i]["summonerId"]])
    
    return 


#####################################################
file = open("GoldSummonerID.csv", "w", newline="")

writer = csv.writer(file)
writer.writerow(["summonerId"])

tier = {"DIAMOND", "PLATINUM", "GOLD", "SILVER", "BRONZE", "IRON"}
division = {"I", "II", "III", "IV"}

start = time.time()
for i in range(2, 5):
    for j in division:
        GetSummonerID("GOLD", j, i)
        request_time += 1
        middle = time.time()
        gap = middle - start
        gap = 120 - gap
        if(request_time == 10 and gap < 120):
            print("Waiting for ", gap ," seconds")
            time.sleep(gap)
            request_time = 0
            start = time.time()

file.close()