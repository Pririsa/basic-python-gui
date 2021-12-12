import csv
import json
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

def timestamp(country):
    date = datetime.now()
    datetime_stamp = date.replace(year=date.year + 543) if country == 'thai' else date
    datetime_stamp = date.strftime('%d-%m-%Y %H:%M:%S' if country == 'thai' else '%Y-%m-%d %H:%M:%S')

    return datetime_stamp

def append_file(quantity, total):
    file_name = 'calculator.txt'
    with open(file_name, 'a', encoding='utf-8') as file:
        data = '\n' + 'วัน-เวลา {} ทุเรียนจำนวน {} กก. รวมยอดทั้งหมด: {:,.2f} บาท'.format(timestamp('thai'), quantity, total)
        file.write(data)

def write_csv(data):
    with open('write_csv_data.csv', 'a', newline='', encoding='utf-8') as file :
        fw = csv.writer(file) #fw = csv file writer
        fw.writerow(data)

def read_csv():
    with open('write_csv_data.csv', newline='', encoding='utf-8') as file :
        fr = csv.reader(file) #fw = csv file writer
        csv_data = list(fr)

    return csv_data

def read_json():
    with open('read_data.json', encoding='utf-8') as file :
        jr = json.loads(file) #fw = csv file writer

    return jr

def write_json(data):
    with open('read_data.json', 'w', encoding='utf-8') as file :
        file.write(data)

def data_calculation():
    data = read_csv()
    list_quantity = []
    list_total = []

    for i in data:
        list_quantity.append(float(i[1]))
        list_total.append(float(i[2]))

    quantity_total = sum(list_quantity)
    total = sum(list_total)

    return (quantity_total, total)

GUI = Tk()
GUI.geometry('600x700')
GUI.title('โปรแกรมของลุง')

file = PhotoImage(file='durian.png')
IMG = Label(GUI,image=file,text='')
IMG.pack()

L1 = Label(GUI,text='โปรแกรมคำนวณทุเรียน',font=('Angsana New',30,'bold'),fg='green')
L1.pack() # .place(x,y) , .grid(row=0,column=0)

L2 = Label(GUI,text='กรุณากรอกจำนวนทุเรียน',font=('Angsana New',20))
L2.pack()

v_quantity = StringVar() #ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลของช่องกรอก

E1 = ttk.Entry(GUI,textvariable=v_quantity,font=('impact',30))
E1.pack()

file_name = 'data.txt'

def Calculate(event=None):
    quantity = v_quantity.get()
    price = 100
    print('จำนวน', float(quantity) * price)
    cal = float(quantity) * price
    
    # append_file(quantity, cal)
    write_csv([timestamp('thai'), quantity, cal])
    cal_result = data_calculation()

    dict_temp = json.dumps({
        'จำนวนที่ขายได้': cal_result[0],
        'ยอดขาย': cal_result[1],
        'ทุเรียนจำนวน': quantity,
        'ราคาทั้งหมด': '{:,.2f}'.format(cal),
    }, ensure_ascii=False, indent=4)

    write_json(dict_temp)
    title = 'ยอดที่ลูกค้าต้องชำระ'
    message = f'ทุเรียนจำนวน {quantity} กิโลกรัม ราคาทั้งหมด: {cal:,.2f} บาท'
    messagebox.showinfo(title, message)

    v_quantity.set('')
    E1.focus()

E1.bind('<Return>', Calculate)

B1 = ttk.Button(GUI, text='คำนวณ',command=Calculate)
B1.pack(ipadx=30,ipady=20,pady=20)

def sum_data(event):
    cal_result = data_calculation()
    title = 'ยอดที่ลูกค้าต้องชำระ'
    message = f'จำนวนที่ขายได้: {cal_result[0]} กก.\nยอดขาย: {cal_result[1]:,.2f} บาท'
    messagebox.showinfo(title, message)

GUI.bind('<F1>', sum_data)


GUI.mainloop()