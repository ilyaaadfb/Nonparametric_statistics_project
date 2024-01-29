import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt

# Генерируем случайные данные в трехмерном пространстве
with open('random_dataXYZ.txt') as f:
    a = f.readlines()
    x, y, z = [], [], []
    for i in a:
        a, b, c = i.split()
        x.append(a)
        y.append(b)
        z.append(c)
x = np.array(list(map(float, x)))
y = np.array(list(map(float, y)))
z = np.array(list(map(float, z)))
X_train = np.array([x, y, z]).T * 10

y_train = np.sin(X_train[:, 0]) + np.cos(X_train[:, 1]) + np.exp(X_train[:, 2])  # Выходные значения
print(X_train)
# Создаем экземпляр модели KNN регрессии
knn_regressor = KNeighborsRegressor(n_neighbors=5)

# Обучаем модель на тренировочных данных
knn_regressor.fit(X_train, y_train)

# Генерируем тестовые данные для предсказания
X_test = np.random.rand(20, 3) * 10  # Тестовые входные признаки

# Предсказываем значения для тестовых данных
y_pred = knn_regressor.predict(X_test)

# Визуализация результатов
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Визуализируем тренировочные данные
ax.scatter(X_train[:, 0], X_train[:, 1], X_train[:, 2], c='b', marker='o', label='Training Data')

# Визуализируем тестовые данные и их предсказания
ax.scatter(X_test[:, 0], X_test[:, 1], X_test[:, 2], c='r', marker='^', label='Test Data')
ax.scatter(X_test[:, 0], X_test[:, 1], X_test[:, 2], c=y_pred, cmap='viridis', marker='x', label='Predictions')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.plot_trisurf(X_test[:, 0], X_test[:, 1], X_test[:, 2], color='purple', alpha=0.6)
ax.legend()
plt.show()