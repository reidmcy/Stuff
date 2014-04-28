import math

def algo1(m = 1, r = 1, v = 0, h = 0.01, g = 9.8, t = 15, p = 1):
    """ algorith for finding the spped position and acceleration of a falling object sphere
        using a = g - 1/2 C rho pi r^2 / m * v^2"""
    print "Time     Acceleration    Velocity"
    print " (s)        (m/s^2)         (m/s)"
    i = 0.0
    P = 0
    C = 0.46
    D = math.pi * r ** 3 / 3 * 4 / m
    while i <= t:
        a = g - 0.5 * C * D * math.pi * r **2 / m * v **2
        if P % p == 0:
            print " " + str(round(i , 4)) + "         " + str(round(a , 4)) + "         " + str(round(v, 4))
        v = v + a * h
        i = i + h
        P = P + 1
        
algo1(r = 0.0075, m = 0.0039)
algo1(r = 0.0075, m = 0.0039, p = 10)