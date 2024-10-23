import csv
import json

# 파일 열기
file = open("GoldMatchInfo.csv", "r", encoding="utf-8", errors="ignore")
file_ref = open("list.csv", "r", encoding="utf-8")
file2 = open("GoldmatchInfoToMeanList.csv", "w", newline="", encoding="utf-8")  # 평균 파일
count = 1

reader = csv.reader(file)
reader_ref = csv.reader(file_ref)
writer = csv.writer(file2)

# 헤더 처리
ref = next(reader_ref)
key_list = ref[0:-1]  # key_list에서 마지막 항목 제외
header = ['championName'] + key_list  # championName을 첫 번째 열에 추가
writer.writerow(header)  # CSV 파일에 헤더 쓰기

# 모든 사용자 정보를 json으로 변환
for lines in reader:
    print(count)
    count += 1
    
    # 각 경기에 대해 10명의 플레이어 데이터를 처리
    for i in range(2, 12):
        lines[i] = lines[i].replace("'", "\"")
        lines[i] = lines[i].replace("True", "true")
        lines[i] = lines[i].replace("False", "false")
        lines[i] = lines[i].replace("?,", "?\",")
        json_data = json.loads(lines[i])

        championName = json_data["championName"]  # 챔피언 이름 추출
        challenges = json_data.get("challenges", {})

        if not isinstance(challenges, dict):
            challenges = {}

        # 각 플레이어의 데이터를 저장할 리스트 초기화
        player_data = [championName]  # 첫 번째 열에 championName 저장

        # key_list의 각 항목에 대해 데이터를 추출
        for key in key_list:
            # "challenges"에서 값을 찾고, 없으면 최상위 키에서 값을 찾음
            value = challenges.get(key, json_data.get(key, 0))

            # 숫자인 경우에만 처리
            if isinstance(value, (int, float)):
                player_data.append(float(value))
            else:
                player_data.append(0)  # 숫자가 아니면 0을 삽입

        # 각 플레이어의 데이터를 CSV 파일에 기록
        writer.writerow(player_data)

file.close()
file_ref.close()
file2.close()
