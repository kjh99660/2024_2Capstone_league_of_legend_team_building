import requests
import csv
import time

#쿼리 횟수 2분 당 100회 /초당 20회 제한
#장인 UID 만드는 코드

api_key = "KEY"
header = {"X-Riot-Token" : api_key}
request_time = 0
numbering = 1
chanpionName = ""

def GetUID(tag, name):
    url = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + name + "/"+ tag

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        data = response.json()

    else:
        print("Request failed with status code:", response.status_code)
        return
    
    global numbering
    print(chanpionName, numbering, " : " ,data['puuid'])
    writer.writerow([numbering, chanpionName, data['puuid']])
    numbering += 1

    return 


#####################################################
file = open("master.csv", "r", encoding='utf-8')
file2 = open("masterUID.csv", "w", newline="", encoding='utf-8')
reader = csv.reader(file)
writer = csv.writer(file2)

start = time.time()
for line in reader:
    chanpionName = line[0]
    for i in range(1, 11):
        Total = line[i]
        Name = Total.split("#")[0]
        Tag = Total.split("#")[1]

        GetUID(Tag, Name)

        request_time += 1
        end = time.time()
        if(request_time == 90 and end - start < 120):
            print("Waiting for ", 120 - (end - start) ," seconds")
            time.sleep(120 - (end - start))
            request_time = 0
            start = time.time()

file.close()
file2.close()
