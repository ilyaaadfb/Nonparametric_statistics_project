# импортируем необходимые модули
import numpy as np


# колоколообразная ядерная функция
def bell_shaped_kernel_parabola(p):
    if p ** 2 <= 5: return 0.335 - 0.067 * p ** 2
    return 0


# функция для вычисления модельного y
def nonparametric_for_e(x_dop, c, x, y):
    s1, s2 = 0, 0
    for i in range(len(y)):
        mu = 1 if x_dop != x[i] else 0
        s1 += y[i] * bell_shaped_kernel_parabola((x_dop - x[i]) / c) * mu
        s2 += bell_shaped_kernel_parabola((x_dop - x[i]) / c) * mu
    if s2 != 0: return s1 / s2
    return 0


# функция для вычисления ошибки
def E(x, y, c):
    e = 0
    for i in range(len(x)):
        ym = nonparametric_for_e(x[i], c, x, y)
        e += (y[i] - ym) ** 2
    return (e / len(x)) ** 0.5


# функция реализующая формулу Надарая-Ватсона
def nonparametric(x_dop, c, xi_list, yi_list):
    numerator, denominator = 0, 0

    for i in range(len(xi_list)):  # вычисление весов точек
        phi_value = bell_shaped_kernel_parabola((x_dop - xi_list[i]) / c)
        numerator += yi_list[i] * phi_value
        denominator += phi_value
    if denominator != 0: return numerator / denominator  # оценка значения в заданной точке
    return 0


# функция выполняющая непараметричскую регрессию
def nep_regression_2D(x, y):
    c_best, e_best = None, None
    for c in np.arange(0.001, 5, 0.01):
        e = E(x, y, c)
        if e_best is None or e < e_best:
            e_best, c_best = e, c
    x_nep, y_nep = [], []
    # Вычисляем оценки значений в заданных точках
    for x_dop in np.arange(min(x), max(x), 0.1):
        y_dop = nonparametric(x_dop, c_best, x, y)
        x_nep.append(x_dop)
        y_nep.append(y_dop)
    return x_nep, y_nep
