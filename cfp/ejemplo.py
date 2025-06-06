try:
    numero=int(input("Ingrese un numero: "))

    print(numero)

except ValueError:
    print("Error: Debe ingresar números.")
    
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
    
finally:
    print("Gracias por ingresar su número.")