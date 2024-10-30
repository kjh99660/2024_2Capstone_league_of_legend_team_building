import csv
import json

file = open("MasterMatchInfo4.csv", "r", encoding="utf-8", errors="ignore")
file_ref = open("list2.csv", "r", encoding="utf-8")
file2 = open("MasterDataByLine4.csv", "w", newline="", encoding="utf-8")  # 라인별 정리

reader = csv.reader(file)
reader_ref = csv.reader(file_ref)
writer = csv.writer(file2)
count = 1
# header
ref = reader_ref.__next__()
key_list = ref[0:-1]
writer.writerow(key_list)
key_list = ref[1:-1]

# 모든 사용자 정보를 json으로 변환
for lines in reader:
    lines[2] = lines[2].replace("\'", "\"")
    lines[2] = lines[2].replace("True", "true")
    lines[2] = lines[2].replace("False", "false")
    lines[2] = lines[2].replace("?,", "?\",")
    json_data = json.loads(lines[2])
      
    challenges = json_data.get("challenges", {})
    gamelength = lines[1]

    # "challenges"가 존재하고 딕셔너리일 경우에만 접근
    if not isinstance(challenges, dict):
        challenges = {}

    # 필요한 값만 추출
    row_data = []
    row_data.append(lines[0])
    for key in key_list:
        # "challenges"에서 값을 찾고, 없으면 최상위 키에서 값을 찾음
        value = challenges.get(key, json_data.get(key, 0))
        # longestTimeSpentLiving 값이 0이면 게임 길이로 대체
        if key == "longestTimeSpentLiving" and value == 0:
            value = gamelength
        if value == 0:
            value = json_data.get(key, 0)
            row_data.append(value)
        else:
            row_data.append(value)  
        
    

    writer.writerow(row_data)
    count += 1


file.close()
file_ref.close()
file2.close()
