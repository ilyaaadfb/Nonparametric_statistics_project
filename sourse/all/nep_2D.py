# импортируем необходимые модули
import numpy as np
from Nad_Wat import f_nadaray_watson
import plotly.graph_objs as go
from RMSE import rmse


# создадим функцию, которая будет реализовывать непараметрическую регрессию,
# на вход принимаются два массива X и Y
def nep_regression_2D(x, y):
    x = np.array(list(map(float, x)))
    y = np.array(list(map(float, y)))

    c = 0.5
    # Вычисляем оценки значений в заданных точках
    query_y = [f_nadaray_watson(q, x, y, c) for q in x]

    # График
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='$$Исходные данные$$',
                             marker=dict(color='green')))
    fig.add_trace(go.Scatter(x=x, y=query_y, name='$$Оценка Надарая-Ватсона$$',
                             marker=dict(color='blue')))
    fig.add_trace(go.Scatter(x=x, y=query_y, mode='markers', name='$$Точки аппроксимации$$',
                             marker=dict(color='red', symbol="star-triangle-up")))
    fig.update_layout(xaxis_title="X", yaxis_title="Y")
    fig.show()
