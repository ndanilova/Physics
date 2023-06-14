import numpy as np
import matplotlib.pyplot as plt

a = 1.0
b = 0.8
c = 2.0
U = 1.0


def get_V(x):
    V = np.zeros_like(x)

    for i, xi in enumerate(x):
        n = np.floor(xi / c)
        if n * c < xi < n * c + a:
            V[i] = 0
        elif n * c + a < xi < (n + 1) * c:
            V[i] = U

    return V


def get_plot_with_potencial_pits():
    x = np.linspace(-6, 7, 1000)

    V = get_V(x)

    plt.plot(x, V, linewidth=2)
    plt.xlabel(r'$X$')
    plt.ylabel(r'$V(x)$')
    plt.title('Потенциальный рельеф для электрона в кристале (модель Кронига-Пенни)')
    plt.grid(True)
    plt.show()


def get_func(x, P):
    return P * np.sin(x) / x + np.cos(x)


def get_plot_with_cronig_peni(P):
    x = np.linspace(-25, 25, 1000)
    y_plus_one = np.full(shape=len(x), fill_value=1, dtype=np.int64)
    y_minus_one = np.full(shape=len(x), fill_value=-1, dtype=np.int64)
    y = get_func(x, P)
    plt.plot(x, y, label=r'$P = ${}'.format(P), color='r')
    plt.plot(x, y_plus_one, 'k--')
    plt.plot(x, y_minus_one, 'k--')
    plt.fill_between(x, y_plus_one, -1, where=(np.abs(y) < 1), color='yellow')
    plt.xlabel(r'$a \cdot \alpha$')
    plt.ylabel(r'$ \cos(a \cdot \alpha) + P \cdot \frac {\sin(a \cdot \alpha)} {(a \cdot \alpha)}$')
    plt.title('графический анализ уравнения Кронига-Пенни')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    p = int(input())
    get_plot_with_potencial_pits()
    get_plot_with_cronig_peni(p)