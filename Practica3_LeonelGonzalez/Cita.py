class Cita:
    def __init__(self, crud):
        self.crud = crud

    def registrar_cita(self, id_Paciente,id_Doctor, fecha,hora, crud):
        self.crud.registrar_Cita(id_Paciente,id_Doctor,fecha,hora)

    def obtener_citas(self):
        self.crud.obtener_cita()
