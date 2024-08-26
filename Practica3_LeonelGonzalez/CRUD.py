from database import BaseDeDatos

class CRUD:

    def __init__(self, db) :
        self.db = db
    
    # Paciente CRUD operations
    def crear_paciente(self, nombre, edad, contacto, direccion):
        consulta = "EXEC sp_Registrar_Paciente @Nombre=?, @Edad=?, @Contacto=?, @Direccion=?"
        self.db.ejecutar_consulta(consulta, (nombre, edad, contacto, direccion))

    def obtener_paciente(self, paciente_id):
        consulta = "SELECT * FROM Paciente WHERE id = ?"
        return self.db.obtener_datos(consulta, (paciente_id,))

    def actualizar_paciente(self, paciente_id, nombre, edad, contacto, direccion):
        consulta = '''
        UPDATE Pacientes SET nombre=?, edad=?, contacto=?, direccion=? WHERE id=?
        '''
        self.db.ejecutar_consulta(consulta, (nombre, edad, contacto, direccion, paciente_id))

    def eliminar_paciente(self, paciente_id):
        consulta = "DELETE FROM Paciente WHERE id = ?"
        self.db.ejecutar_consulta(consulta, (paciente_id,))

    # Doctor CRUD operations
    def crear_doctor(self, nombre, especialidad, contacto):
        consulta = "EXEC sp_Registrar_Doctor @Nombre=?, @Especialidad=?, @Contacto=?"
        self.db.ejecutar_consulta(consulta, (nombre, especialidad, contacto))

    def obtener_doctor(self, doctor_id):
        consulta = "SELECT * FROM Doctores WHERE id = ?"
        return self.db.obtener_datos(consulta, (doctor_id,))

    def actualizar_doctor(self, doctor_id, nombre, especialidad, contacto):
        consulta = '''
        UPDATE Doctores SET nombre=?, especialidad=?, contacto=? WHERE id=?
        '''
        self.db.ejecutar_consulta(consulta, (nombre, especialidad, contacto, doctor_id))

    def eliminar_doctor(self, doctor_id):
        consulta = "DELETE FROM Doctores WHERE id = ?"
        self.db.ejecutar_consulta(consulta, (doctor_id,))

    # Cita CRUD operations
    def programar_cita(self, paciente_id, doctor_id, fecha, hora):
        consulta = "EXEC sp_Agendar_Cita @PacienteID=?, @DoctorID=?, @Fecha=?, @Hora=?"
        self.db.ejecutar_consulta(consulta, (paciente_id, doctor_id, fecha, hora))

    def obtener_cita(self, cita_id):
        consulta = "SELECT * FROM Citas WHERE id = ?"
        return self.db.obtener_datos(consulta, (cita_id,))

    def actualizar_cita(self, cita_id, fecha, hora):
        consulta = '''
        UPDATE Citas SET fecha=?, hora=? WHERE id=?
        '''
        self.db.ejecutar_consulta(consulta, (fecha, hora, cita_id))

    def eliminar_cita(self, cita_id):
        consulta = "DELETE FROM Citas WHERE id = ?"
        self.db.ejecutar_consulta(consulta, (cita_id,))

    def visualizar_citas(self):
        consulta = "EXEC sp_Mostar_Citas"
        return self.db.obtener_datos(consulta)

    def historial_paciente(self, paciente_id):
        consulta = "EXEC sp_Historial_Citas_Pacientes @PacienteID=?"
        return self.db.obtener_datos(consulta, (paciente_id,))