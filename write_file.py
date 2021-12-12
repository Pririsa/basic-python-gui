from datetime import datetime

def read_file():
    file_name = 'data.txt'
    with open(file_name, 'w') as file:
        file.write('Durian: 10')

def write_file():
    pass

def append_file(quantity, total):
    file_name = 'calculator.txt'
    date = datetime.now()
    datetime_stamp = date.replace(year=date.year + 543)
    datetime_stamp = date.strftime(' %d-%m-%Y %H:%M:%S')
    with open(file_name, 'a', encoding='utf-8') as file:
        data = '\n' + 'วัน-เวลา {} ทุเรียนจำนวน {} กก. รวมยอดทั้งหมด: {:,.2f} บาท'.format(datetime_stamp, quantity, total)
        file.write(data)

append_file()