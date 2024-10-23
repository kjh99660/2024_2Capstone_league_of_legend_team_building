import requests
import json
import csv
import time

api_key = "RGAPI-c677adfe-10f4-4d92-8169-458006d77916"
header = {"X-Riot-Token" : api_key}
url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/"
request_time = 0
numbering = 1

def GetPuUID(summonerID):
    url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/" + summonerID

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        data = response.json()

    else:
        print("Request failed with status code:", response.status_code)
    
    time.sleep(0.1)
    return data["puuid"]


#####################################################
file = open("GoldSummonerID.csv", "r")
file2 = open("GoldPUUID.csv", "w", newline="")
reader = csv.reader(file)
writer = csv.writer(file2)

writer.writerow(["puuid"])
reader.__next__()

start = time.time()
for line in reader:
    ID = line[3]
    number = line[2]
    if(ID == "" or int(number) > 100):
        continue
    puuid = GetPuUID(ID)
    writer.writerow([number, puuid])
    print(numbering, ": ", puuid)
    numbering += 1
    request_time += 1
    end = time.time()
    if(request_time == 90 and end - start < 120):
        print("Waiting for ", 120 - (end - start) ," seconds")
        time.sleep(120 - (end - start))
        request_time = 0
        start = time.time()

file.close()
file2.close()