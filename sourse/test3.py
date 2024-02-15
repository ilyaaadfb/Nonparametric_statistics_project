import matplotlib.pyplot as plt


def linear_approximation(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)

    sum_x_squared = sum([xi ** 2 for xi in x])
    sum_xy = sum([xi * yi for xi, yi in zip(x, y)])

    k = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - k * sum_x) / n

    return k, b


def plot_linear_approximation(x, y2, k, b):
    y = []
    for i in x:
        yi = k * i + b
        y.append(yi)
    plt.plot(x, y)
    plt.scatter(x, y2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear Approximation')
    plt.grid(True)
    plt.show()


x = [5, 8, 9, 4, 1, 3]
y2 = [0, 5, 7, 6, 4, 5]
plot_linear_approximation(x, y2, linear_approximation(x, y2)[0], linear_approximation(x, y2)[1])
