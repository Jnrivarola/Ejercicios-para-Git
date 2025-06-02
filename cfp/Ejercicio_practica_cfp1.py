"""1. Clasificación de nota
Situación: Ingresar una nota del 0 al 10 y mostrar si
el estudiante está:
● Desaprobado (0 a 5)
● Aprobado (6 a 8)
● Sobresaliente (9 o 10)"""

nota = int(input("ingrese una nota(del 0 al 10): "))

if nota >= 0 and nota <= 5:
    print("Desaprobado.")
elif nota >= 6 and nota <= 8:
    print("Aprobado.")
elif nota >= 9 and nota <= 10:
    print("Sobresaliente.")
else:
    print("Nota inválida. Usted debe ingresar una nota del 0 al 10.")
