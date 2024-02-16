# импортируем необходимые модули
import numpy as np
from scipy.optimize import curve_fit
import plotly.graph_objs as go


def approx_2D(x, y):
    def func(t, A, w, p, c):
        return A * np.sin(w * t + p) + c

    x = np.array(x)
    y = np.array(y)
    popt, _ = curve_fit(func, x, y)
    x_approx = np.linspace(x.min(), x.max(), 100)
    y_approx = func(x, *popt)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='$$Исходные данные$$',
                             marker=dict(color='green')))
    fig.add_trace(go.Scatter(x=x, y=y_approx, name='$$Синусоидальная функция$$',
                             marker=dict(color='blue')))
    fig.add_trace(go.Scatter(x=x, y=func(x, *popt), mode='markers', name='$$Точки аппроксимации$$',
                             marker=dict(color='red', symbol="star-triangle-up")))
    fig.update_layout(xaxis_title="X", yaxis_title="Y")
    fig.show()
