import requests
import csv
import time

#쿼리 횟수 2분 당 100회 /초당 20회 제한

api_key = "KEY"
header = {"X-Riot-Token" : api_key}
url = "https://asia.api.riotgames.com/lol/match/v5/matches/"
request_time = 0
numbering = 1

def GetMatchInfo(matchid):
    url = "https://asia.api.riotgames.com/lol/match/v5/matches/" + matchid
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        data = response.json()

    else:
        print("Request failed with status code:", response.status_code)
        return
    
    global numbering
    for i in range(len(data)):
        print(numbering, " : " ,data["info"]["gameId"])#gameId
        try:
            writer.writerow([numbering, data["info"]["gameDuration"], data["info"]["participants"][0], data["info"]["participants"][1], data["info"]["participants"][2], data["info"]["participants"][3], data["info"]["participants"][4]
            , data["info"]["participants"][5], data["info"]["participants"][6], data["info"]["participants"][7], data["info"]["participants"][8], data["info"]["participants"][9]])
            numbering += 1
        except:
            print("Error")
            continue

    return 


#####################################################
file = open("MatchID.csv", "r")
file2 = open("MatchInfo.csv", "w", newline="", encoding="utf-8")
reader = csv.reader(file)
writer = csv.writer(file2)

reader.__next__()

start = time.time()
for line in reader:
    MatchID = line[1]

    if(MatchID == ""):
        continue
    GetMatchInfo(MatchID)
    request_time += 1
    end = time.time()
    if(request_time == 90 and end - start < 120):
        print("Waiting for ", 120 - (end - start) ," seconds")
        time.sleep(120 - (end - start))
        request_time = 0
        start = time.time()

file.close()
file2.close()