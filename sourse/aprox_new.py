import matplotlib.pyplot as plt
import numpy as np
import random
# Заданные данные
X = [random.randint(-10, 10) for _ in range(100)]
Y = [np.sin(Yi) for Yi in X]

# Определение нелинейной функции для аппроксимации
def nonlinear_func(t, A, w, p, c):
    return A * np.sin(w * t + p) + c


# Определение функции подгонки
def fitting_func(params):
    a, b = params
    return sum((nonlinear_func(x, a, b) - y) ** 2 for x, y in zip(X, Y))


# Нахождение оптимальных параметров
from scipy.optimize import minimize

result = minimize(fitting_func, [1, 1])  # Начальные значения параметров
a_opt, b_opt = result.x

# Вывод результатов
print("Оптимальные значения параметров:")
print("a =", a_opt)
print("b =", b_opt)

# Генерация точек для построения графика аппроксимации
X_fit = [x // 10 for x in range(10 * min(X), 10 * max(X))]
Y_fit = [nonlinear_func(x, a_opt, b_opt) for x in X_fit]

# Построение графика
plt.plot(X, Y, 'bo', label='Данные')
plt.plot(X_fit, Y_fit, 'r-', label='Аппроксимация')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Нелинейная аппроксимация')
plt.legend()
plt.show()
