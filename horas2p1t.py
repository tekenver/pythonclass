#Vladimir Wilson Hidalgo Quispe
print ("ingrese HH MM SS")
datos = input().split(" ")

a=int(datos[0])
b=int(datos[1])
c=int(datos[2])

c = c+1

if c > 59:
    c = 00
    b = b+1
    if b > 59:
        a = a +1
        b = 00
        if a > 23:
            a = 00
            print(str(a)+":"+str(b)+":"+str(c))

        else:
            print(str(a)+":"+str(b)+":"+str(c))

    else:
        print(str(a)+":"+str(b)+":"+str(c))

else:
    print(str(a)+":"+str(b)+":"+str(c))