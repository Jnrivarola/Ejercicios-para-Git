"""Crear un programa que:
Pida al usuario el nombre de un archivo para abrir (puede ser datos.txt, por ejemplo).
Intente abrirlo y leer su contenido usando with open(...).
Si el archivo no existe, debe mostrar un mensaje personalizado: "¡El archivo no fue encontrado!".
Si el archivo existe y puede leerse, debe mostrar el contenido por pantalla.
Agregá una excepción general para cualquier otro error.
"""

try:
    nombre = input("Ingrese el nombre del archivo que desea abrir: ")
    
    with open(nombre, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo: ")
        print(contenido)
        
except FileNotFoundError:
    print("El archivo buscado no existe.")
    
except PermissionError:
    print("Usted no esta autorizado para abrir el archivo.")
    
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")