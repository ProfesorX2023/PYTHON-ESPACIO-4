import pyodbc
import pandas as pd

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

# Convertir los datos a una lista de listas (en lugar de una lista de tuplas)
data_list = [list(row) for row in data]

# Cerrar la conexión
conn.close()

# Crear un DataFrame de pandas
df = pd.DataFrame(data_list, columns=column_names)

# Mostrar el DataFrame
print(df)