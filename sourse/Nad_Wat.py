# колоколообразная функция
def phi(p):
    if p ** 2 <= 5:
        return 0.335 - 0.067 * p ** 2
    else:
        return 0

# функция для вычисления значения по формуле Надарая-Ватсона
def f_nadaray_watson(x_dop, x_pi_list, y_pi_list, c):
    numerator = 0
    denominator = 0

    for i in range(len(x_pi_list)):  # вычисление весов точек
        phi_value = phi((x_dop - x_pi_list[i]) / c)
        numerator += y_pi_list[i] * phi_value
        denominator += phi_value

    return numerator / denominator  # оценка значения в заданной точке



