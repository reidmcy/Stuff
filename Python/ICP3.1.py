import matplotlib.pyplot as pt 
"""Police verus Speeder"""
PX = 0
PV = 0
PA = 6
SX = 0
SV = 100.0 * 10000.0 / 36000.0
SA = 0

def solver(AP, VP, XP, AS, VS, XS, h):
    vp = [VP + AP * h / 2]
    vs = [VS]
    xp = [XP]
    xs = [XS]
    t = [0.0]
    passed = False
    while not passed:
        vp.append(vp[-1] + AP * h)
        vs.append(VS)
        xp.append(xp[-1] + vp[-1] * h)
        xs.append(xs[-1] + vs[-1] * h)
        t.append(t[-1] + h)
        if xp[-1] >= xs[-1]:
            passed = True
    return [t, vp, vs, xp, xs]
lst = solver(PA, PV, PX, SA, SV, SX, 0.01)
print lst[0][-1]
print lst[4][-1]


pt.plot(lst[0], lst[3], lst[0], lst[4])
pt.show()
