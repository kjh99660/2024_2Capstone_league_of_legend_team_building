import requests
import csv
import time

#쿼리 횟수 2분 당 100회 /초당 20회 제한
#장인 UID 만드는 코드

api_key = "KEY"
header = {"X-Riot-Token" : api_key}
request_time = 0
chanpionName = ""

def GetMatchID(character, puuid):
    url = "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?start=0&count=100"

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        data = response.json()

    else:
        print("Request failed with status code:", response.status_code)
        return
    
    for i in range(len(data)):
        print(character, " : " ,data[i])
        writer.writerow([character, data[i]])
    time.sleep(1)
    return 


#####################################################
file = open("masterUID.csv", "r", encoding='utf-8')
file2 = open("masterMatchID.csv", "w", newline="", encoding='utf-8')
reader = csv.reader(file)
writer = csv.writer(file2)

start = time.time()
for line in reader:
    chanpionName = line[1]
    uid = line[2]

    GetMatchID(chanpionName, uid)

    request_time += 1
    end = time.time()
    if(request_time == 90 and end - start < 120):
        print("Waiting for ", 120 - (end - start) ," seconds")
        time.sleep(120 - (end - start))
        request_time = 0
        start = time.time()
        
file.close()
file2.close()
