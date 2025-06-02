# Lista ordenada de códigos de libros
codigos_libros = [1001, 1023, 1050, 1088, 1100, 1205, 1230, 1301, 1350, 1400]

# Ingreso de codigo a buscar
codigo_busqueda = int(input("Ingrese el código del libro: "))

#Busqueda binaria
inicio = 0
fin = len(codigos_libros) -1
encontrado = False

while inicio <= fin:
    medio = (inicio + fin) // 2
    if codigos_libros[medio] == codigo_busqueda:
        encontrado = True
        break
    elif codigo_busqueda < codigos_libros[medio]:
        fin = medio - 1
    else:
        inicio = medio +1
        
#resultado
if encontrado:
    print("El libro está en el catalogo.")
else:
    print("El libro NO esta en el catalogo.")        