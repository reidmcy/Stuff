import math
import matplotlib.pyplot as pt

g = 9.8
C = 0.46
rho = 1.2
r = 0.03
m = 0.005

def sfind(f, V0, X0, h, T):
    x = [X0]
    v = [V0]
    a = [None]
    n = 1
    t = [0]
    while t[-1] <= T:
        a.append(f(v[-1], x[-1]))
        v.append(v[n-1] + a[n] * h)
        x.append(x[n-1] + v[n] * h)
        t.append(t[-1] + h)
        n = n + 1
    return [t, a[0:], v, x]
def falldrag(V, X):
    return g - 0.5 * C * rho * math.pi * r ** 2 / m * V ** 2

lst = sfind(falldrag, 0, 0, 0.01, 10)

pt.plot(lst[0], lst[3], lst[0], lst[2], lst[0], lst[1])
pt.legend(['x', 'v', 'a'], loc=0)
pt.show('stuff')