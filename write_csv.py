import csv


def write_csv(data):
    with open('write_csv_data.csv', 'a', newline='', encoding='utf-8') as file :
        fw = csv.writer(file) #fw = csv file writer
        fw.writerow(data)

data = ['2021-12-11 13:37:00', 50, 500]
write_csv(data);