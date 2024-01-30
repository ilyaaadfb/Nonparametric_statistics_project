import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt

def nep_regres_3D(x, y, z):
    X_train = np.random.rand(20, 3) * 10  # Тестовые входные признаки

    y_train = np.sin(X_train[:, 0]) + np.cos(X_train[:, 1]) + np.exp(X_train[:, 2])  # Выходные значения
    print(X_train)
    # Создаем экземпляр модели KNN регрессии
    knn_regressor = KNeighborsRegressor(n_neighbors=5)

    # Обучаем модель на тренировочных данных
    knn_regressor.fit(X_train, y_train)

    # Данные для предсказания
    x = np.array(list(map(float, x)))
    y = np.array(list(map(float, y)))
    z = np.array(list(map(float, z)))
    X_test = np.array([x, y, z]).T

    # Предсказываем значения для данных
    y_pred = knn_regressor.predict(X_test)

    # Визуализация результатов
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, color='red')

    # Визуализируем тренировочные данные
    # ax.scatter(X_train[:, 0], X_train[:, 1], X_train[:, 2], c='b', marker='o', label='Training Data')

    # Визуализируем данные и их предсказания
    ax.scatter(x, y, z, c='r', marker='^', label='Test Data')
    ax.scatter(x, y, z, c=y_pred, cmap='viridis', marker='x', label='Predictions')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.plot_trisurf(x, y, z, color='purple', alpha=0.6)
    ax.legend()
    plt.show()