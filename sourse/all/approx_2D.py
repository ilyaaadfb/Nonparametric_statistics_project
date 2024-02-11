# импортируем необходимые модули
import numpy as np
from scipy.optimize import curve_fit
import plotly.graph_objs as go
from RMSE import rmse


# создадим функцию для аппроксимации на вход
# которой подаются два массива x и y
def approx_2D(x, y):
    # Определим математическую функцию, которая
    # будет использоваться для подгонки кривой.
    # В этом примере мы будем использовать
    # синусоидальную функцию.
    def func(t, A, w, p, c):
        return A * np.sin(w * t + p) + c

    x = np.array(list(map(float, x)))
    y = np.array(list(map(float, y)))
    popt, _ = curve_fit(func, x, y)
    x = np.linspace(x.min(), x.max(), 100)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='$$Исходные данные$$',
                             marker=dict(color='green')))
    fig.add_trace(go.Scatter(x=x, y=func(x, *popt), name='$$Синусоидальная функция$$',
                             marker=dict(color='blue')))
    fig.add_trace(go.Scatter(x=x, y=func(x, *popt), mode='markers', name='$$Точки аппроксимации$$',
                             marker=dict(color='red', symbol="star-triangle-up")))
    fig.update_layout(xaxis_title="X", yaxis_title="Y")
    fig.show()
