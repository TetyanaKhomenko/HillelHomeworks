# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).
import os
from datetime import datetime

path = "D:\pythonProject\hillel homeworks"


def domains_function(given_file):
    path_given_file = os.path.join(path, given_file)
    data = []
    with open(path_given_file, "r") as txt_file:
         for line in txt_file.readlines():
            data.append(line.strip().strip("."))
    return data
print(domains_function("domains.txt"))

# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"
path = "D:\pythonProject\hillel homeworks"
def surname_function(given_file2):
    first_data = []
    result_data = []
    path_given_file2 = os.path.join(path, given_file2)
    with open(path_given_file2, "r") as txt_file:
        for line in txt_file.readlines():
            first_data.append(line.strip().split("\t"))
        for element in first_data:
            result_data.append(element[1])
    return result_data
print(surname_function("names.txt"))

# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
path = "D:\pythonProject\hillel homeworks"
list_of_dicts = []
def original_data_function(given_file3):
    path_given_file3 = os.path.join(path, given_file3)
    with open(path_given_file3, "r") as txt_file:
         for line in txt_file.readlines():
             file_line = line.split(" - ")
             if len(file_line) > 1:
                date = file_line[0]
                day, month, year = date.split()
                my_date = datetime.strptime(f"{day[:-2]} {month} {year}", "%d %B %Y")
                list_of_dicts.append(
                      {
                        "date_original": date,
                        "date_modified": datetime.strftime(my_date, "%d/%m/%Y"),
                      }
                )
    return list_of_dicts


print(original_data_function("authors.txt"))
