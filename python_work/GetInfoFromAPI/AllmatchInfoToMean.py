import csv
import json
import statistics

file = open("NEWMatchInfo.csv", "r", encoding="utf-8")
file_ref = open("list.csv", "r", encoding="utf-8")
file2 = open("AllMatchInfoMean.csv", "w", newline="", encoding="utf-8") # 필요한 값 저장할 파일
file3 = open("MeanAndVariance.csv", "w", newline="", encoding="utf-8")  # 평균, 분산 저장할 파일
reader = csv.reader(file)
reader_ref = csv.reader(file_ref)
writer = csv.writer(file2)
writer_mean_variance = csv.writer(file3)
count = 0

# header
ref = reader_ref.__next__()
key_list = ref[0:-1]
writer.writerow(key_list)

# MeanAndVariance.csv 파일에 헤더 쓰기
header = key_list + ['Variance']
writer_mean_variance.writerow(header)

# 키마다 모든 사용자의 값을 저장할 리스트 초기화
all_values = {key: [] for key in key_list}

# 모든 사용자 정보를 json으로 변환
for lines in reader:
    count += 1
    print(count)
    for i in range(2,12):
        lines[i] = lines[i].replace("\'", "\"")
        lines[i] = lines[i].replace("True", "true")
        lines[i] = lines[i].replace("False", "false")
        json_data = json.loads(lines[i])
     
        listToMean = []
        challenges = json_data.get("challenges", {})
        gamelength = challenges.get("gameLength", 25*60) # 게임 길이가 없으면 25분으로 설정
        gamelength = float(gamelength) / 60
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
                    listToMean.append(value)
                    all_values[key].append(float(value))
                else:
                    # 나누는 경우
                    value = float(value) / gamelength
                    listToMean.append(value)
                    all_values[key].append(float(value))
            else:
                listToMean.append(0)  # 숫자가 아니면 0을 삽입

        writer.writerow(listToMean)

mean_values = []
variance_values = []

for key in key_list:
    if all_values[key]:  # 값이 있으면 평균, 분산 계산
        mean_value = statistics.mean(all_values[key])
        variance_value = statistics.variance(all_values[key])

        mean_values.append(mean_value)
        variance_values.append(variance_value)
    else:
        mean_values.append(0)
        variance_values.append(0)

# 최종적으로 평균과 분산을 파일에 기록
writer_mean_variance.writerow(mean_values + ['Overall Mean'])
writer_mean_variance.writerow(variance_values + ['Overall Variance'])   

file.close()
file_ref.close()
file2.close()
file3.close()   