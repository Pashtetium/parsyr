
import csv
import types
import datetime



r = types.SimpleNamespace()
r.entry_time = []
r.exit_time = []
r.person = []



with open("test.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ";")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла

    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
            
        else:
            
            filter_time(row[0])
            
            
        count += 1
    print(r.entry_time)
    print(f'Всего в файле {count} строк.')

#  23.10.2020 19:41:01 000
def filter_time(time_string):
    date_time_str = datetime.datetime.strptime(time_string, '%d.%m.%Y %H:%M:%S')
    
