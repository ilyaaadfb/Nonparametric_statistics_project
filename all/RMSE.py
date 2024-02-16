import math
from nep_2D import nep_regression_2D
from get_points import get_data2D
from approx_2D import approx_2D

def rmse(targets, predictions):
    squared_errors = [(p - t) ** 2 for p, t in zip(predictions, targets)]
    mean_squared_error = sum(squared_errors) / len(predictions)
    rmse = math.sqrt(mean_squared_error)

    return round(rmse, 5)
# print(get_data2D(f'dataXY_{120}.txt')[1])
# print(approx_2D(get_data2D(f'dataXY_{0}.txt')[0], get_data2D(f'dataXY_{0}.txt')[1])[1])


print(
    rmse(get_data2D(f'dataXY_{0}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{0}.txt')[0], get_data2D(f'dataXY_{0}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{10}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{10}.txt')[0], get_data2D(f'dataXY_{10}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{20}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{20}.txt')[0], get_data2D(f'dataXY_{20}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{30}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{30}.txt')[0], get_data2D(f'dataXY_{30}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{40}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{40}.txt')[0], get_data2D(f'dataXY_{40}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{50}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{50}.txt')[0], get_data2D(f'dataXY_{50}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{60}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{60}.txt')[0], get_data2D(f'dataXY_{60}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{70}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{70}.txt')[0], get_data2D(f'dataXY_{70}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{80}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{80}.txt')[0], get_data2D(f'dataXY_{80}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{90}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{90}.txt')[0], get_data2D(f'dataXY_{90}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{100}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{100}.txt')[0], get_data2D(f'dataXY_{100}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{110}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{110}.txt')[0], get_data2D(f'dataXY_{110}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{120}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{120}.txt')[0], get_data2D(f'dataXY_{120}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{130}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{130}.txt')[0], get_data2D(f'dataXY_{130}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{140}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{140}.txt')[0], get_data2D(f'dataXY_{140}.txt')[1])[1]))
print(
    rmse(get_data2D(f'dataXY_{150}.txt')[1],
         nep_regression_2D(get_data2D(f'dataXY_{150}.txt')[0], get_data2D(f'dataXY_{150}.txt')[1])[1]))
