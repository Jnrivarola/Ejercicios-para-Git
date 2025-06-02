"""3. Mayor de tres números
Situación: 
    Ingresar tres números y mostrar cuál es el mayor de los tres."""
    
num1 = int(input("Ingrese primer número: "))  
num2 = int(input("Ingrese segundo número: "))  
num3 = int(input("Ingrese tercer número: "))  

maximo = max(num1,num2,num3) 
print(f"El número mayor es: {maximo}") 