"""#funciones
def func():

    print("Hola mundo")
    
    
#codigo    


lista = [1, "dos", func]  # Una lista con un número, texto y una función



lista[2]()  # Ejecuta la función: "Hola mundo"""

#Cuente,el,numero,de,palabras, cuente el numero de caracteres, retorme ambos valores

def promediar(a,b,c):
    return (a+b+c)//3

num1 = int(input("primer numero: "))
num2 = int(input("segundo numero: "))
num3 = int(input("tercer numero: "))

resultado = promediar(num1,num2,num3)

print(f"El promedio es: {resultado}")

