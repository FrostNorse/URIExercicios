import math
a, b, c = map(float, input().split())
if a != 0:
    delta = b * b - (4 * a *c)
    if delta < 0:
        print("Impossivel calcular")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("R1 = %.5F" % x1)
        print("R2 = %.5F" % x2)
else:
    print("Impossivel calcular")
