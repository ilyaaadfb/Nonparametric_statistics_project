# импортируем необходимые модули
import numpy as np
from scipy.optimize import curve_fit
import plotly.graph_objs as go


def approx_3D(x, y, z):
    def func(xy, a):
        x, y = xy
        return a * np.sin(x)
    popt, pcov = curve_fit(func, (np.array(list(x)), np.array(list(y))), np.array(list(z)))
    x_range = np.linspace(-10, 10, 100)
    y_range = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x_range, y_range)
    Z = func((X, Y), *popt)
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color='blue', size=2)))
    fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale='Reds', opacity=0.5))
    fig.update_layout(scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ))
    fig.show()
