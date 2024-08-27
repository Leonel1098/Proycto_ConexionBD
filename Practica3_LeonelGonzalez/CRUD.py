import pyodbc
from tkinter import messagebox
from database import BaseDeDatos
class CRUD:

    def __init__(self, db):
        self.db = db
    
    # Paciente CRUD Procedimientos que sirven para gestionar datos junto con la base de datos
    def registrar_Paciente(self, nombre, edad, contacto, direccion):
        consulta = "EXEC sp_Registrar_Paciente @nombre_Paciente=?, @edad_Paciente=?, @contacto_Paciente=?, @direccion_Paciente=?"
        self.db.ejecutar_consulta(consulta, (nombre, edad, contacto, direccion))

    def obtener_Paciente(self, id_Paciente):
        consulta = "SELECT * FROM Paciente WHERE id_Paciente = ?"
        return self.db.obtener_datos(consulta, (id_Paciente,))

    def actualizar_Paciente(self, id_Paciente, nombre, edad, contacto, direccion):
        consulta ="EXEC sp_Actualizar_Paciente @id_Paciente=?, @nombre_Paciente=?, @edad_Paciente=?, @contacto_Paciente=?, @direccion_Paciente=?"
        self.db.ejecutar_consulta(consulta, (id_Paciente, nombre, edad, contacto, direccion))

    def eliminar_Paciente(self, id_Paciente):
        consulta = "EXEC sp_Eliminar_Paciente @id_Paciente=?"
        try:
            self.db.ejecutar_consulta(consulta, (id_Paciente,))
        except pyodbc.Error as e:
            error_message = str(e)
            print(f"Error: {error_message}")
            messagebox.showwarning("Advertencia", error_message)


    #DOCTOR CRUD Procedimientos que sirven para gestionar datos junto con la base de datos

    def registrar_Doctor(self, nombre, especialidad, contacto):
        consulta = "EXEC sp_Registrar_Doctores @nombre_Doctor=?, @especialidad_Doctor=?, @contacto_Doctor=?"
        self.db.ejecutar_consulta(consulta, (nombre, especialidad, contacto))

    def obtener_Doctor(self, id_Doctor):
        consulta = "SELECT * FROM Doctores WHERE id_Doctor = ?"
        return self.db.obtener_datos(consulta, (id_Doctor,))

    def actualizar_Doctor(self, id_Doctor, nombre, especialidad, contacto):
        consulta = '''
        UPDATE Doctores SET nombre_Doctor=?, especialidad_Doctor=?, contacto_Doctor=? WHERE id_Doctor=?
        '''
        self.db.ejecutar_consulta(consulta, (nombre, especialidad, contacto, id_Doctor))

    def eliminar_Doctor(self, id_Doctor):
        consulta = "DELETE FROM Doctores WHERE id_Doctor = ?"
        self.db.ejecutar_consulta(consulta, (id_Doctor,))

    # CITAS CRUD Procedimientos que sirven para gestionar datos junto con la base de datos

    def registrar_Cita(self, id_Paciente, id_Doctor, fecha, hora):
        consulta = "EXEC sp_Agendar_Cita @id_Paciente=?, @id_Doctor=?, @fecha=?, @hora=?"
        self.db.ejecutar_consulta(consulta, (id_Paciente, id_Doctor, fecha, hora))

    def obtener_cita(self, id_cita):
        consulta = "SELECT * FROM Citas WHERE id_cita = ?"
        return self.db.obtener_datos(consulta, (id_cita,))

    def actualizar_cita(self, id_cita, fecha, hora):
        consulta = '''
        UPDATE Citas SET fecha=?, hora=? WHERE id_cita=?
        '''
        self.db.ejecutar_consulta(consulta, (fecha, hora, id_cita))

    def eliminar_cita(self, id_cita):
        consulta = "DELETE FROM Citas WHERE id_cita = ?"
        self.db.ejecutar_consulta(consulta, (id_cita,))

    def visualizar_citas(self):
        consulta = "EXEC sp_Mostar_Citas"
        return self.db.obtener_datos(consulta)

    def historial_paciente(self, id_Paciente):
        consulta = "EXEC sp_Historial_Citas_Pacientes @id_Paciente=?"
        return self.db.obtener_datos(consulta, (id_Paciente,))
