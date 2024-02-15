import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

def nadaraya_watson(x, y, z, query_point, h):
    weights = np.exp(-((x - query_point[0])**2 + (y - query_point[1])**2 + (z - query_point[2])**2) / (2 * h**2))
    weighted_sum = np.sum(weights)
    if weighted_sum == 0:
        return 0
    else:
        return np.sum(weights * z) / weighted_sum

# Пример данных точек в 3D пространстве
x = np.linspace(-10, 10, 100)
y = [random.uniform(-10, 10) for _ in range(100)]
z = np.sin(2 * np.pi * x) * np.cos(2 * np.pi * y)

import math
X = [random.uniform(-10, 10) for _ in range(100)]
Y = [random.uniform(-10, 10) for _ in range(100)]
Z = math.sin(x) * math.cos(y)


# Задаем точку для оценки
query_point = [0.5, 0.5, 0.5]

# Задаем ширину окна h
h = 0.3

# Вычисление оценки Надарая-Ватсона для заданной точки
estimated_z = nadaraya_watson(x, y, z, query_point, h)

print("Оценка Надарая-Ватсона для точки", query_point, ":", estimated_z)

# Отображение точек и оценки на графике
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='b', marker='.')
ax.scatter(query_point[0], query_point[1], estimated_z, c='r', marker='o') # отмечаем оценку красным цветом
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()