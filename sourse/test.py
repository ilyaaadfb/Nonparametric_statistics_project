# импортируем необходимые модули
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# создадим функцию для аппроксимации на вход которой подаются два массива X и Y
def approx(x, y, function):
    popt, _ = curve_fit(function, x, y)
    x = np.linspace(x.min(), x.max(), 100)
    plt.plot(x, func(x, *popt), color='green', label="Полиномиальная функция степени 3")
    plt.legend(loc='best')
    plt.scatter(x, y, color='red', s=15)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


with open('dataXY.txt') as f:
    a = f.readlines()
    x, y = [], []
    for i in a:
        a, b = i.split()
        x.append(a)
        y.append(b)


x = np.array(list(map(float, x)))
y = np.array(list(map(float, y)))


# Определим математическую функцию, которая будет использоваться для подгонки кривой.
# В этом примере мы будем использовать простую полиномиальную функцию степени 3.
def func(t, A, w, p, c):
    return A * np.sin(w*t + p) + c
#
#
# def func(x, a, b):
#     return a * np.exp(b ** x)

#
# def func(x, a, b):
#     return b + a * np.log(x)


approx(x, y, func)

with open('dataXY.txt') as f:
    a = f.readlines()
    x, y = [], []
    for i in a:
        a, b = i.split()
        x.append(a)
        y.append(b)
