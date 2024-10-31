import csv
from collections import defaultdict

# 파일 열기
file = open("UserDataByLine.csv", "r", encoding="utf-8", errors="ignore")
output_file = open("ChampionLineAverages_user.csv", "w", newline="", encoding="utf-8")

reader = csv.reader(file)
writer = csv.writer(output_file)

# 헤더 처리
header = next(reader)  # 챔피언과 라인이 포함된 헤더
champion_column = header[0]  # 첫 번째 열은 챔피언 이름
line_column = header[1]      # 두 번째 열은 라인
key_list = header[2:]        # 나머지 항목들

# 챔피언-라인별 데이터를 저장할 구조 초기화
data_by_champion_line = defaultdict(lambda: defaultdict(list))

# 챔피언-라인별 데이터 누적
for row in reader:
    champion = row[0]
    line = row[1]
    
    # True/False를 1과 0으로 변환, 숫자로 변환 가능한 값은 float으로 변환
    values = []
    for value in row[2:]:
        value = value.strip()  # 공백 제거
        if value.lower() == "true":
            values.append(1.0)
        elif value.lower() == "false":
            values.append(0.0)
        else:
            try:
                values.append(float(value))
            except ValueError:
                values.append(0.0)  # 변환 실패 시 0으로 설정
    # 챔피언과 라인별로 데이터를 누적
    for i, value in enumerate(values):
        data_by_champion_line[(champion, line)][key_list[i]].append(value)

# 평균과 분산 계산 및 저장
output_header = ["Champion", "Line"] + [f"{key}_Mean" for key in key_list] + [f"{key}_Variance" for key in key_list] + ["DataCount"]
writer.writerow(output_header)

for (champion, line), data in data_by_champion_line.items():
    row = [champion, line]
    
    # 각 지표의 평균 계산
    mean_values = []
    for key in key_list:
        values = data[key]
        total_sum = sum(values) if values else 0
        count = len(values)
        
        # 평균 계산 (직접 계산)
        mean_value = total_sum / count if count > 0 else 0
        mean_values.append(mean_value)  # 평균값을 따로 저장
        
        if key == "longestTimeSpentLiving":
            print(f"{champion} {line} {mean_value}")

    # 평균값을 row에 추가
    row.extend(mean_values)
    
    # 분산 계산 및 row에 추가
    for key in key_list:
        values = data[key]
        count = len(values)
        
        # 분산 계산 (직접 계산)
        variance_value = sum((x - mean_values[key_list.index(key)]) ** 2 for x in values) / count if count > 1 else 0
        row.append(variance_value)

    # 데이터 개수 추가
    row.append(count)
    if count < 50 or line == "Invalid": continue
    # 계산된 데이터를 CSV 파일에 작성
    writer.writerow(row)

# 파일 닫기
file.close()
output_file.close()
