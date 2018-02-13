"""
This is my own collection for drawing things
"""
import matplotlib.lines as mlines
from matplotlib import pyplot as plt
from numpy import array


def newline(p1, p2):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if (p2[0] == p1[0]):
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1] + (p2[1] - p1[1]) / (p2[0] - p1[0]) * (xmax - p1[0])
        ymin = p1[1] + (p2[1] - p1[1]) / (p2[0] - p1[0]) * (xmin - p1[0])

    l = mlines.Line2D([xmin, xmax], [ymin, ymax])
    ax.add_line(l)
    return l


def axis():
    x_axis = array([1, 0])
    y_axis = array([0, 1])
    zero = array([0, 0])
    newline(zero, x_axis)
    newline(zero, y_axis)


def points(x, y):
    n = x.shape[0]
    for i in range(0, n):
        if y[i] <= 0:
            plt.plot(x[i][0], x[i][1], "bo")
        else:
            plt.plot(x[i][0], x[i][1], "ro")


def points_tuples(t):
    for (x, y) in t:
        plt.plot(x, y, "ro")


def show():
    plt.show()


def hesse(w, b):
    x0 = -b / w[1]
    y0 = -b / w[0]

    p1 = array([0, x0])
    p2 = array([y0, 0])
    newline(p1, p2)


def point(x, color):
    plt.plot(x[1], x[0], color)
