import matplotlib.pyplot as pt
"""Oscillations of an Object on a Spring with drag, Feynmann-Newton"""
m = 1
k = 1
c = 0.1

def solver(f, V0, X0, h, T):
    t = [0.0]
    a = []
    v = [V0 + f(V0, X0) * h]
    x = [X0]
    while t[-1] <= T:
        a.append(f(v[-1], x[-1]))
        v.append(v[-1] + a[-1] * h)
        x.append(x[-1] + v[-1] * h)
        t.append(t[-1] + h)
    return [t, a, v, x]

def spring(V, X):
    return - k / m * X - c / m * V

lst = solver(spring, 0, 1, 0.001, 50)

pt.plot(lst[3], lst[2], 'k,')
pt.show('ICP2.4')