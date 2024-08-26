import pyodbc

class BaseDeDatos:
    def __init__(self):
        self.conexion = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=LEONEL;'
            'DATABASE=Gestion_Citas_Medicas;'
            'UID=Leonel;'
            'PWD=Leonel'
        )
        self.cursor = self.conexion.cursor()

    def ejecutar_consulta(self, consulta, parametros=()):
        try:
            self.cursor.execute(consulta, parametros)
            self.conexion.commit()
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")

    def obtener_datos(self, consulta, parametros=()):
        try:
            self.cursor.execute(consulta, parametros)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener datos: {e}")
            return []

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
