# импортируем необходимые модули
import numpy as np


def get_data2D(name_file):
    with open(name_file) as f:
        a = f.readlines()
        x, y = [], []
        for i in a:
            a, b = i.split()
            x.append(a)
            y.append(b)
        return x, y


# get_data2D(name_file)[0] - X
# get_data2D(name_file)[1] - Y


def get_data3D(name_file):
    with open(name_file) as f:
        a = f.readlines()
        x, y, z = [], [], []
        for i in a:
            a, b, c = i.split()
            x.append(float(a))
            y.append(float(b))
            z.append(float(c))

        return x, y, z

print(get_data3D('dataXYZ_with_hindrance.txt')[0])
# get_data3D(name_file)[0] - X
# get_data3D(name_file)[1] - Y
# get_data3D(name_file)[2] - Z
