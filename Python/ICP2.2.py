import math
import matplotlib.pyplot as pt
"""Oscillations of an simple pendulum"""
g = 1
L = 1

def solver(f, V0, theta, h, T):
    t = [0.0]
    a = []
    v = [V0]
    x = [theta]
    while t[-1] <= T:
        a.append(f(v[-1], x[-1]))
        v.append(v[-1] + a[-1] * h)
        x.append(x[-1] + v[-1] * h)
        t.append(t[-1] + h)
    return [t, a, v, x]

def pendulum(V, theta):
    return - g / L * math.sin(theta)

lst = solver(pendulum, 0, 1, 0.01, 12)

pt.plot(lst[0], lst[3], '.')
pt.show('ICP2.2')