# импортируем необходимые модули
import numpy as np
import matplotlib.pyplot as plt

import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import math

def my_nadaraya_watson(X, Z, x_query, h):
    weights = np.exp(-np.sum((X - x_query) ** 2, axis=1) / (2 * h ** 2))
    weighted_sum = np.sum(weights * Z)
    sum_of_weights = np.sum(weights)
    return weighted_sum / sum_of_weights

def my_phi(p):
    if p ** 2 <= 5:
        return 0.335 - 0.067 * p ** 2
    else:
        return 0

def my_f_nadaray_watson(z_dop, x_pi_list, y_pi_list, c):
    numerator = 0
    denominator = 0
    for i in range(len(x_pi_list)):
        phi_value = my_phi((z_dop - x_pi_list[i]) / c)
        numerator += y_pi_list[i] * phi_value
        denominator += phi_value
    return numerator / denominator


X = np.array([[2], [3], [5]])
print(X)
Y = np.array([0.1, 0.2, 0.3])
print(Y)
z_query = np.array([4])

h = 1

result = my_nadaraya_watson(X, Y, z_query, h)
print(result)

z_dop = 4
x_pi_list = [2, 3, 5]
y_pi_list = [0.1, 0.2, 0.3]
c = 1

result = my_f_nadaray_watson(z_dop, x_pi_list, y_pi_list, c)
print(result)