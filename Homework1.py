import pandas as pd
import numpy
import requests



print(">>>>>>>> Библиотека Pandas >>>>>>>>>")
df = pd.read_csv('shoh')  # выводит информации из файла в консоль

print(df.head())
print("Пример№2")

s = pd.Series(numpy.arange(5), index=["a", "b", "c", "d", "e"])
print(s)
print()
s = pd.Series(numpy.linspace(0, 1, 5))
print(s)

print(">>>>>>>>>>>>>>>> Библиотека Numpy>>>>>>>>>>>>>>>>>>>>")
# библиотека numpy
arr = numpy.array([1, 4, 5, 6, 7, 56, 7, 2])
a = numpy.array([1, 2, 3])
b = numpy.array([4, 5, 6])
sum_ = numpy.sum(arr)
flip = numpy.flip(arr)
c = a + b
d = a * b
print("Сумма:", c)
print("Произведение:", d)
print('Суммв масситва:', sum_)
print('Элементы массива в обратном порядке:', flip)

print("Пример №2")
arry = numpy.random.randint(1, 10, size=(5))  # Создаём случайный массив из 5 элементов от 1 до 9

min_value = numpy.min(arry)  # Находим минимальное значение в массиве
max_value = numpy.max(arry)  # Находим максимальное значение в массиве

print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)


print(">>>>>>>>Библиотека Requests>>>>>>>>>>>>")

url = 'https://api.github.com/users/Shohruh' # указывваем URL на который бедм отправлять запрос
response = requests.get(url)
print(response.text)

