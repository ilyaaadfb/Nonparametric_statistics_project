from nep_3D import nep_regression_3D
from get_points import get_data3D

# get_data3D(name_file)[0] - X
# get_data3D(name_file)[1] - Y
# get_data3D(name_file)[2] - Z

name_file = 'random_dataXYZ.txt'
# name_file = 'dataXYZ.txt'
# name_file = 'dataXYZ_with_hindrance.txt'
x = get_data3D(name_file)[0]
y = get_data3D(name_file)[1]
z = get_data3D(name_file)[2]
nep_regression_3D(x, y, z)
