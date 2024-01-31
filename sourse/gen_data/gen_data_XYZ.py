# импортируем необходимые модули
import numpy as np
import random

# генерация 100 случайных точек
x = np.linspace(-10, 10, 100)
y = [random.uniform(-10, 10) for _ in range(100)]
z1 = [random.uniform(-10, 10) for _ in range(100)]
data1 = np.array([x, y, z1]).T

# добавим параметр в данные
z2 = np.sin(x * y)
data2 = np.array([x, y, z2]).T

# добавим шум в данные
z3 = np.sin(x * y) + np.random.normal(0, 0.1, 100)  # добавим шум в данные
data3 = np.array([x, y, z3]).T

# запись данных в файл:

# без параметра
with open('random_dataXYZ.txt', 'w') as f:
    [print(i, j, z, file=f) for i, j, z in data1]

# с параметром без шума
with open('dataXYZ.txt', 'w') as f:
    [print(i, j, t, file=f) for i, j, t in data2]

# с параметром с шумом
with open('dataXYZ_with_hindrance.txt', 'w') as f:
    [print(i, j, z, file=f) for i, j, z in data3]
