import sys
import csv
import json
import argparse
import mysql.connector
from mysql.connector import Error

def mysqlDbConnection(host_value, db, user_name, pw):
    try:
        connection = mysql.connector.connect(
            host=host_value,
            database=db,
            user=user_name,
            password=pw
        )
        print("Connection Success")
    except Error as e:
        print("Error connecting to MySQL : {}".format(e))
        sys.exit(1)
    return connection

def mysqlDbClose(connection):
    if connection.is_connected():
        connection.cursor().close()
        connection.close()
        print("disconnection MySQL")

def get_index_list(entire_col, stop_point_list):
    index_list = []
    for x in entire_col:
        if x in stop_point_list:
            continue
        index_list.append(x)
    return index_list

def get_match_participant_query_data(entire_col, index_list, numbering, duration, puuId):
    # matchParticipant 테이블 insert
    insert_query1 = "INSERT INTO matchParticipant (numbering, Duration, puuId"
    insert_query2 = " VALUES (%s, %s, %s"
    insert_data = [numbering, duration, puuId]
    for index in index_list:
        if index not in entire_col:
            data = None
        else:
            data = entire_col[index]
        insert_data.append(data)
        insert_query1 += ", " + index
        insert_query2 += ", %s"

    if masterChampion != None:
        insert_query1 += ", masterChampion"
        insert_query2 += ", %s"
        insert_data.append(masterChampion)
    
    insert_query1 += ")"
    insert_query2 += ")"
    insert_query = insert_query1 + insert_query2

    return insert_query, insert_data

def get_challanges_query_data(entire_col, index_list, numbering, puuId):
    # challenges 테이블 insert
    insert_query1 = "INSERT INTO challenges (numbering, puuId"
    insert_query2 = " VALUES (%s, %s"
    insert_data = [numbering, puuId]

    # challenges의 legendaryItemUsed 리스트를 string으로 변환하여 추가(원본은 네자리 int의 리스트)
    if "challenges" in entire_col:
        if "legendaryItemUsed" in entire_col["challenges"]:
            item_list = entire_col["challenges"]["legendaryItemUsed"]
            insert_query1 += ", legendaryItemUsed"
            insert_query2 += ", %s"
            data = ""

            count = 0
            for item_code in item_list:
                # 이게 아마 아이템 사용내역이라 길어질대로 길어질 수 있어서 임의로 끊었음
                if count > 30:
                    break
                data += str(item_code)
                count += 1
            insert_data.append(data)
        else:
            insert_query1 += ", legendaryItemUsed"
            insert_query2 += ", %s"
            data = None
            insert_data.append(data)
                    
        for index in index_list:
            if index not in entire_col["challenges"]:
                data = None
            else:
                data = entire_col["challenges"][index]
            insert_data.append(data)
            insert_query1 += ", " + index
            insert_query2 += ", %s"
    else:
        insert_query1 += ", legendaryItemUsed"
        insert_query2 += ", %s"
        data = None
        insert_data.append(data)

        for index in index_list:
            data = None
            insert_data.append(data)
            insert_query1 += ", " + index
            insert_query2 += ", %s"
    insert_query1 += ")"
    insert_query2 += ")"
    insert_query = insert_query1 + insert_query2

    return insert_query, insert_data

def get_missions_query_data(entire_col, index_list, numbering, puuId):
    # missions 테이블 insert
    insert_query1 = "INSERT INTO missions (numbering, puuId"
    insert_query2 = " VALUES (%s, %s"
    insert_data = [numbering, puuId]
    if "missions" in entire_col:
        for index in index_list:
            if index not in entire_col["missions"]:
                data = None
            else:
                data = entire_col["missions"][index]
            insert_data.append(data)
            insert_query1 += ", " + index
            insert_query2 += ", %s"
        insert_query1 += ")"
        insert_query2 += ")"
        insert_query = insert_query1 + insert_query2
    else:
        for index in index_list:
            data = None
            insert_data.append(data)
            insert_query1 += ", " + index
            insert_query2 += ", %s"
        insert_query1 += ")"
        insert_query2 += ")"
        insert_query = insert_query1 + insert_query2
    
    return insert_query, insert_data

def get_perk_stats_query_data(entire_col, index_list, numbering, puuId):
    # perkStats 테이블 insert
    insert_query1 = "INSERT INTO perkStats (numbering, puuId"
    insert_query2 = " VALUES (%s, %s"
    insert_data = [numbering, puuId]
    if "perks" in entire_col:
        if "statPerks" in entire_col["perks"]:
            for index in index_list:
                if index not in entire_col:
                     data = None
                else:
                    data = entire_col["perks"]["statPerks"][index]
                insert_data.append(data)
                insert_query1 += ", " + index
                insert_query2 += ", %s"
        else:
            for index in index_list:
                data = None
                insert_data.append(data)
                insert_query1 += ", " + index
                insert_query2 += ", %s"
    else:
        for index in index_list:
            data = None
            insert_data.append(data)
            insert_query1 += ", " + index
            insert_query2 += ", %s"
    insert_query1 += ")"
    insert_query2 += ")"
    insert_query = insert_query1 + insert_query2

    return insert_query, insert_data

