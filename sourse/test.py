import math

def y_dop(x_dop, x_list, y_list, c):
    sum_num = 0
    sum_den = 0

    for i in range(len(x_list)):
        distance = (x_dop - x_list[i]) / c
        phi = math.exp(-distance**2)
        sum_num += y_list[i] * phi
        sum_den += phi

    return sum_num / sum_den


x_list = [1, 2, 3, 4, 5]
y_list = [10, 20, 30, 40, 50]
c = 2

x_dop = 3.5
result = y_dop(x_dop, x_list, y_list, c)

print(result)  # Вывод: 35.64231826068233



# импортируем необходимые модули
import numpy as np
import matplotlib.pyplot as plt


# создадим функцию, которая будет оценивать значения в определённой точке
def f_nadaray_watson(x, y, query_x, h):
    weights = np.exp(-0.5 * ((x - query_x) / h) ** 2)  # вычисление весов точек
    numerator = np.sum(weights * y)
    denominator = np.sum(weights)
    return numerator / denominator  # оценка значения в заданной точке


# создадим функцию, которая будет реализовывать непараметрическую регрессию,
# на вход принимаются два массива X и Y
def nep_regression_2D(x, y):
    x = np.array(list(map(float, x)))
    y = np.array(list(map(float, y)))
    # Задаем точки, в которых хотим получить оценку
    query_x = np.array([i for i in x])


    # Вычисляем оценки значений в заданных точках
    query_y = [f_nadaray_watson(x, y, q, 0.5) for q in query_x]

    # График
    plt.scatter(x, y, label='Исходные данные')
    plt.plot(query_x, query_y, label='Оценка Надарая-Ватсона', color='blue')
    plt.legend()
    plt.show()