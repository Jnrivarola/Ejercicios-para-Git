print("Cálculo de promedio de notas")

try:
    total = float(input("Ingrese el total de puntos obtenidos: "))
    cantidad = int(input("Ingrese la cantidad de evaluaciones: "))
    promedio = total / cantidad
except ValueError:
    print("Error: Debe ingresar solo numeros.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
else:
    print(f"El promedio del estudiante es: {promedio:.2f}")
finally:
    print("Gracias por usar el sistema de calculo de promedio.")