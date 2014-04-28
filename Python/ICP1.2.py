import math
import matplotlib.pyplot as pt

def algo1(m = 1, r = 1, v = 0, h = 0.01, g = 9.8, t = 15, p = 1):
    """ algorith for finding the spped position and acceleration of a falling object sphere
        using a = g - 1/2 C rho pi r^2 / m * v^2"""
    tlst = []
    alst =[]
    vlst = []
    i = 0.0
    P = 0
    C = 0.46
    D = math.pi * r ** 3 / 3 * 4 / m
    while i <= t:
        a = g - 0.5 * C * D * math.pi * r **2 / m * v **2
        if P % p == 0:
            tlst.append(i)
            alst.append(a)
            vlst.append(v)    
        v = v + a * h
        i = i + h
        P = P + 1
    return [tlst, alst, vlst]

lst = algo1(r = 0.5, m= 12)
t = lst[0]
a = lst[1]
v = lst[2]

pt.plot(t, v, t, a)
pt.show( 'falling.pdf' )