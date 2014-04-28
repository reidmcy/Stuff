import math
import matplotlib.pyplot as pt

F = 2
O = 2.4
J = 0.1
m = 1
A = 0.25
B = 0.5

def solver(f, X0, V0, h, T):
    t = [0.0]
    a = []
    v = [V0]
    x = [X0]
    while t[-1] <= T:
        a.append(f(v[-1], x[-1], t[-1]))
        v.append(v[-1] + a[-1] * h)
        x.append(x[-1] + v[-1] * h)
        t.append(t[-1] + h)
        print t[-1]
    return [t, a, v, x]

def equation(V, X, T):
    return - J*V/m + 2*A*X/m - 4*B/m*X**3 + F*math.cos(O*T)/m

lst = solver(equation, 0.5, 0.0, 0.00001, 10)

pt.plot(lst[0], lst[3], 'k,')
pt.axis('tight')
pt.legend( )
pt.grid('on')
pt.show( 'Problem1-1')
pt.savefig('Problem 1-1.pdf')
print equation(0, 0.5, 0)