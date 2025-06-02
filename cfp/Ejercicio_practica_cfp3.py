"""3. Ingreso de contraseña
Situación: El programa debe pedir al usuario que
ingrese una contraseña.
Solo se permite acceder si la contraseña ingresada es
"python123".
Si es incorrecta, debe pedirla nuevamente hasta que

sea correcta.
Al ingresar la correcta, mostrar "Acceso autorizado".
"""

password = input("Ingrese la contraseña: ").lower() #.upper()

while password != "python123":
    print("Contraseña incorrecta...")
    password = input("Ingrese la contraseña: ").lower()
print("Acceso autorizado!!!")
