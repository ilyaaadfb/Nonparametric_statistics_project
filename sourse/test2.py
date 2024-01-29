# импортируем необходимые модули
import numpy as np

# генерация 100 случайных чисел
x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)
data = np.array([x, y, z]).T
# запись данных в файл
with open('random_dataXYZ.txt', 'w') as f:
    for i, j, t in data:
        print(i, j, t, file=f)




# импортируем необходимые модули
import numpy as np

# генерация 100 случайных чисел
x = np.random.random(100)
y = np.random.random(100)
z = np.sin(x * y)
data = np.array([x, y, z]).T
# добавим шум в данные
z2 = np.sin(x) + np.random.normal(0, 0.1, size=100)
data = np.array([x, y, z]).T
# запись данных в файл
with open('dataXYZ.txt', 'w') as f:
    for i, j, z in data:
        print(i, j, z, file=f)

# запись данных с шумом в файл
with open('dataXYZ_with_hindrance.txt', 'w') as f:
    for i, j, z in data:
        print(i, j, z, file=f)




