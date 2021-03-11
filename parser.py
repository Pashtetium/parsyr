import csv
import json
from datetime import datetime as dt

data = {}       # Основное хранилище

rows_to_skip = 1   # Переменные для пропуска первой строки в csv файле
rows_read = 0      #

#Отрезаем лишние символы в строке времени ("23.10.2020 19:41:01 000")
def time_slicing(end_date):
    return end_date[:end_date.rindex(" ")]

#Преобразывываем обрезанную строку в формат datetime
def str_to_datetime(sliced_str):
    return dt.strptime(sliced_str, "%d.%m.%Y %H:%M:%S")

#def comparingTime(time_str, person):
#    for time_str in data:
 #       if data[person]



#Считываем данные из csv файла в структуру dict 
with open('test.csv', encoding='utf-8') as r_file:
    reader = csv.reader(r_file, delimiter = ";")
          
    for row in reader:
        if rows_read >= rows_to_skip:            
           sliced_time_str = time_slicing(row[0]) 
           
               
                   
           person = row[1] + " " + row[2]
           address = row[3]
           company = row[4]
           buffer_dict = {
               #'entry_time':entry_time,
               #'exit_time':exit_time, 
               'person':person, 
               'address': address, 
               'company':company
            }              
           time = str_to_datetime(sliced_time_str)
            
           
           if person in data:
               if time < data.get(person).get('buffer_dict').get('entry_time'):
                    data[person]['buffer_dict']['entry_time'] = time                                  
               elif time > data[person]['buffer_dict']['exit_time']:
                    data[person]['buffer_dict']['exit_time'] = time 
           else:
                #data[person]['buffer_dict'].append(buffer_dict)
                data[person] = {'buffer_dict':[buffer_dict]}   

            
        rows_read += 1
    # Как настоящий джентльмен, не допускаем утечек
    r_file.close()
print(data)
"""
for person in data:
    x = data.get(person)
    entry_time_min = x["entry_time"]
    if entry_time < entry_time_min:
        entry_time_min = entry_time
"""