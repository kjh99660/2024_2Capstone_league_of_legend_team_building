import csv
import json
from collections import defaultdict
import math

# 파일 열기
file = open("GoldmatchInfoToMeanList.csv", "r", encoding="utf-8", errors="ignore")  # 플레이어별 데이터가 있는 파일
file2 = open("GoldAverageAndStdDev.csv", "w", newline="", encoding="utf-8")  # 캐릭터별 평균 및 표준편차 파일

reader = csv.reader(file)
writer = csv.writer(file2)

# 헤더 처리
header = next(reader)  # 첫 번째 행 (championName + key_list)
champion_column = header[0]  # 챔피언 이름
key_list = header[1:]  # 나머지 key_list

# 챔피언별 데이터를 저장할 구조 초기화
champion_data = defaultdict(lambda: {
    'count': 0,  # 데이터 수
    'totals': [0] * len(key_list),  # 값의 합
    'squared_totals': [0] * len(key_list)  # 값의 제곱 합 (표준편차 계산용)
})

# 데이터 읽기 및 챔피언별 값 누적
for row in reader:
    champion_name = row[0]  # 첫 번째 열에 챔피언 이름
    values = list(map(float, row[1:]))  # 나머지 값들은 숫자 (float로 변환)

    if champion_name not in champion_data:
        champion_data[champion_name] = {
            'count': 0,
            'totals': [0] * len(key_list),
            'squared_totals': [0] * len(key_list)
        }

    # 각 챔피언의 값 누적
    champion_data[champion_name]['count'] += 1
    for i, value in enumerate(values):
        champion_data[champion_name]['totals'][i] += value
        champion_data[champion_name]['squared_totals'][i] += value ** 2  # 값의 제곱을 누적

# 챔피언별 평균 및 표준편차 계산 및 저장
header = ['championName'] + [f'{key}_mean' for key in key_list] + [f'{key}_stddev' for key in key_list]
writer.writerow(header)  # CSV 파일에 헤더 기록

for champion_name, data in champion_data.items():
    count = data['count']
    totals = data['totals']
    squared_totals = data['squared_totals']

    # 평균 계산
    means = [total / count if count > 0 else 0 for total in totals]

    # 표준편차 계산
    stddevs = [
        math.sqrt((squared_total / count) - (mean ** 2)) if count > 1 else 0
        for squared_total, mean in zip(squared_totals, means)
    ]

    # 챔피언 이름과 평균 및 표준편차 값을 함께 기록
    writer.writerow([champion_name] + means + stddevs)

# 파일 닫기
file.close()
file2.close()
