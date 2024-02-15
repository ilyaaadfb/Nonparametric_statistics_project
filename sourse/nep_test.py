import numpy as np


def f_nadaray_watson(x, y, query_x, h):
    weights = np.exp(-0.5 * ((x - query_x) / h) ** 2)  # вычисление весов точек
    numerator = np.sum(weights * y)
    denominator = np.sum(weights)
    return numerator / denominator


query_x = 2
x = np.array([6, 5, 2, 3, 4])
y = np.array([4, 3, 6, 2, 5])
h = 2
print(f_nadaray_watson(x, y, query_x, h))
