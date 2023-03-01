#Требуется найти в массиве A[1..N]
#самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – 
#количество элементов в массиве. В последующих  строках записаны N целых чисел
#Ai. Последняя строка содержит число X

#*Пример:*

#5
#    1 2 3 4 5
#    6
#    -> 5

import random
random_list = []
for i in range(int(input("Введите количество элементов списка: "))):
    random_list.append(random.randint(1,20))
print(f"Это наш список {random_list} ")
def number_near(n):
    if n in random_list:
        return n
    random_list.append(n)
    random_list.sort()
    return random_list.pop(random_list.index(n) + 1)
print (number_near(int(input("Введите число: "))))
