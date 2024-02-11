# импортируем необходимые модули
import numpy as np
import random

# генерация 100 случайных точек
X = np.linspace(-10, 10, 100)
Y = np.linspace(-10, 10, 100)
Z = np.sin(X * Y)

# пройдёмся циклом по коэффициентам процентов
for proc in [round(x * 0.1, 1) for x in range(16)]:
    # процент шума = i * 100%
    # добавим шум в данные
    Z1 = [Zi + random.uniform(-(((max(Y) - min(Y)) * proc) / 2), (((max(Y) - min(Y)) * proc) / 2)) for Zi in Z]
    data = np.array([X, Y, Z1]).T
    # добавим данные в файл в название укажем процент шума
    with open(f'dataXYZ_{round(proc * 100, 1)}.txt', 'w') as f:
        [print(i, j, z, file=f) for i, j, z in data]
