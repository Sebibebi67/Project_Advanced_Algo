import matplotlib.pyplot as plt

def display(p):
    p.append(p[0]) #repeat the first point to create a 'closed loop'

    xs = [k.x for k in p]
    ys = [k.y for k in p]

    plt.figure()
    plt.plot(xs,ys) 
    plt.show()

def displayWithCorde(p, c):
    p.append(p[0]) #repeat the first point to create a 'closed loop'

    xs = [k.x for k in p]
    ys = [k.y for k in p]

    plt.figure()
    plt.plot(xs,ys) 

    for k in range(len(c)):
        plt.plot([p[c[k][0]].x, p[c[k][1]].x], [p[c[k][0]].y, p[c[k][1]].y])

    plt.show() 