
a = int(input('Напиши любую цифру: '))
b = int(input('Напиши любую цифру от 1 до 200: '))

if b < 1 or b > 200:
	print("Вы выбрали не верное значение!!!")

what = input('Введите "+" ИЛИ Введите "-" : ')

if what == "+": 
	c = float(a) + float(b)
	print("результат: " + str(c))
if what == "-":
	for i in range(a, b):
		print(i, end = " ")
else:
        print("Выбрана не верная операция!")

u = input("Напишите комнетарий")

e = input('Напишите "yes: "')

if e == "yes": 
	for i in range(0, int(a)):
		print(u, [i])

if e != "yes":
	print("Выбрана не верная операция!")






