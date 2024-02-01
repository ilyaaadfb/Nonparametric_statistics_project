# импортируем необходимые модули
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# создадим функцию для аппроксимации на вход которой
# подаются три массива X и Y и Z
def approx_3D(x, y, z):
    x = np.array(list(map(float, x)))
    y = np.array(list(map(float, y)))
    z = np.array(list(map(float, z)))
    # Определение математической функции для
    # аппроксимации кривой
    def func(xy, a):
        x, y = xy
        return a*np.sin(x)
    # Выполнить подгонку кривой
    popt, pcov = curve_fit(func, (x, y), z)
    # Функция для реализации 3D-графика точек данных
    # и подобранной кривой
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, color='blue')
    x_range = np.linspace(-10, 10, 50)
    y_range = np.linspace(-10, 10, 50)
    X, Y = np.meshgrid(x_range, y_range)
    Z = func((X, Y), *popt)
    ax.plot_surface(X, Y, Z, color='red', alpha=0.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
















