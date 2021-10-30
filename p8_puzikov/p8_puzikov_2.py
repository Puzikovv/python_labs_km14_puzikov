import math
a = input("ВВедіть a")
b = input("ВВедіть b")
c = input("ВВедіть c")
try:
    a = float(a)
except TypeError:
    print("а не є дійсним числом")

try:
    b = float(b)
except TypeError:
    print("b не є дійсним числом")
try:
    c = float(c)
except TypeError:
    print("c не є дійсним числом")
d = b*b - 4*a*c
try: 
    if d < 0:
        raise ValueError("Дискримінант менше нуля")
    x1 = (-1*b + math.sqrt(d))/(2*a)
    x2 = (-1*b - math.sqrt(d))/(2*a)
    
    print("Корені:", x1, "та", x2)
except ValueError as ve:
    print(ve)
    raise
except ZeroDivisionError:
    print("а не може бути 0")