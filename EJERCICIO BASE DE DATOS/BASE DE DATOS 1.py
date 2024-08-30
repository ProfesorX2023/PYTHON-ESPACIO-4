import pyodbc

#Establecer la conexion a la base de datos SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-HNACHSH;'
    'DATABASE=Universidad;'
    'UID=python;'  # Reemplaza 'tu_usuario' con tu nombre de usuario de SQL Server
    'PWD=1234;'  # Reemplaza 'tu_contraseña' con tu contraseña de SQL Server
)

#Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

#Ejecutar una consulta
cursor.execute('SELECT * FROM Estudiantes')


conn.close()