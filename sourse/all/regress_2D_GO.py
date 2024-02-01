from nep_2D import nep_regression_2D
from get_points import get_data2D

# get_data2D(name_file)[0] - X
# get_data2D(name_file)[1] - Y

name_file = 'random_dataXY.txt'
# name_file = 'dataXY.txt'
# name_file = 'dataXY_with_hindrance.txt'
x = get_data2D(name_file)[0]
y = get_data2D(name_file)[1]
nep_regression_2D(x, y)