def get_perk_style_query_data(entire_col, numbering, puuId):
    is_no_exist = False
    # perkStyle1 : primaryStyle 테이블 insert
    insert_query1 = "INSERT INTO perkStyle (numbering, puuId"
    insert_query2 = " VALUES (%s, %s"
    insert_data = [numbering, puuId]

    if "perks" in entire_col:
        if "styles" in entire_col["perks"]:
            #primaryStyle style
            data = entire_col["perks"]["styles"][0]["style"]
            insert_data.append(data)
            insert_query1 += ", primary_style"
            insert_query2 += ", %s"

            #subStyle style
            data = entire_col["perks"]["styles"][1]["style"]
            insert_data.append(data)
            insert_query1 += ", sub_style"
            insert_query2 += ", %s"
            for i in range(4):
                insert_query1 += ", primary_perk" + str(i + 1)
                for j in range(3):
                    insert_query1 += ", primary_perk" + str(i + 1) + "_value" + str(j + 1)
                insert_query2 += ", %s, %s, %s, %s"

                insert_data.append(entire_col["perks"]["styles"][0]["selections"][i]["perk"])
                insert_data.append(entire_col["perks"]["styles"][0]["selections"][i]["var1"])
                insert_data.append(entire_col["perks"]["styles"][0]["selections"][i]["var2"])
                insert_data.append(entire_col["perks"]["styles"][0]["selections"][i]["var3"])
            for i in range(2):
                insert_query1 += ", sub_perk" + str(i + 1)
                for j in range(3):
                    insert_query1 += ", sub_perk" + str(i + 1) + "_value" + str(j + 1)
                insert_query2 += ", %s, %s, %s, %s"

                insert_data.append(entire_col["perks"]["styles"][1]["selections"][i]["perk"])
                insert_data.append(entire_col["perks"]["styles"][1]["selections"][i]["var1"])
                insert_data.append(entire_col["perks"]["styles"][1]["selections"][i]["var2"])
                insert_data.append(entire_col["perks"]["styles"][1]["selections"][i]["var3"])
        else:
            is_no_exist = True
    else:
        is_no_exist = True
    if is_no_exist:
        #primaryStyle style
        data = None
        insert_data.append(data)
        insert_query1 += ", primary_style"
        insert_query2 += ", %s"

        #subStyle style
        data = None
        insert_data.append(data)
        insert_query1 += ", sub_style"
        insert_query2 += ", %s"
        for i in range(4):
            insert_query1 += ", primary_perk" + str(i + 1)
            for j in range(3):
                insert_query1 += ", primary_perk" + str(i + 1) + "_value" + str(j + 1)
            insert_query2 += ", %s, %s, %s, %s"

            insert_data.append(None)
            insert_data.append(None)
            insert_data.append(None)
            insert_data.append(None)
        for i in range(2):
            insert_query1 += ", sub_perk" + str(i + 1)
            for j in range(3):
                insert_query1 += ", sub_perk" + str(i + 1) + "_value" + str(j + 1)
            insert_query2 += ", %s, %s, %s, %s"

            insert_data.append(None)
            insert_data.append(None)
            insert_data.append(None)
            insert_data.append(None)
    insert_query1 += ")"
    insert_query2 += ")"
    insert_query = insert_query1 + insert_query2

    return insert_query, insert_data

def get_all_index_list(csv_file_path):
    f = open(csv_file_path,'r', encoding='utf-8', errors='ignore')
    reader = csv.reader(f)
    row = next(reader)
    
    line = row[2].replace(source[0], destination[0])
    line = line.replace(source[1], destination[1])
    line = line.replace(source[2], destination[2])
    line = line.replace(source[3], destination[3])
    try:
        entire_col = json.loads(line)
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
    
    match_participant_index = get_index_list(entire_col, match_participant_stop)
    challenges_index = get_index_list(entire_col["challenges"], challenges_stop)
    missions_index = get_index_list(entire_col["missions"], missions_stop)
    stat_perks_index = get_index_list(entire_col["perks"]["statPerks"], perk_stats_stop)
    
    f.close()

    return [match_participant_index, challenges_index, missions_index, stat_perks_index]

