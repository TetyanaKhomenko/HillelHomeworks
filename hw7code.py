# 1. Дано целое число (int). Определить сколько нулей в этом числе.
#########################1
my_int = list(input("Enter a number:"))
num_of_zeroes = 0
for number in range(len(my_int)):
    if my_int[number] == '0':
        num_of_zeroes += 1
print(num_of_zeroes)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
##########################2
my_int = int(input("Enter a number:"))
res_2 = 0
while my_int % 10 == 0:
    my_int //= 10
    res_2 += 1
print(res_2)

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
##########################3
my_list_1 = input("Enter a first list of elements,separated by commas:").split(",")
my_list_2 = input("Enter a second list of elements,separated by commas:").split(",")
my_result = my_list_1[::2]
print(my_result)
my_result.extend(my_list_2[1:len(my_list_2) + 1:2])
print(my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
##########################4
my_list = input("Enter a list of elements,separated by commas:").split(",")
new_list = []
new_list.extend(my_list)
new_list.append(new_list.pop(0))
print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
#########################5
my_list = input("Enter a list of elements,separated by commas:").split(",")
my_list.append(my_list.pop(0))
print(my_list)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
##########################6
my_str = "43 больше чем 34 но меньше чем 56".split()
num_in_str = []
for element in my_str:
    if element.isdigit():
        num_in_str.append(int(element))
sum_of_num = sum(num_in_str)
print(sum_of_num)

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
##########################7
my_str = "My long string"
l_limit = "o"
l_limit_index = my_str.find(l_limit)
r_limit = "g"
r_limit_index = my_str.rfind(r_limit)
sub_str = my_str[l_limit_index + 1:r_limit_index]
print(sub_str)

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
my_str = input("Enter a string:")
new_list = []
for index in range(0, len(my_str), 2):
    if index < len(my_str) - 1:
        new_list.append(my_str[index:index + 2])
    else:
        new_list.append(my_str[index] + "_")
print(new_list)

# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
#########################9
list_of_num = [2, 4, 1, 5, 3, 9, 0, 7]
counter = 0
for element in range(1, len(list_of_num) - 1):
    if list_of_num[element - 1] < list_of_num[element] > list_of_num[element + 1]:
        counter += 1
print(counter)
