import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
D = b*b - 4*a*c  
if D > 0:
    r1 = (-b + math.sqrt(D)) / (2*a)
    r2 = (-b - math.sqrt(D)) / (2*a)
    print("Two real roots:", r1, r2)

elif D == 0:
    r = -b / (2*a)
    print("One real root:", r)

else:
    print("No real roots (discriminant < 0)")