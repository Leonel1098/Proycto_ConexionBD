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
            # Intenta eliminar el paciente
            self.db.ejecutar_consulta(consulta, (id_Paciente,))
            messagebox.showinfo("Éxito", "Paciente eliminado correctamente.")
        except pyodbc.ProgrammingError as e:
            error_message = str(e)
            # Verifica si el error es por citas asociadas y pregunta si se desea continuar con la eliminacion
            if "El paciente tiene citas programadas" in error_message:
                respuesta = messagebox.askyesno("Advertencia", "El paciente tiene citas programadas. ¿Desea continuar con la eliminación?")
                if respuesta:
                    try:
                        # Si el usuario acepta, se ejecuta nuevamente la eliminación haciendo la eliminación de citas primero 
                        # para que deje eliminar el paciente
                        self.db.ejecutar_consulta("DELETE FROM Citas WHERE id_Paciente=?", (id_Paciente,))
                        self.db.ejecutar_consulta(consulta, (id_Paciente,))
                        messagebox.showinfo("Éxito", "Paciente y sus citas eliminados exitosamente.")
                    except pyodbc.Error as e:
                        messagebox.showerror("Error", f"No se pudo eliminar al paciente: {str(e)}")
                else:
                    messagebox.showinfo("Cancelado", "La eliminación del paciente ha sido cancelada.")
            else:
                messagebox.showerror("Error", f"Error desconocido: {str(e)}")




    #DOCTOR CRUD Procedimientos que sirven para gestionar datos del Doctor junto con la base de datos

    def registrar_Doctor(self, nombre, especialidad, contacto):
        consulta = "EXEC sp_Registrar_Doctores @nombre_Doctor=?, @especialidad_Doctor=?, @contacto_Doctor=?"
        self.db.ejecutar_consulta(consulta, (nombre, especialidad, contacto))

    def obtener_Doctor(self, id_Doctor):
        consulta = "SELECT * FROM Doctores WHERE id_Doctor = ?"
        return self.db.obtener_datos(consulta, (id_Doctor,))

    def actualizar_Doctor(self, id_Doctor, nombre, especialidad, contacto):
        consulta ="EXEC sp_Actualizar_Doctor @id_Doctor=?, @nombre_Doctor=?, @especialidad_Doctor=?, @contacto_Doctor=?"
        self.db.ejecutar_consulta(consulta, (id_Doctor, nombre, especialidad, contacto))

    def eliminar_Doctor(self, id_Doctor):
        consulta = "EXEC sp_Eliminar_Doctor @id_Doctor=?"
        try:
            # Elimina el doctor si no tiene citas asignadas
            self.db.ejecutar_consulta(consulta, (id_Doctor,))
            messagebox.showinfo("Éxito", "Doctor eliminado correctamente.")
        except pyodbc.ProgrammingError as e:
            error_message = str(e)
            # Verifica si el error es por citas asociadas y pregunta si se desea continuar con la eliminacion
            if "El Doctor tiene citas programadas" in error_message:
                respuesta = messagebox.askyesno("Advertencia", "El Doctor tiene citas programadas. ¿Desea continuar con la eliminación?")
                if respuesta:
                    try:
                        # Si el usuario acepta, se ejecuta nuevamente la eliminación haciendo la eliminación de citas primero 
                        # para que deje eliminar al doctor
                        self.db.ejecutar_consulta("DELETE FROM Citas WHERE id_Doctor=?", (id_Doctor,))
                        self.db.ejecutar_consulta(consulta, (id_Doctor,))
                        messagebox.showinfo("Éxito", "Doctor y sus citas eliminados exitosamente.")
                    except pyodbc.Error as e:
                        messagebox.showerror("Error", f"No se pudo eliminar al Doctor: {str(e)}")
                else:
                    messagebox.showinfo("Cancelado", "La eliminación del Doctor ha sido cancelada.")
            else:
                messagebox.showerror("Error", f"Error desconocido: {str(e)}")



    # CITAS CRUD Procedimientos que sirven para gestionar datos de las citas junto con la base de datos

    def registrar_Cita(self, id_Paciente, id_Doctor, fecha, hora):
        consulta = "EXEC sp_Agendar_Cita @id_Paciente=?, @id_Doctor=?, @fecha=?, @hora=?"
        self.db.ejecutar_consulta(consulta, (id_Paciente, id_Doctor, fecha, hora))

    def obtener_cita(self, id_cita):
        consulta = "SELECT * FROM Citas WHERE id_cita = ?"
        return self.db.obtener_datos(consulta, (id_cita,))

    def actualizar_Cita(self, id_cita,id_Paciente,id_Doctor,fecha, hora):
        consulta ="EXEC sp_Actualizar_Cita id_cita=?,@id_Paciente=?, @id_Doctor=?, @fecha=?, @hora=?"
        self.db.ejecutar_consulta(consulta, (id_cita,id_Paciente,id_Doctor,fecha, hora))

    def eliminar_Cita(self, id_cita):
        consulta = "DELETE FROM Citas WHERE id_cita = ?"
        self.db.ejecutar_consulta(consulta, (id_cita,))

    def visualizar_Citas(self):
        consulta = "EXEC sp_Mostar_Citas"
        return self.db.obtener_datos(consulta)

    def buscar_citas_por_Paciente(self, paciente):
        consulta = "EXEC sp_Filtrar_Citas_Paciente @paciente=?"
        parametros = (paciente,)
        return self.db.obtener_datos(consulta, parametros)
    
    def buscar_citas_por_Doctor(self, doctor):
        consulta = "EXEC sp_Filtrar_Citas_Doctor @doctor=?"
        parametros = (doctor,)
        return self.db.obtener_datos(consulta, parametros)

    def buscar_citas_por_Fecha(self, fecha):
        consulta = "EXEC sp_Filtrar_Citas_Fecha @fecha=?"
        parametros = (fecha,)
        return self.db.obtener_datos(consulta, parametros)

    #Muestra las citas al buscarlas por medio del id del paciente
    def historial_Paciente(self, id_Paciente):
        consulta = "EXEC sp_Historial_Citas_Pacientes @id_Paciente=?"
        return self.db.obtener_datos(consulta, (id_Paciente,))
