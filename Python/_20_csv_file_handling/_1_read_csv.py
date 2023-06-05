# CSV
# extension .csv
# stands for comma seperated value
# all the data in this file are seperated using comma

import csv

rows = []
with open(r"C:\Users\vashi\OneDrive\Documents\DS150423\Python\_20_csv_file_handling\csv_file.csv","r") as file:
    data = csv.reader(file)

    header = next(data)
    print("Header : ",header)

    for row in data:
        rows.append(row)

    print(rows)


    print()

    for i in rows[:2]:
        print(i)

    count = data.line_num
    print("Row count : ",count)