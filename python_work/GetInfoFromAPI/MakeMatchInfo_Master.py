import requests
import csv
import time

#쿼리 횟수 2분 당 100회 /초당 20회 제한

api_key = "RGAPI-6bd2f003-1f81-416b-8f3f-760bc352bdb6"
header = {"X-Riot-Token" : api_key}
url = "https://asia.api.riotgames.com/lol/match/v5/matches/"
request_time = 0
numbering = 1

def GetMatchInfo_Master(championName, matchid):
    url = "https://asia.api.riotgames.com/lol/match/v5/matches/" + matchid
    find = False
    pos = 0
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        data = response.json()

    else:
        print("Request failed with status code:", response.status_code)
        if(response.status_code == 429):
            print("Waiting for 60 seconds")
            time.sleep(60)
        return
    
    for i in range(0,10):
        try:
            champ = data["info"]["participants"][i]["championName"]
            champ = champ.lower()
            if(champ == championName):
                find = True
                pos = i
                break
        except:
            print("Error")

            
    if(find == False):
        time.sleep(0.5)
        print("Not Found")
        return
    global numbering
    print(numbering," ",championName, " : " ,data["info"]["gameId"])#gameId
    try:
        writer.writerow([championName, data["info"]["gameDuration"], data["info"]["participants"][pos]])
        numbering += 1
    except:
        print("Error")      

    time.sleep(0.5)
    return 


#####################################################
file = open("masterMatchID.csv", "r")
file2 = open("MatchInfo4.csv", "w", newline="", encoding="utf-8")
reader = csv.reader(file)
writer = csv.writer(file2)

reader.__next__()
while(True):
    line = reader.__next__()
    Name = line[0]
    pos = line[1]
    print(pos, "넘어가는 중")
    if(Name == "rengar"):
        break

start = time.time()
for line in reader:
    Name = line[0]
    MatchID = line[1]

    GetMatchInfo_Master(Name, MatchID)
    request_time += 1
    end = time.time()
    if(request_time == 90 and end - start < 120):
        print("Waiting for ", 120 - (end - start) ," seconds")
        time.sleep(120 - (end - start))
        request_time = 0
        start = time.time()

file.close()
file2.close()