import csv
import json
import statistics

file = open("MatchInfo4.csv", "r", encoding="utf-8", errors="ignore")
file_ref = open("list.csv", "r", encoding="utf-8")
file2 = open("MasterMeanAndVariance4.csv", "w", newline="", encoding="utf-8")  # 평균 파일

reader = csv.reader(file)
reader_ref = csv.reader(file_ref)
writer = csv.writer(file2)
championName = "rengar"
# header
ref = reader_ref.__next__()
key_list = ref[0:-1]
writer.writerow(key_list)

# data
# 키마다 모든 사용자의 값을 저장할 리스트 초기화
all_values = {key: [] for key in key_list}

# 모든 사용자 정보를 json으로 변환
for lines in reader:
    if championName != lines[0]:       
        mean_values = []
        for key in key_list:
            if all_values[key]:
                mean_value = statistics.mean(all_values[key])
                mean_values.append(mean_value)
            else:
                mean_values.append(0)
        mean_values[0] = championName
        championName = lines[0]
        # 최종적으로 평균을 파일에 기록
        print(mean_values)
        writer.writerow(mean_values)
        # reset
        all_values = {key: [] for key in key_list}



    lines[2] = lines[2].replace("\'", "\"")
    lines[2] = lines[2].replace("True", "true")
    lines[2] = lines[2].replace("False", "false")
    lines[2] = lines[2].replace("?,", "?\",")
    json_data = json.loads(lines[2])
     
    
    challenges = json_data.get("challenges", {})
    gamelength = float(lines[1]) / 60
    if(gamelength == 0):
        gamelength = 25

    # "challenges"가 존재하고 딕셔너리일 경우에만 접근
    if not isinstance(challenges, dict):
        challenges = {}

    for key in key_list:
        # "challenges"에서 값을 찾고, 없으면 최상위 키에서 값을 찾음
        value = challenges.get(key, json_data.get(key, 0))
            
        # 숫자인 경우에만 처리
        if isinstance(value, (int, float)):
            # Minute / Before / Percentage / 경우 안나누고 저장
            if key.find("Minute") != -1 or key.find("Before") != -1 or key.find("Percentage") != -1:
                # 나누지 않는 경우                    
                all_values[key].append(float(value))
            else:
                # 나누는 경우
                value = float(value) / gamelength
                all_values[key].append(float(value))
        
mean_values = []
for key in key_list:
    if all_values[key]:
        mean_value = statistics.mean(all_values[key])
        mean_values.append(mean_value)
    else:
        mean_values.append(0)
mean_values[0] = championName
championName = lines[0]
# 최종적으로 평균을 파일에 기록
print(mean_values)
writer.writerow(mean_values)

file.close()
file_ref.close()
file2.close()
