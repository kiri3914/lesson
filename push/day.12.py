'''
#1
#Представьте Вы хотите взять какой-то набор данных и переконвертировать его в SET для удаления дубликатов,
#в Classroom возьмите values и проверьте каждый ли элемент доступен для конвертации. 
#Создайте список. Проитерируйте values.
#Если объект в списке можно переконвертировать добавьте True в новый список иначе добавьте False.
#После, с помощью функции all() скажите можно ли конвертировать values в SET?

values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
a1 = []
for x in values:
	try:
		set(x)
		a1.append(True)
	except TypeError :
		a1.append(False)

print(a1)
print(all(a1))

#2
#Спросите у пользователя 5 чисел добавьте их в SET и скажите какое самое маленькое число он ввел.
r = []
for i in range(5):
	a = input("Введите цифры : ")
	r.append(a)

print(min(r))

#3
'''w = ["all","any","abs","min","eval","reversed","max","slice","round"]
d = input("напиши функцию: ")
try:
	for i in range(1):
		if d in w:
	    	print("есть такая функция")
		else:
			print(d, "такой функции нет")
except IndexError:
	print("у вас не правильно")'''

#4 
#Вы работаете в Банке и пишите программу которая считает % для кредита. Спросите у пользователя сумму займа(не меньше 50 000) и посчитайте сколько нужно будет вернуть если % = 3.47, результат округлите до 2 чисел после точки. 
#Формула подсчёта переплаты: Сумма * (% / 100)

s = int(input("Введите сумму Кредита (не меньше 50 000!!!) :  "))
while s < 50000:
	s = int(input("Введите сумму Кредита (не меньше 50 000!!!) : "))
p = 3.47 
a = s * (p / 100)
print("Сумма переплаты",round(a,2))
print("Общая Сумма оплаты",s+a)


#5
#Напишите код где есть TypeError,IndexError,NameError

try:
	a = ("a"+5)
except TypeError:
	print("обнаружена TypeError")
try:
	f = (s+5)
except NameError:
	print("обнаружена NameError")
try:
	r = ["2"]
	print(r[3])
except IndexError:
	print("обнаружена IndexError")
finally:
	print("Конец операции")

#6
#Возьмите код #1 с Classroom и создайте для него try... except...
try:
	at = 10
	i = 15
	wo = 20

	for e in range(-at, at):
		print(wo / e)
	if at > '5':
		print("at > 5")

except ZeroDivisionError:
	print("поймано ZeroDivisionError")

finally:
	print("Были исправлены IndentationError,SyntaxError")

#7
#Перенесите к себе код #2 с Classroom и исправьте все ошибки, сделайте так чтобы работал.
#Если не знаете как исправить ошибку создайте для неё except выражение.
try:
	lst = []
	for i in range(10):
		lst.append(i)

		a = list(reversed(lst))
		sls_obj = slice(0,8)
	print(a[sls_obj])
finally:
	print("Были исправлены NameError,AttributeError,TypeError")


#8
#Перенесите к себе код #3 с Classroom и исправьте все ошибки, сделайте так чтобы код работал. 
#Если не знаете как исправить ошибку создайте для неё except выражение.

try:
	a = 0
	b = 1
	numbers = []
	while b < a:
		numbers.append(b)
		b += 1
finally:
	print("Были исправлены IndentationError,TypeError,RuntimeError")


#9
#Дан словарь в котором ключи должны быть только строковыми объектами, 
#но может встретиться Int, как в качестве ключа, 
#но ваша проверка только проверяет на строку и поэтому у вас выходит баг, 
#ваша задача обработать исключением ошибку TypeError

#Пример:
#dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
#for x in dict_.keys():
#x + 'abc'
#Запустить код
#Обработайте исключение
try:
	dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
	for x in dict_.keys():
		x + 'abc'

except TypeError:
	pass
finally:
	print("Были исправлены ошибки и было исключено TypeError")
'''












