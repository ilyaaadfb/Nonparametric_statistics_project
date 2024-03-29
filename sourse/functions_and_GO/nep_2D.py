# импортируем необходимые модули
import numpy as np
import matplotlib.pyplot as plt


# создадим функцию, которая будет оценивать значения в определённой точке
def nadaraya_watson(x, y, query_x, h):
    weights = np.exp(-0.5 * ((x - query_x) / h) ** 2)  # вычисление весов точек
    numerator = np.sum(weights * y)  # числитель
    denominator = np.sum(weights)  # знаменатель
    return numerator / denominator  # оценка значения в заданной точке


# создадим функцию, которая будет реализовывать непараметрическую регрессию,
# на вход принимаются два массива X и Y
def nep_regression_2D(x, y):
    x = np.array(list(map(float, x)))
    y = np.array(list(map(float, y)))
    # Задаем точки, в которых хотим получить оценку
    query_x = np.array([i for i in x])

    # Задаем ширину окна h (ширина окна на одну сторону)
    h = 0.5

    # Вычисляем оценки значений в заданных точках
    query_y = [nadaraya_watson(x, y, q, h) for q in query_x]

    # График
    plt.scatter(x, y, label='Исходные данные')
    plt.plot(query_x, query_y, label='Оценка Надарая-Ватсона', color='blue')
    plt.legend()
    plt.show()


