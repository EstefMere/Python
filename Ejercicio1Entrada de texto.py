from math import sqrt

a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))
x1 = 0
x2= 0

if((b**2)-(4*a*c)) < 0:

    print("No hay solucion")
else:
    x1 = (-b + sqrt((b**2)-(4*a*c))) /(2*a)
    x2 = (-b - sqrt((b**2)-(4*a*c))) /(2*a)
    print("La solucion es: \nx1 =", x1, "\nx2", x2)
