import pyodbc
from tabulate import tabulate

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

# Ejecutar una consulta
cursor.execute('SELECT * FROM Estudiantes')

# Obtener los nombres de las columnas
column_names = [column[0] for column in cursor.description]

# Obtener los datos
data = cursor.fetchall()

# Cerrar la conexión
conn.close()

# Mostrar los datos en forma de tabla usando tabulate
print(tabulate(data, headers=column_names, tablefmt='pretty'))
