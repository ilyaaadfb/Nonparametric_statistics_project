# колоколообразная функция
def phi(p):
    if p ** 2 <= 5:
        return 0.335 - 0.067 * p ** 2
    else:
        return 0

def z_nadaray_watson(x_dop, y_dop, z_dop, x_pi_list, y_pi_list, z_pi_list, c):
    numerator = 0
    denominator = 0

    for i in range(len(x_pi_list)):
        phi_value = phi(
            ((x_dop - x_pi_list[i]) ** 2 + (y_dop - y_pi_list[i]) ** 2 + (z_dop - z_pi_list[i]) ** 2) ** 0.5 / c)
        numerator += z_pi_list[i] * phi_value
        denominator += phi_value

    return numerator / denominator

x_dop = 4
y_dop = 2
z_dop = 3
x_pi_list = [4, 5, 6]
y_pi_list = [7, 8, 9]
z_pi_list = [10, 11, 12]
c = 2

result = z_nadaray_watson(x_dop, y_dop, z_dop, x_pi_list, y_pi_list, z_pi_list, c)
print(result)
