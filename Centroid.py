import numpy as np
from numpy import array
from matplotlib import pyplot as plt

import Other.MaschLernen.Draw as draw


def centroid(x_p, x_n):
    m_p = middle_vector(x_p)
    m_n = middle_vector(x_n)

    draw.point(m_p, "go")
    draw.point(m_n, "go")

    w = m_p - m_n
    b = (np.linalg.norm(m_n)**2 - np.linalg.norm(m_p)**2) / 2
    return w, b


def middle_vector(x):
    debug = False
    if debug:
        print(x)
    n = x.shape[0]
    sum = np.zeros(x.shape[1])
    for item in x:
        if debug:
            print("sum", sum, "item", item)
        sum += item
    return array(sum / n)


def get_data():
    debug = False
    file = open("Centroid.txt", "r")
    x1 = []
    y1 = []
    for line in file:
        if debug:
            print(line)
        split = line.split(" ")
        x1.append([float(split[0]), float(split[1])])
        y1.append(float(split[2]))
        if debug:
            print(x1, y1)
    file.close()

    return array(x1), array(y1)


x, y = get_data()

lower = []
upper = []

n = x.shape[0]
for i in range(n):
    if y[i] < 0:
        lower.append(x[i])
    else:
        upper.append(x[i])

w, b = centroid(array(upper), array(lower))

print("Ebene: w = ", w, " b = ", b)

draw.points(x, y)
draw.hesse(w, b)
draw.axis()
draw.show()
