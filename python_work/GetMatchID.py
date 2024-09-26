import requests
import csv
import time

#쿼리 횟수 2분 당 100회 /초당 20회 제한

api_key = "KEY"
header = {"X-Riot-Token" : api_key}
url = "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/"
request_time = 0
numbering = 1

def GetMatchID(puuid):
    url = "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?start=0&count=20"

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        data = response.json()

    else:
        print("Request failed with status code:", response.status_code)
    
    global numbering
    for i in range(len(data)):
        print(numbering, " : " ,data[i])
        writer.writerow([numbering, data[i]])
        numbering += 1

    return 


#####################################################
file = open("PUUID.csv", "r")
file2 = open("MatchID.csv", "w", newline="")
reader = csv.reader(file)
writer = csv.writer(file2)

reader.__next__()

start = time.time()
for line in reader:
    PUUID = line[1]

    if(PUUID == ""):
        continue
    GetMatchID(PUUID)
    request_time += 1
    end = time.time()
    if(request_time == 90 and end - start < 120):
        print("Waiting for ", 120 - (end - start) ," seconds")
        time.sleep(120 - (end - start))
        request_time = 0
        start = time.time()

file.close()
file2.close()