import csv
import json

def GetCSVData(input_csv, output_csv):
    count = 0
    KillParticipationValue = 0.1
    killsNearEnemyTurret = 0
    goldPerMinute = 300
    laneMinionsFirst10Minutes = 50
    death = 5
    pickKillWithAlly = 5
    kill = 0
    assist = 0
    looseOfWin = 0
    rowValue = []
    with open(input_csv, 'r', encoding='utf-8', newline='') as infile:
        reader = csv.reader(infile)
        for row in reader:          
            for i in range(2, 12):
                row[i] = row[i].replace("\'", "\"")
                row[i] = row[i].replace("False", "false")
                row[i] = row[i].replace("True", "true")
                jsonData = json.loads(row[i])
                if jsonData['lane'] == 'MIDDLE':
                    try:
                        KillParticipationValue = jsonData['challenges']['killParticipation']
                        killsNearEnemyTurret = jsonData['challenges']['killsNearEnemyTurret']
                        goldPerMinute = jsonData['challenges']['goldPerMinute']
                        laneMinionsFirst10Minutes = jsonData['challenges']['laneMinionsFirst10Minutes']
                        death = jsonData['deaths']
                        pickKillWithAlly = jsonData['challenges']['pickKillWithAlly']
                        looseOfWin = jsonData['win']
                        #kill = jsonData['kills']
                        #assist = jsonData['assists']
                        rowValue.append([KillParticipationValue, killsNearEnemyTurret, goldPerMinute, laneMinionsFirst10Minutes, death, pickKillWithAlly, kill, assist])
                        print(count, ": ",KillParticipationValue, " ",killsNearEnemyTurret, " ", goldPerMinute, " ", laneMinionsFirst10Minutes, " ", death, " " ,pickKillWithAlly)
                        count += 1
                    except:
                        continue
        with open(output_csv, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(rowValue)
                    
        
input_csv = 'NEWMatchInfo.csv'
output_csv = 'CSVForMid.csv'
GetCSVData(input_csv, output_csv)
