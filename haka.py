from random import *
names = ["Рамиль","Бектур","Вова","Динара","Жибека","Улан","Баэль",'Nurmamat', 'Nurayim']
k1 = []
k2 = []
i = 0
while i < 5:
  q = choice(names)
  if q not in k1:
    k1.append(q)
    i+=1
i = 0
while i < 4:
  q = choice(names)
  if q not in k1 and q not in k2:
    k2.append(q)
    i+=1

if "Рамиль" in k1 and "Вова" in k1:
  print("Возможно команда 1 сильнее")
if "Рамиль" in k2 and "Вова" in k2:
  print("Возможно команда 2 сильнее") 
print("Команда 1",k1)
print("Команда 2",k2)

