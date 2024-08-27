import pyodbc
from tkinter import messagebox
class Paciente:

    def __init__(self, crud):
        self.crud = crud

    def registrar_paciente(self, nombre,edad,contacto,direccion):
        self.crud.registrar_Paciente(nombre,edad,contacto,direccion)

    def actualizar_paciente(self, id_paciente,nombre,edad,contacto,direccion):
        self.crud.actualizar_Paciente(id_paciente,nombre, edad, contacto, direccion)

    def eliminar_paciente(self, id_paciente):
        self.crud.eliminar_Paciente(id_paciente)

    def buscar_paciente(self, id_paciente):
        consulta = """
        SELECT nombre_Paciente, edad_Paciente, contacto_Paciente, direccion_Paciente
        FROM Paciente
        WHERE id_Paciente = ?
        """
        try:
            result = self.crud.db.cursor.execute(consulta, (id_paciente,)).fetchone()
            if result:
                return result  
            else:
                return None
        except pyodbc.Error as e:
            messagebox.showerror("Error", str(e))
            return None

    def historial_pacientes(self, id_Paciente):
        return self.crud.historial_paciente(id_Paciente)






