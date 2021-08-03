#####################################################1
value = int(input("Enter a number:"))
if value < 100:
    new_value = value / 2
else:
    new_value = -value
print(new_value)

#####################################################2
value = int(input("Enter a number:"))
if value < 100:
    new_value = 1
else:
    new_value = 0
print(new_value)

#####################################################3
value = int(input("Enter a number:"))
if value < 100:
    new_value = True
else:
    new_value = False
print(new_value)

#####################################################4
my_str = input("Enter a string:")
print(my_str[::2])

#####################################################5
my_str = input("Enter a string:")
print(my_str[::2])


#####################################################6
my_str = input("Enter a string:")
if len(my_str) >= 5:
    print(my_str)
else:
    print(my_str * 2)

#####################################################7
my_str = input("Enter a string:")
if len(my_str) >= 5:
    print(my_str)
else:
    print(my_str + my_str[::-1])

