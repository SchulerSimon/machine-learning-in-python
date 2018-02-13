# Author: Simon Schuler

import random

import numpy as np
from numpy import array

import Other.MaschLernen.Draw as draw

def plr(x, y):
    debug = False
    # init
    n = x.shape[0]
    w = array([random.uniform(-1, 1), random.uniform(-1, 1)])
    b = random.uniform(-1, 1)
    r = get_r(x)
    #lernschrittweite
    gamma = 1
    # algo
    k = 1

    while k != 0:
        if debug:
            print("while")
        # abbruchbedingung setzen
        k = 0
        for i in range(0, n):
            if debug:
                print("\ti = ", i)
                print("\ty[i] * (np.dot(w, x[i]) + b) = ",
                      y[i] * (np.dot(w, x[i]) + b))
            if y[i] * (np.dot(w, x[i]) + b) <= 0:
                k += 1
                b = b + gamma * y[i] * (r ** 2)
                w = w + gamma * y[i] * x[i]
                if debug:
                    print("\t\tk = ", k)
                    print("\t\tw = ", w)
                    print("\t\tb = ", b)
    return w, b


"""
Berechnet max_i(||x_i||)
"""
def get_r(x):
    debug = False
    temp = []
    for item in x:
        if debug:
            print("item:", item, " length:", np.linalg.norm(item))
        temp.append(np.linalg.norm(item))

    if debug:
        print("R = ", max(temp))
    return max(temp)


def get_data():
    debug = False
    file = open("PLR.txt", "r")
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
w, b = plr(x, y)

print("Ebene: w = ", w, " b = ", b)

draw.points(x, y)
draw.hesse(w, b)
draw.axis()
draw.show()
