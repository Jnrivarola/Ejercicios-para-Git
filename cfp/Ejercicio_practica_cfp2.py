"""2. Par o impar
Situación: Pedir un número al usuario y decir si es
par o impar."""

numero = int(input("Por favor ingrse un número para saber si es par o impar: "))


if numero % 2 == 0:
    print("Es par.")
else:
    print("Es impar.")