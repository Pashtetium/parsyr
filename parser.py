import csv
import json
import datetime

data = []      # Основное хранилище

rows_to_skip = 1   # Переменные для пропуска первой строки в csv файле
rows_read = 0      #

#Отрезаем лишние символы в строке времени ("23.10.2020 19:41:01 000")
def time_slicing(end_date):
    return end_date[:end_date.rindex(" ")]

#Преобразывываем обрезанную строку в формат datetime
def str_to_datetime(sliced_str):
    return datetime.datetime.strptime(sliced_str, "%d.%m.%Y %H:%M:%S")


def search(name):
    for p in data:
        if p['person'] == person:
            return p['person']

#Считываем данные из csv файла в структуру dict 
with open('test.csv', encoding='utf-8') as r_file:
    reader = csv.reader(r_file, delimiter = ";")
          
    for row in reader:
        if rows_read >= rows_to_skip:            
           sliced_time_str = time_slicing(row[0])    
           time = str_to_datetime(sliced_time_str)                   
           person = row[1] + " " + row[2]
           address = row[3]
           company = row[4]
           if 'vhod' in address:
               entry_time = time
               exit_time = datetime.datetime.min
           elif 'vyhod' in address:
               entry_time = datetime.datetime.max
               exit_time = time
           buffer_dict = {
               'person' : person, 
               'entry_time': entry_time,
               'exit_time': exit_time                   
             
           }
              
            
           if person == search(person):  
               for index in data:
                   if time < index['entry_time']:                  
                      index['entry_time'] = time                      
                   elif time > index['exit_time']:
                      index['exit_time'] = time 
           else:                
               data.append(buffer_dict)          
                      
        rows_read += 1
    # Как настоящий джентльмен, не допускаем утечек
    r_file.close()
for p in data:
    print(p)

"""
for person in data:
    x = data.get(person)
    entry_time_min = x["entry_time"]
    if entry_time < entry_time_min:
        entry_time_min = entry_time
"""