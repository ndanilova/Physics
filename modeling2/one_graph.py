import numpy as np
import matplotlib.pyplot as plt

p_current = 10
p_min = 0
p_max = 100

value = 10
# Левая граница графика
start = -np.sqrt(value)
# Правая граница графика
end = np.sqrt(value)

# Значения x для графика
values = np.arange(start, end, 0.001)


def f(alpha, a, P):
    return np.cos(alpha * a) + P * np.sin(alpha * a) / (alpha * a)


# Вычисление половины значений функции энергетических зон
def calc_graph(P, isLeft):
    multiplier = -1 if isLeft else 1
    return plt.plot(values * (multiplier * values), f(values, values, P), color='C0', linewidth=2)


# Вычисление всех значений функции энергетических зон
def calc_whole_graph(P):
    left_part, = calc_graph(P, False)
    right_part, = calc_graph(P, True)
    return [left_part, right_part]


# Вычисление половины значений поддерживающих линий.
# Они, в отличие от полос, могут принимать значения -1, 0, 1
# И служат лишь для большей наглядности
def calc_support_lines(P, is_left):
    multiplier = -1 if is_left else 1
    return plt.plot(values * (multiplier * values),
                    [-1 if f(i, i, P) < -1 else 1 if f(i, i, P) > 1 else 0 for i in values], color='black', linewidth=1)


# Вычисление всех значений поддерживающих линий
def calc_whole_support_lines(P):
    leftPart, = calc_support_lines(P, True)
    rightPart, = calc_support_lines(P, False)
    return [leftPart, rightPart]


# Вычисление половины разрешенных (полосы) и запрещенных (впадины) значений
def calc_bars(P, is_left):
    multiplier = -1 if is_left else 1
    return plt.plot(values * (multiplier * values), [1 if abs(f(i, i, P)) < 1 else 0 for i in values], color='red',
                    linewidth=1)


# Вычисление всех значений полос и впадин
def calc_whole_bars(P):
    left_part, = calc_bars(P, False)
    right_part, = calc_bars(P, True)
    return [left_part, right_part]


fig, ax = plt.subplots()

ax.set_xlabel('αa')
ax.set_ylabel('f(α, a)')

plt.axhline(y=1, linestyle="--", c='green', linewidth=1)
plt.axhline(y=-1, linestyle="--", c='green', linewidth=1)

lines = [calc_whole_graph(p_current), calc_whole_support_lines(p_current), calc_whole_bars(p_current)]

plt.text(11, 10.5, "Процент запрещенных зон:", horizontalalignment='right', verticalalignment='top')
barsValues = [1 if abs(f(i, i, p_current)) < 1 else 0 for i in values]
percent = plt.text(11, 10, f"{barsValues.count(0) / len(barsValues) * 100 : .2f}" + "%", horizontalalignment='right',
                   verticalalignment='top')

plt.subplots_adjust(left=0.25)

plt.show()
