#Требуется вычислить, сколько раз встречается некоторое число X в массиве
#A[1..N]. Пользователь в первой строке вводит натуральное число N – 
#количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
#Последняя строка содержит число X

#*Пример:*

#5
 #   1 2 3 4 5
  #  3
   # -> 1
import random
num_list =[]
for i in range(int(input("количество элементов в массиве:? "))):
    num_list.append(random.randint(1,15))
user_number = (int(input("Введите число от 1 до 15: ")))
if user_number > 16:
   print("Введите корректное число")
print(f"Это данный массив{num_list}")  
count = 0
for i in range(len(num_list)):
    if user_number == num_list[i]:
      count += 1
print(f"В данном массиве ваше число встречается {count} раз")      

     