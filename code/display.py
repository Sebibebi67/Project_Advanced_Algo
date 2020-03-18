import matplotlib.pyplot as plt

def display(p):
    p.append(p[0]) #repeat the first point to create a 'closed loop'

    xs = [k.x for k in p]
    ys = [k.y for k in p]

    plt.figure()
    plt.plot(xs,ys) 
    plt.show()

def displayWithCorde(p, c):
    pDisplay = list(p)
    pDisplay.append(p[0]) #repeat the first point to create a 'closed loop'

    xs = [k.x for k in pDisplay]
    ys = [k.y for k in pDisplay]

    plt.figure()
    plt.plot(xs,ys) 

    for k in range(len(c)):
        plt.plot([pDisplay[c[k][0]].x, pDisplay[c[k][1]].x], [pDisplay[c[k][0]].y, pDisplay[c[k][1]].y])

    plt.show() 