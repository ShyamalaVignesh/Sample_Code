import csv

header = ['name', 'pincode', 'city', 'State']
data = ['Nisar', 600120, 'chennai', 'TamilNadu']

with open('D:\Csv_write.csv', 'w', encoding='UTF8') as f:
    write_csv = csv.writer(f)
    write_csv.writerow(header)  # For header
    write_csv.writerow(data)  # For Row
    print("data insert completed")
