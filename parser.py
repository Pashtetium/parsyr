
import csv

import datetime







with open("test.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ";")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    d = {
       'time': [],
       'person': [], 
       'company': [] 
    }

    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
            count += 1
        else:
            d = {
                    'time': row[0],
                    'person': row[1] + ' ' + row[2], 
                    'company': row[4] 
            }
            
        
    
    print(f'Всего в файле {count} строк.')
    print(d)
    
