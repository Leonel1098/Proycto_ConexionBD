from database import BaseDeDatos
class CRUD:

    def __init__(self, db):
        self.db = db
    
    # Paciente CRUD operations
    def registrar_Paciente(self, nombre, edad, contacto, direccion):
        consulta = "EXEC sp_Registrar_Paciente @nombre_Paciente=?, @edad_Paciente=?, @contacto_Paciente=?, @direccion_Paciente=?"
        self.db.ejecutar_consulta(consulta, (nombre, edad, contacto, direccion))

    def obtener_Paciente(self, id_Paciente):
        consulta = "SELECT * FROM Paciente WHERE id = ?"
        return self.db.obtener_datos(consulta, (id_Paciente,))

    def actualizar_Paciente(self, id_Paciente, nombre, edad, contacto, direccion):
        consulta = '''
        UPDATE Paciente SET nombre_Paciente=?, edad_Paciente=?, contacto_Paciente=?, direccion_Paciente=? WHERE id=?
        '''
        self.db.ejecutar_consulta(consulta, (nombre, edad, contacto, direccion, id_Paciente))

    def eliminar_Paciente(self, id_Paciente):
        consulta = "DELETE FROM Paciente WHERE id = ?"
        self.db.ejecutar_consulta(consulta, (id_Paciente,))

    # Doctor CRUD operations
    def registar_Doctor(self, nombre, especialidad, contacto):
        consulta = "EXEC sp_Registrar_Doctor @nombre_Doctor=?, @especialidad_Doctor=?, @contacto_Doctor=?"
        self.db.ejecutar_consulta(consulta, (nombre, especialidad, contacto))

    def obtener_Doctor(self, id_Doctor):
        consulta = "SELECT * FROM Doctores WHERE id = ?"
        return self.db.obtener_datos(consulta, (id_Doctor,))

    def actualizar_Doctor(self, id_Doctor, nombre, especialidad, contacto):
        consulta = '''
        UPDATE Doctores SET nombre_Doctor=?, especialidad_Doctor=?, contacto_Doctor=? WHERE id=?
        '''
        self.db.ejecutar_consulta(consulta, (nombre, especialidad, contacto, id_Doctor))

    def eliminar_Doctor(self, id_Doctor):
        consulta = "DELETE FROM Doctores WHERE id = ?"
        self.db.ejecutar_consulta(consulta, (id_Doctor,))

    # Cita CRUD operations
    def registrar_Cita(self, id_Paciente, id_Doctor, fecha, hora):
        consulta = "EXEC sp_Agendar_Cita @id_Paciente=?, @id_Doctor=?, @fecha=?, @hora=?"
        self.db.ejecutar_consulta(consulta, (id_Paciente, id_Doctor, fecha, hora))

    def obtener_cita(self, id_cita):
        consulta = "SELECT * FROM Citas WHERE id = ?"
        return self.db.obtener_datos(consulta, (id_cita,))

    def actualizar_cita(self, id_cita, fecha, hora):
        consulta = '''
        UPDATE Citas SET fecha=?, hora=? WHERE id=?
        '''
        self.db.ejecutar_consulta(consulta, (fecha, hora, id_cita))

    def eliminar_cita(self, id_cita):
        consulta = "DELETE FROM Citas WHERE id = ?"
        self.db.ejecutar_consulta(consulta, (id_cita,))

    def visualizar_citas(self):
        consulta = "EXEC sp_Mostar_Citas"
        return self.db.obtener_datos(consulta)

    def historial_paciente(self, id_Paciente):
        consulta = "EXEC sp_Historial_Citas_Pacientes @id_Paciente=?"
        return self.db.obtener_datos(consulta, (id_Paciente,))
