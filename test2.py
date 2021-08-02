
what = input( "Выбери значение (+, -):" )


a = float( input("Первое число: "))
b = float( input("Второе число: "))


if what == "+": 
	c = float(a) + float(b)
	print("результат: " + str(c))

elif what == "-":
	c = float(a) - float(b)
	print("результат" + str(c))
else:
        print("Выбрана не верная операция!")

