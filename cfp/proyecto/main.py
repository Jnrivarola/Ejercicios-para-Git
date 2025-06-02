import tkinter as tk
from tkinter import messagebox
from conexion import crear_conexion

def guardar_datos():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    dni = entry_dni.get()

    if not nombre or not apellido or not dni:
        messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios")
        return

    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO alumnos (nombre, apellido, dni) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nombre, apellido, dni))
            conexion.commit()
            messagebox.showinfo("Éxito", "Alumno guardado correctamente")
            entry_nombre.delete(0, tk.END)
            entry_apellido.delete(0, tk.END)
            entry_dni.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el alumno\n{e}")
        finally:
            conexion.close()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Registro de Alumnos")

# Campos de entrada
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Apellido:").grid(row=1, column=0, padx=10, pady=5)
entry_apellido = tk.Entry(ventana)
entry_apellido.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="DNI:").grid(row=2, column=0, padx=10, pady=5)
entry_dni = tk.Entry(ventana)
entry_dni.grid(row=2, column=1, padx=10, pady=5)

# Botón de guardar
btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
btn_guardar.grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()
