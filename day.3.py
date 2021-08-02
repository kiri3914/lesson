'''
#PROBLEM1
a=2**3
b=3**2
if a>b :
	print("a меньше чем b")
elif a == b:
	print("a равна b")
else:
        print("условие неверно")

#PROBLEM2
a=25
b=55

if  a<0 or a>21:
	print('запрещенный')
if b<57 or b>100:
	print('запрещенный')
else:
	print('условия не соблюдены')

#PROBLEM 3
a = 9
print(a)
if a %2:
	print('четное')
else:
	print('не четное')

if a %3:
	print('делится на 3 без остатка')
else:
	print('не делится на 3 без остатка')

s = a**2
if s > 1000: 	
	print('a больше 1000')
else:
	print('a меньше 1000')



#PROBLEMA 4
a = 12
if a*1 and a<1:
	print('ok')
else:
	print('not')

#PROBLEMA5
a=10//5
b=10/5

if a ==b :
	c=a+b
	print(c)
elif a != b : 
	print('not')

#PROBLEM 6
a = 2
a = -a
print(a)

#PROBLEM 7
a = 10 
b = 5
if  a>0 and b>0:
	print('Положительный')

#PROBLEM 8
a=10
b=5
if a>b:
	c=a+2
	print(c)
else:
	f=b+2
	print(f)
#PROBLEM 9

a = float(input("введите число: "))


if  a>0: 
 	print("Положительное число")
elif a<0:
        print("Отрицательное число")
else:
        print("what")

#PROBLEM 10
a = int(input("Введите ваш возрост : "))

if  a>18 or a==18:
        print('Совершеннолетний')
elif a<18 or a==4:
        print('НЕ СОВЕРШЕННОЛЕТНИЙ')
else:

        print('условия не соблюдены')
#PROBLEM 11

a = 45
b = 6
if a/b:
	print('делится' )
else:
	print('не делится')

#PROBLEN 12
a = int(input(" Введиете год : "))

if  a==2021:
        print('Текущий год')
elif a>2021:
	print('Год еще не наступил')
elif a<2021:
        print('Год прошел')
else:
        print('условия не соблюдены')

#PROBLEM 13
a = int(input("Введите ваш возрост : "))

if  a>18 or a==18:
        print('Совершеннолетний')
elif a<4 or a==4:
        print('child')
else:
        print('minor')

#PROBLEM 14
a = 3
b = 4
c = 5

if a>b and a>c: 
	print('large namber' + str(a))
elif b>a and b>c:
	print('large namber' + str(b))
elif c>a and c>b:
	print('large namber' + str(c))

if   a<b and a<c: 
        print('mall namber' + str(a))
elif b<a and b<c:
        print('small namber' + str(b))
elif c<a and c<a:
        print('small namber'+ str(c)) 

#problem 16
a = 13
c = a**2
f = 172 
if c < f:
	print("меньше", + f**2) 

'''