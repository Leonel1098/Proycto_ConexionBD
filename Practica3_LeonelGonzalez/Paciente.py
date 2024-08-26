class Paciente:

    def __init__(self, id, nombre, edad, contacto, direccion):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.contacto = contacto
        self.direccion = direccion

    
    def registrar_Paciente(self, data_base):
        data_base.ejecutar_procedimiento

