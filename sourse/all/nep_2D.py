# импортируем необходимые модули
import numpy as np
from Nad_Wat import nonparametric
import plotly.graph_objs as go

# создадим функцию, которая будет реализовывать непараметрическую регрессию,
# на вход принимаются два массива X и Y
def nep_regression_2D(x, y):
    c = 0.3
    x_lst = []
    y_lst = []
    print(min(x), max(x))
    # Вычисляем оценки значений в заданных точках
    for x_dop in np.arange(min(x), max(x), 0.1):
        y_dop = nonparametric(x_dop, c, x, y)
        x_lst.append(x_dop)
        y_lst.append(y_dop)

    # График
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='$$Исходные данные$$',
                             marker=dict(color='green')))
    fig.add_trace(go.Scatter(x=x_lst, y=y_lst, name='$$Непараметрическая регрессия$$',
                              marker=dict(color='blue')))
    fig.add_trace(go.Scatter(x=x_lst, y=y_lst, mode='markers', name='$$Точки непараметрической регрессии$$',
                             marker=dict(color='red', symbol="star-triangle-up")))
    fig.update_layout(xaxis_title="X", yaxis_title="Y")
    fig.show()
