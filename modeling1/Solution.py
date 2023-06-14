from scipy import constants
from math import*
import matplotlib.pyplot as plt
import numpy as np
# Потенциальная энергия взята как 13.6 эВ -> электрон на первой орбите атома водорода
U = 15.168e-18

# a была вычислена опытным путем
a = 2e-10

def f(U, x, a):
    return -U if (abs(x) < a) else 0

# Определим пси-функцию
def psi(x_0, n):
    # Просто коэффициент, чтобы функции красиво выглядели
    coefficient = 70000000000000000000000
    # И еще немного коэффициентов: делим значения на 2 и сдвигаем на pi * n / 2
    return sqrt(2 / a) * sin(((constants.pi * (n + 1) * (x_0) / a) / 2) + (n + 1) * constants.pi / 2) / coefficient


# График собственных функций осциллографа
def oscillograph_functions(n, x, E):
    points = []
    for index in range(len(x)):
        norm = constants.electron_mass / 150000  # Коэффициент нормализации, чтобы графики получились не огромные
        coefficient = 1 / (sqrt(pow(2, n) * factorial(n))) * pow((alpha / constants.pi), 0.25)
        point = norm * coefficient * exp(-0.5 * alpha * pow(x[index], 2)) * hermite(n, x[
            index]) + E  # + E чтобы поднять график на определенную высоту
        points.append(point)

    return points

# Построим график осцилляторного потенциала
def pot(omega, x_3):
    return 0.5 * constants.electron_mass * pow(omega, 2) * pow(x_3, 2)


# Определим функцию для Эрмитова многочлена
def hermite(n, x):
    array = [0] * (n) + [1]
    hermite = np.polynomial.hermite.Hermite(array)
    return hermite(x * sqrt(alpha))


x_min = -2*a
x_max = 2*a
x = np.arange(x_min, x_max, 1e-12)

y = []

for i in range(len(x)):
    y.append(f(U, x[i], a))

plt.plot(x, y)
plt.xlabel("a", fontsize=14)
plt.ylabel("U", rotation=0, fontsize=14)
plt.grid()
plt.show()

# Максимальное значение k_2 в уравнении Шредингера
# Оно восходит к тому, что аргумент arcsin в следующем блоке должен быть не больше 1
k_max = 1 / constants.hbar * sqrt(2 * constants.electron_mass * U)
print(k_max)
# Графически решим уравнение:
# k_2 * a = pi * n - 2 * arcsin((hbar * k_2)/sqrt(2 * m * U)),
# n = 1, 2, 3...

# Функция прямой (левой части уравнения)
left_func = np.arange(0, k_max, 1e7) * a

# Найдем количество видимых правых частей
# Высота правой части равна pi, значит количество видимых частей будет:
# ceil(k_max * a / pi)
visible_curves = ceil(k_max * a / constants.pi)

# Массив свзяанных значений
# Связанное значение — значение коэффициента k_2 = sqrt(2 * m * E / pow(hbar, 2))
related_values = []

plt.plot(np.arange(0, k_max, 1e7), left_func)

for n in range(1, visible_curves + 1):
    x_1 = []
    y_1 = []
    for k_2 in range(0, int(k_max), int(1e7)):
        x_1.append(k_2)
        right = constants.pi * n - 2 * asin((constants.hbar * k_2) / sqrt(2 * constants.electron_mass * U))
        y_1.append(right)

    plt.plot(x_1, y_1)
    for index in range(len(y_1)):
        value = abs(left_func[index] - y_1[index])
        previous_value_x = related_values[len(related_values) - 1] / 1e7 if len(related_values) > 0 else -1
        previous_value_y = y_1[index - 1] if index > 0 and len(y_1) > 0 else -1
        is_correct_by_x = abs(index - previous_value_x) > 5 if previous_value_x > -1 else True
        is_correct_by_y = abs(y_1[index] - previous_value_y) > 0.5 if previous_value_y > -1 else True

        if (value < 0.004 and (is_correct_by_x or is_correct_by_y)):
            related_values.append(index * 1e7)
            plt.plot(index * 1e7, y_1[index], 'ro')

print(related_values)
plt.xlabel("k", fontsize=14)
plt.ylabel("y", rotation=0, fontsize=14)
plt.grid()
plt.show()
# Вычислим энергии из найденных значений k и отметим их на графике
energies = [0] * len(related_values)

plt.plot(x, y)



for index in range(len(related_values)):
    energies[index] = (constants.hbar ** 2) * related_values[index] ** 2 / (2 * constants.electron_mass)
    plt.axhline(y=energies[index] - U, linestyle="--", c='red', linewidth=0.6)

    # Нарисуем на графике графики волновых функций
    y_psi = []
    for x_i in range(len(x)):
        y_psi.append(psi(x[x_i], index) + (energies[index] - U))

    plt.plot(x, y_psi, c='green')
    print(energies[index])

plt.xlabel("a", fontsize=14)
plt.ylabel("U", rotation=0, fontsize=14)
plt.grid()
plt.show()


x = np.arange(-3e-2, 3e-2, 1e-4)
# x = np.arange(-3, 3, 0.1)
y = []
omega = 1
alpha = constants.electron_mass * omega / constants.hbar

for index in range(len(x)):
    y.append(pot(omega, x[index]))

plt.plot(x, y, linewidth=3)




# Нарисуем линии энергетических уровней
# Собственные значения — значения энергий
own_values = []

n = 0
while True:
    E = (n + 0.5) * constants.hbar * omega

    if (E > y[0]):
        break

    own_values.append(E)

    plt.plot(x, [E] * len(x), linewidth=0.6, c='red')
    plt.plot(x, oscillograph_functions(n, x, E), c='green', linewidth=1)
    n += 1
plt.xlabel("x", fontsize=14)
plt.ylabel("Ψ", rotation=0, fontsize=14)
plt.grid()
plt.show()
print(own_values)