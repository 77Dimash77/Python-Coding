# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
randlist = []
length = int(input('Введите длинну списка: '))
min = int(input('Введите минимуc: '))
max = int(input('Введите макимус: '))
index = 0
listindex = []
while len(randlist) < length:
  randlist.append(random.randint(-10,10))
print('Составленный список: ',randlist)
for i in randlist:
  if i <= max and i >= min:
    listindex.append(index)
    index +=1
  else:
    index +=1
print('Индексы элиментов между мин и макс: ',listindex)
