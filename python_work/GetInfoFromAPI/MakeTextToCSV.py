import csv

file = open("masters.txt", "r", encoding='utf-8')
file2 = open("master.csv", "w", newline="", encoding='utf-8')
reader = csv.reader(file)
writer = csv.writer(file2)

for line in reader:
    Total = line[0]
    Name = Total.split(":")[0]
    Tag = Total.split(":")[1]
    writer.writerow([Name, Tag, line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9]])

file.close()
file2.close()