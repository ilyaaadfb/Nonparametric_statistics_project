# импортируем необходимые модули
import numpy as np
import random

# генерация 100 случайных точек
x = np.linspace(-10, 10, 100)
y1 = [random.uniform(-10, 10) for _ in range(100)]
data1 = np.array([x, y1]).T

# добавим параметр в данные
y2 = np.sin(x)
data2 = np.array([x, y2]).T

# добавим шум в данные
y3 = np.sin(x) + np.random.normal(0, 0.1, 100)
data3 = np.array([x, y3]).T

# запись данных в файл:

# без параметра
with open('random_dataXY.txt', 'w') as f:
    [print(i, j, file=f) for i, j, in data1]

# с параметром без шума
with open('dataXY.txt', 'w') as f:
    [print(i, j, file=f) for i, j, in data2]

# с параметром с шумом
with open('dataXY_with_hindrance.txt', 'w') as f:
    [print(i, j, file=f) for i, j, in data3]
