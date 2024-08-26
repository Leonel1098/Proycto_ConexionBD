class Paciente:

    def __init__(self, crud):
        self.crud = crud
    def registar_paciente(self, nombre,edad,contacto,direccion):
        self.crud.registrar_Paciente(nombre,edad,contacto,direccion)

    def historial_pacientes(self, id_Paciente):
        return self.crud.historial_paciente(id_Paciente)






