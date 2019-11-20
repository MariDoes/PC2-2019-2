#Escriba un programa que registre las inscripciones de un curso de natación. 
#El curso solo acepta 5 personas y se debe preguntar 3 datos: nombre, sexo y edad. 
#El programa solo debe permitir inscripciones de edades entre 5 y 17 años. 
# El programa debe terminar cuando se tenga a las 5 personas que cumplan los requisitos y mostrar lo siguiente:
#•	Lista de inscritos (mostrar todos sus datos).
#•	Cantidad de hombres y mujeres.
#•	Promedio de edad.
N =[]
E =[]
SM =[]
SF =[]



while True:
    e = int(input("Ingrese su edad: "))
    if (e >= 5) and (e <= 17):
        E.append(e)
        if E == 6:
            break
    else:
        print("numero invalido, vuelva a ingresar")
        e = int(input("Ingrese su edad: "))

    n = input("Ingrese su nombre: ")

    s = input("Ingrese su sexo (M/F): ").lower
    if s == m:
        SM.append(s)
    elif s == f:
        SF.append(s)
    else:
        print("Dato invalido, vuelva a ingresar (M/F)")
        s = input("Ingrese su sexo (M/F): ").lower 

print(E)   
print(e)
print(n)
print(s)