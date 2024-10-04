import csv

def extract_odd_rows(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', newline='') as infile:
        reader = csv.reader(infile)
        odd_rows = [row for index, row in enumerate(reader) if index % 2 == 0]  # 홀수줄(0, 2, 4, ...) 추출
        
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(odd_rows)

# 사용 예시
input_csv = 'MatchInfo.csv'
output_csv = 'NEWMatchInfo.csv'
print ("making " +input_csv)
extract_odd_rows(input_csv, output_csv)