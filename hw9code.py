# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
#######################1
def list_function(my_list=["123", "qwe", "01", "ro"]):
    new_list = []
    for index in range(len(my_list)):
        if index % 2 == 0:
            new_list.append(my_list[index][::-1])
        else:
            new_list.append(my_list[index])

    return new_list
print(list_function())

# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".
########################2
def a_function(my_list = ["112", "a34", "A4", "bbb", "AaA", "Tanya"]):
    new_list = [element for element in my_list if element.lower().startswith("a")]
    return new_list
print(a_function())

# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.
########################3
def anywhere_function(my_list=["1a2", "a34", "A4", "bAb", "bbb5", "Tanya"]):
    a_elements = []
    for element in my_list:
        if element.lower().__contains__("a"):
            a_elements.append(element)
    return a_elements
print(anywhere_function())

# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
########################4
def str_function(my_list=[1, 2, 3, "11", "22", 33]):
    only_str = [element for element in my_list if type(element) is str]
    return only_str
print(str_function())

# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
########################5
def once_function(my_str = "1234455666677777888"):
    my_set = set(my_str)
    unique_symbols = []
    for symbol in my_set:
        if my_str.count(symbol) == 1:
            unique_symbols.append(symbol)
    return unique_symbols
print(once_function())

# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
# ########################6
def list_function(my_str1 = "1a2b3c4d5e6f7gaaccc", my_str2 = "?gj123aaa"):
    res_list = list(set(my_str1).intersection(set(my_str2)))
    return res_list
print(list_function())

# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
########################7
def list_function(my_str1 = "1a2b3c4d5e6f7gaaccc", my_str2 = "?gj123aaa"):
    my_intersection = set(my_str1).intersection(set(my_str2))
    res_list = []
    for symbol in my_intersection:
        if my_str1.count(symbol) == 1:
            res_list.append(symbol)
    return res_list
print(list_function())

# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com
########################8
from string import ascii_lowercase
import random
from random import randint, choice

def creat_email(names = ["student", "parent", "teacher"],domains = ["net", "com", "ua"]):
    e_mail = f"{random.choice(names)}.{randint(100, 1000)}@{''.join(choice(ascii_lowercase) for i in range(randint(5,7)))}.{random.choice(domains)}"
    return e_mail
print(creat_email())
