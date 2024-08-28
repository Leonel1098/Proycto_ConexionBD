from tkinter import messagebox
import tkinter as tk

#En esta clase se crean los metodos que sirven para manejar los procedimientos de la base de datos por medio del CRUD
class Cita:
    def __init__(self, crud):
        self.crud = crud

    def registrar_cita(self, id_Paciente,id_Doctor, fecha,hora):
        self.crud.registrar_Cita(id_Paciente,id_Doctor,fecha,hora)

    def actualizar_cita(self, id_cita,id_paciente,id_doctor,fecha,hora):
        self.crud.actualizar_Cita(id_cita,id_paciente,id_doctor,fecha, hora)

    def eliminar_cita(self, id_cita):
        self.crud.eliminar_Cita(id_cita)

    def visualizar_citas(self):
        return self.crud.visualizar_Citas()
    
    def filtrar_citas(self,paciente, doctor,fecha):
        self.crud.filtrar_Citas(paciente,doctor,fecha)

    def filtrar_citas_paciente(self, paciente):
        self.crud.buscar_citas_por_Paciente(paciente)
    
    def filtrar_citas_doctor(self, doctor):
        self.crud.buscar_citas_por_Doctor(doctor)

    def filtrar_citas_fecha(self, fecha):
        self.crud.buscar_citas_por_Fecha(fecha)

    def obtener_citas(self):
        self.crud.obtener_cita()
