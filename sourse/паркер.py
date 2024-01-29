import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity

# Создание случайной выборки точе
X = np.concatenate((np.random.normal(0, 1, 100), np.random.normal(5, 1, 100)))[:, np.newaxis]
print(X)
# Создание модели KDE
kde = KernelDensity(kernel='gaussian', bandwidth=0.75).fit(X)

# Определение плотности для новых точек
x = np.linspace(-5, 10, 1000)[:, np.newaxis]
log_dens = kde.score_samples(x)

# Визуализация результатов
plt.fill(x[:, 0], np.exp(log_dens), fc='lightblue')
plt.title('KDE of Random Points')
plt.show()