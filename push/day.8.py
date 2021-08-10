'''
#Problem 0
#Из множества 
#№ 1 в Google Colab - удалите число 7

dates_of_birth = {3,7,10,11,13,31,7,21,1,10,3,7,7,5,6,7,6}
while 7 in dates_of_birth:
    dates_of_birth.remove(7)
    print(dates_of_birth)

dates_of_birth.remove(7)
print(dates_of_birth)


#Problem 1
#Найти объекты которые есть и в SET №2 и в SET №3 из Google Colab 
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
a = farm_1.intersection(farm_2)
print(a)

#Problem 2
#В SET №3 из Google Colab найдите объекты которых нет SET №2

farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
f = farm_1.difference(farm_2)
print(f)

#Problem 3
#Создайте SET из 5 элементов. Потом добавьте в SET ещё один элемент.
#А затем удалите через .pop() элемент и посмотрите что же вы удалили.

i = {23,24,55,66,5}
i.add(7)
i.pop()
print(i)

#Problem 000:
#Из Dictionary №1:
#Добавьте в меню 
#'besh_barmak' который стоит  130 сом.
#Оказалось лагман слишком дешевый. Обновите цену на 135
#Ваш повар отвратительно готовит борщ, поэтому хотите удалить это блюдо.
#Удалить borsh

menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
b = {'bech_barmak': 130}
menu.update(b)
print(menu)
menu['lagman']=135
print(menu)
menu.pop('borsh')
print(menu)


#Problem 10:
#Из Dictionary №1:
#Добавьте в меню
#напитки как ключ "drinks", 
#А список всех доступных напитков: ['Coca-Cola', 'Sprite', 'Fanta'] как его значение.

menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['drinks']=['Coca-Cola', 'Sprite', 'Fanta']  
print(menu)

#Problem 020:
#Создайте SET который хранит в себе все методы  для работы  с  SET.
#Создайте второй SET который хранит в себе  методы  для работы  с  Dictionary которые вы сегодня узнали.
#Проверьте какие методы похожи у этих типов данные.

a = {'.add','.update', '.intersection','.remove','.clear','.update','.difference','.discard','.intersection','.intersection_update','.pop'}
b = {'.clear', '.get','.values','.update'}
c = a.intersection(b)
print(c)

#Problem 31:
#Создайте пустой словарь.
#Запустите цикл который 3 раза спросит его имя и его пароль.
#Записывайте имя пользователя как ключ, а пароль как его значение.

l = {}
for i in range(3):
    a = input('Введите имя :')

for i in range(3):
    b =  int(input('Введите пaроль : '))
l[a]=b
print(l)


#Problem 27:
#Создайте Dictionary с 5 элементами где ключи это их имена, а значение их профессия.
#С помощь цикла for пройти вывести на экран строку:
#"Здравствуйте <Имя>  Прекрасная профессия <Профессия>"

a = {'Azat': 'mentor' , 'Айдар' : 'Мерчендайзер', "Улан": "Астронафт" , "Нурайым":"Бухгалтер" , "Баэл":"Таксист" }
for i , y in a.items():
    print("Здраствуйте", i ,"Прекрастная профессия" ,y )

#Problem 22:
#Создайте цикл который справшивает у пользователя 10 чисел и добавьте их в SET.
#Сделайте так чтобы эти данные уже никто не смог поменять позже.
a = set()
for x in range(10):
    p = input("Введите номер : ")
    a.add(p)
print(a)

#Problem 11:
#Есть список Южноамериканских стран
#Google Colab - 
#СПИСОК №2
#в котором Суринам встречается два раза. Необходимо написать программу,
#которая удалит дублирующуюся запись, и возвратит в результате список


south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',    'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
a = {}
a=set(south_american_countries)
print(list(a))

#Problem 101:
#Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст: 
#suitcase = [] 
#Однако он
#может вместить всего 5 вещей.
#Положите 5 вещей в чемодан.
#Вы передумали, и решили убрать последнюю вещь. 
#1 вариянт
suitcase = [] 
suitcase.append("чемодан")
suitcase.append("штаны")
suitcase.append("шокалад")
suitcase.append("тапки")
suitcase.append("слансы")
suitcase.remove("слансы")
print(suitcase)
#2 вариянт
suitcase=[]
i=0
while i<5:
 i+=1
 h=input('please add clothes?')
 suitcase.append(h)
print (suitcase)
suitcase.pop(4)
print(suitcase)
'''
#Problem 001:
#Из Google Colab Множество 4 и 5
#Напишите код, который: Выведет новое множество, которое есть как в
#первой ферме, так и во второй.





