'''
i = 1000
while i > 10:
	print(i)
	i /= 2
'''
'''
for j in range(0, 4):
	print('privet %s' % j)

print(list(range(10,20)))
cow = 4
letl_cow = 4
cow_down = 1
cow_vse = cow
print(cow+50*(letl_cow - cow_down))

for i in range(1,51):
	cow_vse = cow_vse + letl_cow - cow_down
	print("День %s Стало %s" % (i,cow_vse))
"""%S озночает места где может быть значение %"""
'''

#код ищет значение sub_str в значении languages

'''languages=['go','java','php','python','javascript','ruby']
s = input('Искать: ')
for i, j in enumerate(languages):
	if j.count(s) !=0:
		print('Найден', j, "оно под номером", i + 1)'''

#enumerate - считывать внутри переменного
#count - найти значение переменного
#type - проверяет тип 
#.appen - добавлять
#len() - показывает сколько значений в обьекте
#while - подробно https://www.youtube.com/watch?v=Ll3AN1FXXfE



#УДАЛЕНИЕ ОПРЕДЕЛЕННОГО ОБЬЕКТА ВНУТРИ ЛИСТА
'''names = ['Jack','Oskar', 'Jimmy', 'Jackson','Oskar', 'Jhon', 'Jackson', 'Jhon', "Oskar", 'Jimmy', 'Jackson','Oskar', 'Jhon','Jack', "Oskar", 'Jimmy', 'Jack', "Oskar", 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]

f = 'Oskar'
while f in names:
	names.remove(f)
	print(names)'''




#Как запрашивать пороль!!!
'''
password = int(input("Придумайте пороль : \n "))
repeat_password = int(input("Повторите пороль : \n "))
repeat_password = password
while repeat_password != password: 
	print("Не совпало!!!")
	repeat_password = int(input("Повторите еще раз : \n "))

a = int(input("Ведите пороль : \n ")) 
count = 1
while a != password: 
	count+=1
	print("Не верный пороль!!!")
	a = int(input("Повторите еще раз : \n "))
if a == password:
	print("Верный пороль!!!")
print("Вы потратили " , count ," попыток!!!")	

'''

# КОД КОТОРЫЙ ЗЛОМАЕТ ЛЮБОЙ ПОРОЛЬ!!!
password = int(input("Придумайте ШЕСТИЗНАЧНЫЙ пороль : \n "))
if password < 100000:                                           
	while password < 100000 :
		password = int(input("Пороль НЕ ШЕСТИЗНАЧНЫЙ значений!!!  \nПовторите еще раз:  "))
if password > 999999:
	while password >999999  :
		password = int(input("Пороль НЕ ШЕСТИЗНАЧНЫЙ значений!!!  \nПовторите еще раз:  "))

a = input('Если хотите зломать пороль НАПИШИТЕ "+" :\n ' )
while a != "+": 
		a = input('НАПИШИТЕ "+" :\n ' )

count = 1
s = 0
while s != password: 
	print("Не верный пороль!!!")
	while s != password:
		count+=1
		print(s," Не верный пороль!")
		s+=1

print("Верный пороль!!!" , "Ваш пороль", password)
print("Вы потратили " , count ," попыток!!!")

