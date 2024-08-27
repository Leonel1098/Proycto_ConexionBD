import pyodbc
from tkinter import messagebox
class Doctor:

    def __init__(self,crud):
        self.crud = crud

    def registrar_doctor(self, nombre, especialidad, contacto):
        self.crud.registrar_Doctor(nombre,especialidad,contacto)
    
    def actualizar_doctor(self, id_doctor,nombre,especialidad,contacto):
        self.crud.actualizar_Doctor(id_doctor,nombre, especialidad, contacto)

    def eliminar_doctor(self, id_doctor):
        self.crud.eliminar_Doctor(id_doctor)

    def buscar_doctor(self, id_doctor):
        consulta = """
        SELECT nombre_Doctor, especialidad_Doctor, contacto_Doctor
        FROM Doctores
        WHERE id_Doctor = ?
        """
        try:
            result = self.crud.db.cursor.execute(consulta, (id_doctor,)).fetchone()
            if result:
                return result  
            else:
                return None
        except pyodbc.Error as e:
            messagebox.showerror("Error", str(e))
            return None
    