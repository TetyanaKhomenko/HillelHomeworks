# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.
######################1
my_list = [ "123", "qwe", "01", "ro"]
my_list1 = []
for index in range(len(my_list)):
    if index % 2 == 0:
        my_list1.append(my_list[index][::-1])
    else:
        my_list1.append(my_list[index])
print(my_list1)

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
######################2
my_list = ["112", "a34", "A4", "bbb", "AaA", "Tanya"]
a_elements = [element for element in my_list if element.lower().startswith("a")]
print(a_elements)

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
######################3
my_list = ["1a2", "a34", "A4", "bAb", "bbb5", "Tanya"]
a_elements = []
for element in my_list:
    if element.lower().__contains__("a"):
        a_elements.append(element)
print(a_elements)

# 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.
######################4
my_list = [1, 2, 3, "11", "22", 33]
only_str = [element for element in my_list if type(element) is str]
print(only_str)

# В заданиях 5,6,7 надо использовать множества
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.
######################5
my_str = "1234455666677777888"
my_set = set(my_str)
unique_symbols = []
for symbol in my_set:
    if my_str.count(symbol) == 1:
        unique_symbols.append(symbol)
print(unique_symbols)

# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
######################6
my_str1 = "1a2b3c4d5e6f7gaaccc"
my_str2 = "?gj123aaa"
res_list = list(set(my_str1).intersection(set(my_str2)))
print(res_list)

# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
######################7
my_str1 = "1a2b3c4d5e6f7gaaccc"
my_str2 = "?gj123aaa"
my_intersection = set(my_str1).intersection(set(my_str2))
res_list = []
for symbol in my_intersection:
    if my_str1.count(symbol) == 1 and my_str2.count(symbol) == 1:
        res_list.append(symbol)
print(res_list)

# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность
######################8
person_dict = {"Фамилия": "Петров",
               "Имя": "Иван",
               "Возраст": 35,
               "Проживание": {"страна": "Украина", "город":"Киев","улица": "Ломоносова"},
               "Работа": {"наличие": "+",
               "должность": "Junior Python Developer"}
              }
print(person_dict)

# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло
######################9
cake_dict ={"Коржи": {"мука": "150 г", "молоко": "500 мл", "масло": "115 г", "яйца": "4 шт"},
            "Крем": {"сахар": "250 г", "масло": "20 г", "ваниль": "5 г", "сметана": "5 ст л"},
            "Глазурь": {"какао": "0,5 стакана", "сахар": "1 стакан", "масло": "4 ст л"}

            }
print(cake_dict)

# 10) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
#######################10
import statistics
list_of_dicts = [
    {"name": "John", "age": 15},
    {"name": "Jack", "age": 45},
    {"name": "Catherine", "age": 15},
    {"name": "Cleo", "age": 67}
    ]
#a
ages = []
for age in list_of_dicts:
    ages.append(age["age"])
min_age = min(ages)

for person in list_of_dicts:
    if person["age"] == min_age:
        print(person["name"])

#б
names = []
for name in list_of_dicts:
    names.append(len(name["name"]))
max_name = max(names)

for person in list_of_dicts:
    if len(person["name"]) == max_name:
        print(person["name"])

#в
print(statistics.mean(ages))


# 11) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
######################11
my_dict1 = {"country": "Ukraine", "population": "44.39 million", "climate": "continental", "language": "Ukrainian"}
my_dict2 = {"country": "Mexico", "population": "127.6 million", "currency": "peso", "calling code": "+52"}
#a
list_of_keys = list(set(my_dict1).intersection(set(my_dict2)))
#б
only_in_dict1 = list(set(my_dict1).difference(set(my_dict2)))
#в
new_dict = {}
for key in only_in_dict1:
    new_dict[key] = my_dict1[key]
#г
mega_dict = {}

for key in list_of_keys:
    mega_dict[key] = my_dict1[key],my_dict2[key]

only_in_dict2 = list(set(my_dict2).difference(set(my_dict1)))
for key in only_in_dict1:
    mega_dict[key] = my_dict1[key]
for key in only_in_dict2:
    mega_dict[key] = my_dict2[key]
print(mega_dict)

