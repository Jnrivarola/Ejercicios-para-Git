from conexion import crear_conexion

def insertar_alumno(nombre, apellido, dni):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO alumnos (nombre, apellido, dni) VALUES (%s, %s, %s)"
            datos = (nombre, apellido, dni)  
            cursor.execute(sql, datos)
            conexion.commit()
            print("Alumno insertado correctamente.")
        except Exception as e:
             print("Error al insertar alumno:", e) 
        finally:
             conexion.close()   
def menu():
    print("=== Sistema de Gestión de Alumnos ===") 
    nombre = input("Nombre: ")
    apellido = input("Apellido: ") 
    dni = input("DNI: ")
    
    insertar_alumno(nombre, apellido, dni)
    
if __name__ == '__main__': 
    menu() 