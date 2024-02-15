import numpy as np

def nadaraya_watson(x, y, xi, h):
    weights = np.exp(-(xi - x)**2 / (2 * h**2))  # вычисляем веса
    numerator = np.sum(weights * y)  # числитель
    denominator = np.sum(weights)  # знаменатель
    return numerator / denominator  # результат

# Пример использования
x = np.array([1, 2, 3, 4, 5])  # набор исходных данных x
y = np.array([10, 20, 30, 40, 50])  # набор исходных данных y
xi = 3.5  # точка, в которой хотим вычислить прогноз
h = 2  # параметр ширины окна

prediction = nadaraya_watson(x, y, xi, h)
print("Прогноз для точки", xi, ":", prediction)