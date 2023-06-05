import  csv

header =  ['rno', 'name', 'address']
rows = [['1', 'Bharati', 'Navi Mumbai'], ['2', 'Raj', 'Mumbai'], ['3', 'Ram', 'Pune']]

with open(r"C:\Users\vashi\OneDrive\Documents\DS150423\Python\_20_csv_file_handling\csv_file1.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)