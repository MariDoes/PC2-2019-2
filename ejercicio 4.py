while True:
    n = int(input("ingrese el numero de la matriz"))
    if n >= 2 and n <= 5:
        break
    else:
        print("numero invalido, ingrese el numero otra vez")
        n = int(input("ingrese el numero de la matriz"))

    m = int(input("ingrese el numero de la matriz"))
    if m >= 2 and m <= 5:
        break
    else:
        print("numero invalido, ingrese el numero otra vez")
        m = int(input("ingrese el numero de la matriz"))  

matriz = []
for i in range(n):
    matriz.append(i)




print(matriz)