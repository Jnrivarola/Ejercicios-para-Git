#Lista de DNIs registrados
dnis_registrados = [40123456, 39222333, 40888999, 37777111, 36666111, 42222555, 39999888, 38555222]

#ingreso de dato por el usuario
dni_busqueda = int(input("Ingrese el DNI  del alumno para verificar inscripción: "))

#busqueda lineal
encontrado = False
for dni in dnis_registrados:
    if dni == dni_busqueda:
        encontrado = True
        break
    
#resultado
if encontrado:
    print("El alumno esta registrado.")
else:
    print("El alumno NO esta registrado")    

