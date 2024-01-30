# импортируем необходимые модули
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# создадим функцию для аппроксимации на вход
# которой подаются два массива X и Y
def approx_XY(x, y):
    # Определим математическую функцию, которая
    # будет использоваться для подгонки кривой.
    # В этом примере мы будем использовать
    # синусоидальную функцию.
    def func(t, A, w, p, c):
        return A * np.sin(w * t + p) + c

    x = np.array(list(map(float, x)))
    y = np.array(list(map(float, y)))
    popt, _ = curve_fit(func, x, y)
    x = np.linspace(x.min(), x.max(), 100)
    plt.plot(x, func(x, *popt), color='green',
             label="Синусоидальная функция")
    plt.legend(loc='best')
    plt.scatter(x, y, color='red', s=15)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
