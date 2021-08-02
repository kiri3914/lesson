'''
#PROBLEM 0 

#Создать список и 5 вложенных кортежей

names = []

b = ('Jack')
c = ('Jimmy')
d = ('Jackson')
r = ('Jhon')
o = ('Jackson')


names.append(b)
names.append(c)
names.append(d)
names.append(r)
names.append(o)
print(names)

#problem 1 

#Создать Tuple из 3 элементов и вывести каждый из них по индексу.

t = ("for", 5 , 77)

print(t[0:3])


#problem 2 

#Создать Лист и заполнить его 5 РАЗНЫМИ ТИПАМИ ДАННЫХ.

names = []

b = 'true'
c = 555
d = "привет"
r = 'Jhon'
o = ('Jackson')


names.append(b)
names.append(c)
names.append(d)
names.append(r)
names.append(o)
print(names)

#problem 3 

#1.Создать Лист из 5 разных имён.

#2.Создать пустую строку и через .join() соеденить пустую строку и все имена в списке.

l = ['Jack','Jimmy', 'Jackson', 'Jhon', 'Jackson']

a = " "

p = a.join(l)

print(p)

#PROBLEM 4

#Создать 2 списка(List) заполнить данными, к первому списку добавить все объекты второго списка

l = ['Jack','Jimmy', 'Jackson', 'Jhon', 'Jackson']
c = ['Jack','Jimmy', 'Jackson', 'Jhon', 'Jackson']

p = c+l
print(p)

#PROBLEM 5

Взять Лист №1 из Google Colab и посчитать сколько раз там встречается имя "Jack".
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]

t = names.count('Jack')

print(t)


#PROBLEM 6

#Удалить из Листа №1 объект "Oskar"

names = ['Jack','Oskar', 'Jimmy', 'Jackson','Oskar', 'Jhon', 'Jackson', 'Jhon', "Oskar", 'Jimmy', 'Jackson','Oskar', 'Jhon','Jack', "Oskar", 'Jimmy', 'Jack', "Oskar", 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
s = 0
f = 'Oskar'
while f in names:
	names.remove(f)
	s += 1 
	print(names,"\n" , s , "раз была удалена имя Oskar")


# ВАРИАНТ С ИСПОЛЬЗОВАНИЕМ FOR

names = ['Jack','Oskar', 'Jimmy', 'Jackson','Oskar', 'Jhon', 'Jackson', 'Jhon', "Oskar", 'Jimmy', 'Jackson','Oskar', 'Jhon','Jack', "Oskar", 'Jimmy', 'Jack', "Oskar", 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
f = 'Oskar'
for f in names:
	if f == "Oskar":
		names.remove(f)
		print(names)
	
			
#PROBLEM 7

#Создать пустой лист.

#Добавить в него сначала Ваше Имя, Год Рождения, любимый Язык Программирования.

x = []

b = ("kiri")
c = 2002
d = ('python')

x.append(b)
x.append(c)
x.append(d)
print(x)

#PROBLEM 8

#Взять Лист №2 из Google Colab узнать индекс объекта(строки) "loop" и удалить его по индексу 

pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]

p = lun()

print(pythonList[6])

#PROBLEM 9
#Взять Лист №3 из Google Colab и посчитать произведение этих чисел т.е. умножить их все и вывести результат.

numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
s = 1
for i in numbers:
	s *= i
	print(numbers , s)

i = 0
s = 1 
d = len(numbers)
if i < d:
	while i in numbers:
		s*=i
		print(numbers, s)


'''
#PROBLEM 10
#Взять строку №1 создать два списка numbers и letters, пройтись по каждому элементу строки №1 и в numbers добавлять только числа, а в letters буквы

spisok_1 = "'Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23"

letters = []
numbers = []
for i in spisok_1:
	if i.isnumeric():
		numbers.append(int(i))
	else:
		letters.append(i)
		print(numbers, "\n", letters)





'''#PROBLEM 11
#Взять Лист №2 и вывести объекты с 1 по 3 индекс 

pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]

for i in pythonList[0:3]:
	print(i, end=" ")

'''
