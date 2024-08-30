import pyodbc

# Establecer la conexión a la base de datos SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-HNACHSH;'
    'DATABASE=Universidad;'
    'UID=python;'  # Reemplaza 'tu_usuario' con tu nombre de usuario de SQL Server
    'PWD=1234;'  # Reemplaza 'tu_contraseña' con tu contraseña de SQL Server
)

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Ejemplo de consulta: Seleccionar todos los estudiantes
cursor.execute('SELECT * FROM Estudiantes')
estudiantes = cursor.fetchall()
print("Estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

# Ejemplo de inserción: Añadir un nuevo estudiante
cursor.execute('''
    INSERT INTO Estudiantes (id_estudiante, nombre, apellido, fecha_nacimiento, genero, departamento_id)
    VALUES (?, ?, ?, ?, ?, ?)
''', (7, 'Pedro', 'Suarez', '2002-02-14', 'Masculino', 1))
conn.commit()  # Asegurarse de guardar los cambios

# Verificar que el estudiante se ha insertado
cursor.execute('SELECT * FROM Estudiantes WHERE id_estudiante = 7')
nuevo_estudiante = cursor.fetchone()
print("\nNuevo Estudiante Insertado:")
print(nuevo_estudiante)

# Ejemplo de actualización: Actualizar el nombre de un estudiante
cursor.execute('''
    UPDATE Estudiantes
    SET nombre = ?
    WHERE id_estudiante = ?
''', ('Pedro Actualizado', 7))
conn.commit()  # Asegurarse de guardar los cambios

# Verificar la actualización
cursor.execute('SELECT * FROM Estudiantes WHERE id_estudiante = 7')
estudiante_actualizado = cursor.fetchone()
print("\nEstudiante Actualizado:")
print(estudiante_actualizado)

# Ejemplo de eliminación: Eliminar un estudiante
cursor.execute('DELETE FROM Estudiantes WHERE id_estudiante = ?', (7,))
conn.commit()  # Asegurarse de guardar los cambios

# Verificar la eliminación
cursor.execute('SELECT * FROM Estudiantes WHERE id_estudiante = 7')
estudiante_eliminado = cursor.fetchone()
print("\nEstudiante Eliminado (debe ser None):")
print(estudiante_eliminado)

# Cerrar la conexión
conn.close()
