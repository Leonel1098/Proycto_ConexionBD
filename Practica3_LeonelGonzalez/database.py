import pyodbc

class BaseDeDatos:
    def __init__(self):
        try:
            self.conexion = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=PC-DEV14;'
                'DATABASE=Gestion_Citas_Medicas;'
                'UID=Leonel;'
                'PWD=Leonel'
            )
            self.cursor = self.conexion.cursor()
        except pyodbc.Error as e:
            print("Error al conectar la base de datos",e)
            raise
    def ejecutar_consulta(self, consulta, parametros = None):
        try:
            if parametros:
                self.cursor.execute(consulta, parametros)
            else:
                self.cursor.execute(consulta)
            self.conexion.commit()
        except pyodbc.Error as e:
            print("Erro al ejecutar el procedimiento",e)
            raise

    def obtener_datos(self, consulta, parametros = None):
        try:
            if parametros:
                self.cursor.execute(consulta, parametros)
            else:
                self.cursor.execute(consulta)
                return self.cursor.fetchall()
        except pyodbc.Error as e:
            print(f"Error al obtener datos:",e)
            raise
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
