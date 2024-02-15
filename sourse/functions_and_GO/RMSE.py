import math


def rmse(predictions, targets):
    squared_errors = [(p - t) ** 2 for p, t in zip(predictions, targets)]
    mean_squared_error = sum(squared_errors) / len(predictions)
    rmse = math.sqrt(mean_squared_error)

    return rmse


predictions = [3, 4, 5, 6]
targets = [2, 4, 6, 8]

print(rmse(predictions, targets))
