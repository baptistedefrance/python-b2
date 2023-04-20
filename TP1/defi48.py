import math
r = 0.5
theta = 0.0
while theta <= 4 * math.pi:
    x = round(math.cos(theta) * r, 5)
    y = round(math.sin(theta) * r, 5)
    f = open('spirale.txt','a')
    f.write(str(x) + " " + str(y)+"\n")
    f.close()
    print("Coordonnées cartésiennes: ({}, {})".format(x, y))
    r += 0.1
    theta += 0.1
