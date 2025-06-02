"""2. Par o impar 
 Situación: Pedir un número al usuario y decir si es par o impar. """

numero = int(input("Ingrese un número para saber si es par o no: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
