class Doctor:

    def __init__(self,crud):
        self.crud = crud

    def registar_doctor(self, nombre, especialidad, contacto):
        self.crud.registar_Doctor(nombre,especialidad,contacto)
