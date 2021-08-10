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
  f = choice(names)
  if f not in k1 and f not in k2:
    k2.append(f)
    i+=1
print(k1)
print(k2)

