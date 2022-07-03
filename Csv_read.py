import csv

with open('D:\Csv_write.csv') as file:
# with open('samplecsv.csv') as file:
    read_csv = csv.reader(file)
    for row in read_csv:
        print(row)