def entire_data_insert(csv_file_path):
    index_lists = get_all_index_list(csv_file_path, encoding='utf-8', errors='ignore')

    f = open(csv_file_path,'r')
    reader = csv.reader(f)

    host = 'localhost'
    database = 'database_name'
    user = 'user_name'
    password = 'password'
    connection = mysqlDbConnection(host, database, user, password)

    if connection.is_connected():
        cursor = connection.cursor()

        id_count = 0
        for row in reader:
            numbering = row[0]
            duration = row[1]
            puuId = None
            data = None

            for col in row[2:]:
                line = col.replace(source[0], destination[0])
                line = line.replace(source[1], destination[1])
                line = line.replace(source[2], destination[2])
                line = line.replace(source[3], destination[3])
                entire_col = json.loads(line)
                
                puuId = entire_col["puuid"]
                if puuId == 'BOT':
                    puuId = '$$$BOT_' + str(id_count) + '$$$'
                    id_count += 1
                # matchParticipant 테이블에 데이터 insert 
                insert_query, insert_data = get_match_participant_query_data(entire_col, index_lists[0], numbering, duration, puuId)
                cursor.execute(insert_query, tuple(insert_data))
                #print("matchParticipant 데이터 삽입 완료.")

                # challanges 테이블에 데이터 insert 
                insert_query, insert_data = get_challanges_query_data(entire_col, index_lists[1], numbering, puuId)
                cursor.execute(insert_query, tuple(insert_data))
                #print("challenges 데이터 삽입 완료.")

                # missions 테이블에 데이터 insert 
                insert_query, insert_data = get_missions_query_data(entire_col, index_lists[2], numbering, puuId)
                cursor.execute(insert_query, tuple(insert_data))
                #print("missions 데이터 삽입 완료.")

                # perkStats 테이블에 데이터 insert 
                insert_query, insert_data = get_perk_stats_query_data(entire_col, index_lists[3], numbering, puuId)
                cursor.execute(insert_query, tuple(insert_data))
                #print("perkStats 데이터 삽입 완료.")

                # perkStyle 테이블에 데이터 insert 
                insert_query, insert_data = get_perk_style_query_data(entire_col, numbering, puuId)
                cursor.execute(insert_query, tuple(insert_data))
                #print("perkStyle 데이터 삽입 완료.")
        #print(id_count)

        # 변경사항 저장
        connection.commit()
    mysqlDbClose(connection)
    f.close()

def master_data_insert(csv_file_path):
    index_lists = get_all_index_list(csv_file_path)

    f = open(csv_file_path,'r', encoding='utf-8', errors='ignore')
    reader = csv.reader(f)

    host = 'localhost'
    database = 'match5_data_set'
    user = 'root'
    password = '@pas3$89+0D'
    connection = mysqlDbConnection(host, database, user, password)

    numbering = 100000
    with open('match-numbering.txt', 'r') as f:
        numbering = int(f.read())

    if connection.is_connected():
        cursor = connection.cursor()

        for row in reader:
            masterChampion = row[0]
            duration = row[1]
            puuId = None
            data = None

            line = row[2].replace(source[0], destination[0])
            line = line.replace(source[1], destination[1])
            line = line.replace(source[2], destination[2])
            line = line.replace(source[3], destination[3])
            entire_col = json.loads(line)
                
            puuId = entire_col["puuid"]

            # matchParticipant 테이블에 데이터 insert 
            insert_query, insert_data = get_match_participant_query_data(entire_col, index_lists[0], numbering, duration, puuId, masterChampion)
            cursor.execute(insert_query, tuple(insert_data))
            #print("matchParticipant 데이터 삽입 완료.")

            # challanges 테이블에 데이터 insert 
            insert_query, insert_data = get_challanges_query_data(entire_col, index_lists[1], numbering, puuId)
            cursor.execute(insert_query, tuple(insert_data))
            #print("challenges 데이터 삽입 완료.")

            # missions 테이블에 데이터 insert 
            insert_query, insert_data = get_missions_query_data(entire_col, index_lists[2], numbering, puuId)
            cursor.execute(insert_query, tuple(insert_data))
            #print("missions 데이터 삽입 완료.")

            # perkStats 테이블에 데이터 insert 
            insert_query, insert_data = get_perk_stats_query_data(entire_col, index_lists[3], numbering, puuId)
            cursor.execute(insert_query, tuple(insert_data))
            #print("perkStats 데이터 삽입 완료.")

            # perkStyle 테이블에 데이터 insert 
            insert_query, insert_data = get_perk_style_query_data(entire_col, numbering, puuId)
            cursor.execute(insert_query, tuple(insert_data))
            #print("perkStyle 데이터 삽입 완료.")

            numbering += 1

        # 변경사항 저장
        connection.commit()
    mysqlDbClose(connection)
    f.close()

    with open('match-numbering.txt', 'w') as f:
        f.write(str(numbering))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        default="",
        help="path of csv file",
    )
    parser.add_argument(
        "-m",
        "--mode",
        type=int,
        default=0,
        help="mode type (0: entire participant data, 1: master's participant data)",
    )
    args = parser.parse_args()

    assert args.path != ""

    source = ["\'", ": True", ": False", "?,"]
    destination = ["\"", ": true", ": false", "\","]
    match_participant_stop = ["challenges", "missions", "perks", "puuid"]
    challenges_stop = ["legendaryItemUsed"]
    missions_stop = []
    perk_stats_stop = []

    if args.mode == 0:
        sys.exit(entire_data_insert(args.path))
    elif args.mode == 1:
        sys.exit(master_data_insert(args.path))
