# '''
# import os 
# print(os.getcwd())

# import random
# a = random.choice(["ok" , "not" , "rot"])
# print (a)
# import random
# c = random.randint(0,57)
# print(c)

# import time
# a = time.localtime(time.time())
# print(a)


# #1
# #Внутри my_module.py создайте вызваннную print которая выводит текст "Я функция из my_module.py". А затем импортируйте my_module.py в другой файл.

# import my_module
# print(my_module)

# #2
# #Вам дан список имён names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"] и вытащите 4 рандомных имени оттуда и сохраните в другой список.
# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# p = []
# i = 0
# while i <4:
#   p.append(random.choice(names))
#   i=i+1
# print (p)

# #вариант 2

# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# p = []
# for i in range(4):
#   p.append(random.choice(names))
# print (p)

# #3
# #Узнайте какая у вас операционная система с помощью модуля sys и выведите на экран имя опрационной системы.

# from sys import platform
# print(platform)
# #4
# #Через терминал передайте Python несколько аргументов, а затем выведите их на экран.

# """from math import pi
# print(pi)
# """

# import sys
# print("Привет {}. Добро пожаловать в руководство по {} на {}".format(sys.argv[1],sys.argv[2],sys.argv[3]))


# #5
# import os
# import random
# os.mkdir("range") 
# for i in range(5):
#   os.mkdir(f'/home/kiri/lesson/range/1{random.randint(1,33)}.txt')


# #6
# #Возьмите список имён из задания №2 и сформируйте 4 разные команды из всех участников.
# from random import *
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# k1 = []
# k2 = []
# k3 = []
# k4 = []
# i = 0
# while i < 3:
#   q = choice(names)
#   if q not in k1:
#     k1.append(q)
#     i+=1
# i = 0
# while i < 3:
#   f = choice(names)
#   if f not in k1 and f not in k2:
#     k2.append(f)
#     i+=1
# i = 0
# while i < 3:
#   q = choice(names)
#   if q not in k1 and q not in k2 and q not in k3:
#     k3.append(q)
#     i+=1
# i = 0
# while i < 3:
#   f = choice(names)
#   if f not in k1 and f not in k2 and f not in k3 and f not in k4:
#     k4.append(f)
#     i+=1
# print("Команда 1",k1)
# print("Команда 2",k2)
# print("Команда 3",k3)
# print("Команда 4",k4)


# #8
# # Создайте программу которая спрашивает у пользователя число N для генерации пароля а затем генерирует ему пароль длиною N символов.
# from random import *
# from string import *
# l = int(input("Введите число : "))
# password = ""
# for i in range(0,l):
#   password += choice(ascii_letters)

# print("Ваш пароль : ",password)

# #9
# #Камень-Ножницы-Бумага
# from random import *
# a = input("Выберите\nКамень 1\nНожницы 2\nБумага 3\n Ваш выбор : ")
# a1 = ["Камень","Бумага","Ножницы"] 
# if a == "1":
#   i = choice(a1)
#   if i == "Камень":
#     print("Компютер выбрал ",i," Ничья")
#   if i == "Бумага":
#     print("Компютер выбрал ",i, " Вы Победили!!!" )
#   elif i == 'Ножницы':
#     print("Компютер выбрал ",i,'Вы ПРОИГРАЛИ!!!')
# if a == "2":
#   i = choice(a1)
#   if i == "Камень":
#     print("Компютер выбрал ",i," Вы ПРОИГРАЛИ!!!")
#   if i == "Бумага":
#     print("Компютер выбрал ",i, " Вы Победили!!!" )
#   elif i == 'Ножницы':
#     print("Компютер выбрал ",i,' Ничья')

# if a == "3":
#   i = choice(a1)
#   if i == "Камень":
#     print("Компютер выбрал ",i," Вы Победили!!!")
#   if i == "Бумага":
#     print("Компютер выбрал ",i, " Ничья" )
#   elif i == 'Ножницы':
#     print("Компютер выбрал ",i,'Вы ПРОИГРАЛИ!!!')

# #10
# #Используя функцию randrange() получите псевдослучайное четное число в пределах от 6 до 12.
# #Также получите число кратное пяти в пределах от 5 до 100.
# '''

# from random import *
# a = randrange(6,12,2)
# print(a)

# a = randrange(5,100,5)
# print(a)

# '''
# #12
# #Определить дату, которая наступит через 1000 дней от текущей даты
# from datetime import *
# d = datetime.now()
# t = timedelta(days=1000)
# r = d+t
# print(r)

# '''