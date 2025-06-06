"""En una clase de programación, necesitás registrar quiénes asistieron. 
Para eso, vas a hacer un programa en Python que:
Le pida al usuario ingresar los nombres de los presentes separados por comas.
Guarde cada nombre en una línea distinta dentro de un archivo llamado asistencia.txt.
Luego lea e imprima en pantalla el contenido del archivo."""

print("Por favor ingrese una lista de nombres(Separados por coma) y al finalizar presione Enter.")
print("=========================================================================================")

presentes = input("Nombre: ")
nombres = presentes.split(",")

with open("asistencia.txt", "w", encoding="utf-8") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")
        
with open("asistencia.txt", "r", encoding="utf-8") as archivo:
    print("Personas presentes: ")        
    print("====================")
    print(archivo.read())


