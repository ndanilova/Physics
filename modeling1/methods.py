from py_linq import Enumerable
import linq as linq
import pip
import py as py
from scipy import constants
from scipy.optimize import fsolve
import math
import matplotlib.pyplot as plt
import numpy as np


# Some helpfull functions. Nothing to see here.
def distance(x1, x2, y1, y2):
    res = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return res


def intersect(x1, x2, y1, y2, eps):
    if len(x1) != len(y1) or len(x2) != len(y2) or len(x2) != len(x1):
        assert ("len x and len y should be equal")

    points = []
    for i in range(len(x1)):
        dist = distance(x1[i], x2[i], y1[i], y2[i])
        if dist <= eps:
            points.append((x1[i], y1[i], dist))

    points = Enumerable(points)
    min_dist = points.select(lambda x: x[2]).min()
    min_point = points.where(lambda x: x[2] == min_dist).first()
    if min_point is None:
        assert ('No intersection found')

    return (min_point[0], min_point[1])


def print_points_table(points):
    print('\begin{tabular}{| c | c | c |}')
    print('\hline\nn  & x  & y \\')
    for i in range(len(points)):
        print(f'\hline\n{i + 1} & {points[i][0]:.3f}  & {points[i][1]:.3f} \\')
    print('\hline\n\end{tabular}')


def gorgeous_scientific_print(x):
    for i in x:
        print(f'{i:.3e}', end=" ")