# импортируем необходимые модули
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def threeD_approx(x, y, z, function):
    # Выполнить подгонку кривой
    popt, pcov = curve_fit(function, (x, y), z)

    # Функция для реализации 3D-графика точек данных и подобранной кривой
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, color='blue')
    x_range = np.linspace(0, 1, 50)
    y_range = np.linspace(0, 1, 50)
    X, Y = np.meshgrid(x_range, y_range)
    Z = func((X, Y), *popt)
    print(X)
    ax.plot_surface(X, Y, Z, color='red', alpha=0.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


# Считаем данные из txt файла
with open('random_dataXYZ.txt') as f:
    a = f.readlines()
    x, y, z = [], [], []
    for i in a:
        a, b, c = i.split()
        x.append(a)
        y.append(b)
        z.append(c)
x = np.array(list(map(float, x)))
y = np.array(list(map(float, y)))
z = np.array(list(map(float, z)))
data = np.array([x, y, z]).T


# Определение математической функции для аппроксимации кривой
def func(xy, a, b, c, d, e, f):
    x, y = xy
    return a + b * x + c * y + d * x ** 2 + e * y ** 2 + f * x * y


threeD_approx(x, y, z, func)
