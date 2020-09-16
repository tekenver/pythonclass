#Vladimir Wilson Hidalgo Quispe
from math import sqrt
a = int(input("ingrese el coeficiente a: "))
b = int(input("ingrese el coeficiente b: "))
c = int(input("ingrese el coeficiente c: "))
raiz = b**2 - (4*a*c)
if raiz == 0 :
    print("la ecuacion tiene solucion y sus raices son iguales")
    x = -b + sqrt(raiz)/2*a
    print ("x1 y x2 son =" + str(x))
elif raiz > 0:
    print("la ecuacion de seguno grado si tiene solocion y sus raices seran distintas")
    x1 = -b +(sqrt(raiz))/2*a
    x2 = -b -(sqrt(raiz))/2*a
    print("x1 es = "+str(x1)+" x2 es ="+ str(x2))
else:
    print("la solucion tiene reaices imaginarias")
    