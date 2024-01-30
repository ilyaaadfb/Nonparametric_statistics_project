from approx_2D import approx_XY
from approx_3D import approx_3D
from nep_2D import nep_regression_2D
from nep_3D import nep_regres_3D
from get_points import get_data2D, get_data3D

# get_data2D(name_file)[0] - X
# get_data2D(name_file)[1] - Y

# get_data3D(name_file)[0] - X
# get_data3D(name_file)[1] - Y
# get_data3D(name_file)[2] - Z

name_file = 'dataXYZ.txt'
x = get_data3D(name_file)[0]
y = get_data3D(name_file)[1]
z = get_data3D(name_file)[2]
approx_3D(x, y, z)
