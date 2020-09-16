#vladimir Wilson Hidalgo Quispe
#ingrese un tiempo x que estara en segundos
#luego ingrese el tiempo en segundo s minutos horas

segundos=int(input("ingrese los segundos: "))
print("ingrese hora de la tarea HH MM SS")
datos = input().split(" ")
a=int(datos[0])
b=int(datos[1])
c=int(datos[2])


horas=int(segundos/3600)
segundos-=horas*3600
minutos=int(segundos/60)
segundos-=minutos*60
 
if a >= horas and b >= minutos and c >= segundos:
    print("si se puede realizar la tarea")
else:
    print("no se puede realizar la tarea")
