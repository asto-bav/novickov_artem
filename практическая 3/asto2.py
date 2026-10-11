#1
my_list = [1, 2, 3]
print(my_list)
my_list[0] = int(input("На какое число хотите заменить 1 элемент: "))
print(my_list)
#Мы меняем 1 элемент в списке, так как он начинается с 0 а не с 1 то мы меняем элемент 0
#2
my_tuple = (1, 2, 3)
print(my_tuple)
try:
    my_tuple[0] = int(input("На какое число хотите заменить 1 элемент: "))
except TypeError:
    print("Ошибка: кортеж нельзя изменять")
#Кортеж нельзя изменять
#3
my_string = "cat"
print(my_string)
try:
    my_string[0] = input("На какое число хотите заменить 1 элемент: ")
except TypeError:
    print("Ошибка: строку нельзя изменять")
#Cтроку нельзя изменять