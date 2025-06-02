"""4. Función que calcule el promedio de 3 notas
Situación: Crear una función que reciba 3 notas,
calcule el promedio y lo devuelva."""

def calcular_promedio(a,b,c):
    return (a+b+c)//3


nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercer nota: "))

resultado = calcular_promedio(nota1,nota2,nota3)

print(f"El promedio de {nota1}, {nota2} y {nota3} es: {resultado}.")
