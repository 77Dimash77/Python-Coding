# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
def Zadacha22():
  import random
  x = int(input('Введите длинну первого набора: '))
  y = int(input('Введите длинну второго набора: '))
  xl, yl = [], []
  for i in range(1, x+1):
    xl.append(random.randint(1,x))
  print(xl)
  for j in range(1, y+1):
    yl.append(random.randint(1,y))
  print(yl)
  xl = set(xl)
  yl = set(yl)
  cl = xl.intersection(yl)
  print(f'числа которые повтаряються в первои и втором наборе: {cl}')
Zadacha22()