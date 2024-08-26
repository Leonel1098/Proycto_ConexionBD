import tkinter as tk
from tkinter import ttk, messagebox
from CRUD import CRUD
from database import BaseDeDatos

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Citas Médicas")
        self.root.geometry("800x600")
        
        # Inicializar Base de Datos y CRUD
        self.db = BaseDeDatos()
        self.crud = CRUD(self.db)

        # Crear la interfaz gráfica
        self.create_widgets()

    def create_widgets(self):
        # Frame para el registro de pacientes
        self.frame_paciente = tk.LabelFrame(self.root, text="Registrar Paciente")
        self.frame_paciente.pack(fill="x", padx=10, pady=10)

        tk.Label(self.frame_paciente, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_nombre = tk.Entry(self.frame_paciente)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.frame_paciente, text="Edad:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_edad = tk.Entry(self.frame_paciente)
        self.entry_edad.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.frame_paciente, text="Contacto:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_contacto = tk.Entry(self.frame_paciente)
        self.entry_contacto.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.frame_paciente, text="Dirección:").grid(row=3, column=0, padx=10, pady=5)
        self.entry_direccion = tk.Entry(self.frame_paciente)
        self.entry_direccion.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.frame_paciente, text="Registrar", command=self.registrar_paciente).grid(row=4, columnspan=2, pady=10)

        # Frame para el registro de doctores
        self.frame_doctor = tk.LabelFrame(self.root, text="Registrar Doctor")
        self.frame_doctor.pack(fill="x", padx=10, pady=10)

        tk.Label(self.frame_doctor, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_nombre_doctor = tk.Entry(self.frame_doctor)
        self.entry_nombre_doctor.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.frame_doctor, text="Especialidad:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_especialidad = tk.Entry(self.frame_doctor)
        self.entry_especialidad.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.frame_doctor, text="Contacto:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_contacto_doctor = tk.Entry(self.frame_doctor)
        self.entry_contacto_doctor.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.frame_doctor, text="Registrar", command=self.registrar_doctor).grid(row=3, columnspan=2, pady=10)

        # Frame para programar citas
        self.frame_cita = tk.LabelFrame(self.root, text="Programar Cita")
        self.frame_cita.pack(fill="x", padx=10, pady=10)

        tk.Label(self.frame_cita, text="Paciente ID:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_paciente_id = tk.Entry(self.frame_cita)
        self.entry_paciente_id.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.frame_cita, text="Doctor ID:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_doctor_id = tk.Entry(self.frame_cita)
        self.entry_doctor_id.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.frame_cita, text="Fecha (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5)
        self.entry_fecha = tk.Entry(self.frame_cita)
        self.entry_fecha.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.frame_cita, text="Hora (HH:MM):").grid(row=3, column=0, padx=10, pady=5)
        self.entry_hora = tk.Entry(self.frame_cita)
        self.entry_hora.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.frame_cita, text="Programar Cita", command=self.programar_cita).grid(row=4, columnspan=2, pady=10)

        # Frame para visualizar citas
        self.frame_visualizar = tk.LabelFrame(self.root, text="Visualizar Citas")
        self.frame_visualizar.pack(fill="x", padx=10, pady=10)

        self.treeview_citas = ttk.Treeview(self.frame_visualizar, columns=("ID", "Paciente", "Doctor", "Fecha", "Hora"), show="headings")
        self.treeview_citas.heading("ID", text="ID")
        self.treeview_citas.heading("Paciente", text="Paciente")
        self.treeview_citas.heading("Doctor", text="Doctor")
        self.treeview_citas.heading("Fecha", text="Fecha")
        self.treeview_citas.heading("Hora", text="Hora")
        self.treeview_citas.pack(fill="both", expand=True)

        tk.Button(self.frame_visualizar, text="Cargar Citas", command=self.cargar_citas).pack(pady=10)

    def registrar_paciente(self):
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        contacto = self.entry_contacto.get()
        direccion = self.entry_direccion.get()
        self.crud.crear_paciente(nombre, edad, contacto, direccion)
        messagebox.showinfo("Éxito", "Paciente registrado exitosamente")

    def registrar_doctor(self):
        nombre = self.entry_nombre_doctor.get()
        especialidad = self.entry_especialidad.get()
        contacto = self.entry_contacto_doctor.get()
        self.crud.crear_doctor(nombre, especialidad, contacto)
        messagebox.showinfo("Éxito", "Doctor registrado exitosamente")

    def programar_cita(self):
        paciente_id = self.entry_paciente_id.get()
        doctor_id = self.entry_doctor_id.get()
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        self.crud.programar_cita(paciente_id, doctor_id, fecha, hora)
        messagebox.showinfo("Éxito", "Cita programada exitosamente")

    def cargar_citas(self):
        for row in self.treeview_citas.get_children():
            self.treeview_citas.delete(row)

        citas = self.crud.visualizar_citas()
        for cita in citas:
            self.treeview_citas.insert("", "end", values=cita)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
