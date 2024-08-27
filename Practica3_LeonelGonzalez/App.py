import tkinter as tk
from tkinter import ttk, messagebox
from CRUD import CRUD
from database import BaseDeDatos
from Paciente import Paciente
from Doctor import Doctor
from Cita import Cita

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Citas Médicas")
        self.root.geometry(f"{400}x{280}+{550}+{200}")
        self.root.config(bg = "black")


        # Inicializar Base de Datos y CRUD
        self.db = BaseDeDatos()
        self.crud = CRUD(self.db)
        self.paciente = Paciente(self.crud)
        self.doctor = Doctor(self.crud)
        self.cita = Cita(self.crud)

        # Crear la interfaz gráfica
        self.ventana_Principal()

    def ventana_Principal(self):
        self.frame_Principal = tk.Frame(self.root, bg="black")
        self.frame_Principal.pack(padx=10, pady=10)

        tk.Button(self.frame_Principal, text="Gestionar Pacientes", command=self.ventana_Registrar_Paciente, bg="gray", fg="black",
                  font=("Courier New", 14, "bold","italic"), width=20, height=1).grid(row=0, column=0, pady=10)
        
        tk.Button(self.frame_Principal, text="Gestionar Doctores",command= self.ventana_Registar_Doctor,bg="gray", fg="black",
                  font=("Courier New", 14, "bold","italic"),width=20, height=1).grid(row=1, column=0, pady=10)
        
        tk.Button(self.frame_Principal, text="Gestionar Citas",bg="gray", fg="black",
                  font=("Courier New", 14, "bold","italic"),width=20, height=1).grid(row=2, column=0, pady=10)
        
        tk.Button(self.frame_Principal, text="Visualizar Citas",bg="gray", fg="black",
                  font=("Courier New", 14, "bold","italic"),width=20, height=1).grid(row=3, column=0, pady=10)

    def ventana_Registrar_Paciente(self):
        ventana_paciente = tk.Toplevel(self.root)
        Ventana_Pacientes(ventana_paciente, self.paciente)

    def ventana_Registar_Doctor(self):
        ventana_doctor = tk.Toplevel(self.root)
        Ventana_Doctores(ventana_doctor, self.doctor)

    """def open_programar_cita(self):
        new_window = tk.Toplevel(self.root)
        ProgramarCitaWindow(new_window, self.cita)

    def open_visualizar_citas(self):
        new_window = tk.Toplevel(self.root)
        VisualizarCitasWindow(new_window, self.crud)"""

class Ventana_Pacientes:
    def __init__(self, root, paciente):
        self.root = root
        self.root.title("Registrar Paciente")
        self.root.geometry(f"{400}x{280}+{550}+{200}")
        self.root.config(bg = "black")
        self.paciente = paciente
        self.agregar_componentes()

    def agregar_componentes(self):
        
        tk.Label(self.root, text="Nombre:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90,y=35)
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.place(x=200,y=35)

        tk.Label(self.root, text="Edad:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90,y=60)
        self.entry_edad = tk.Entry(self.root)
        self.entry_edad.place(x=200,y=60)

        tk.Label(self.root, text="Contacto:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=85)
        self.entry_contacto = tk.Entry(self.root)
        self.entry_contacto.place(x=200, y=85)

        tk.Label(self.root, text="Dirección:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=110)
        self.entry_direccion = tk.Entry(self.root)
        self.entry_direccion.place(x=200, y=110)

        tk.Button(self.root, text="Registrar", command=self.registrar_paciente, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=200, y=140)
        
        tk.Button(self.root, text="Mas Opciones", command=self.ventana_eliminar_buscar, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=15, height=1).place(x=220, y=220)
        
        tk.Button(self.root, text="Actualizar", command=self.ventana_actualizar, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=220)

    def ventana_actualizar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Actualizar Paciente")
        ventana.geometry(f"{400}x{280}+{550}+{200}")
        ventana.config(bg="black")

        tk.Label(ventana, text="ID Paciente:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=12, height=1).place(x=75,y=35)
        self.entry_id = tk.Entry(ventana)
        self.entry_id.place(x=200,y=35)

        tk.Label(ventana, text="Nombre:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90,y=60)
        self.entry_nombre = tk.Entry(ventana)
        self.entry_nombre.place(x=200,y=60)

        tk.Label(ventana, text="Edad:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90,y=85)
        self.entry_edad = tk.Entry(ventana)
        self.entry_edad.place(x=200,y=85)

        tk.Label(ventana, text="Contacto:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=110)
        self.entry_contacto = tk.Entry(ventana)
        self.entry_contacto.place(x=200, y=110)

        tk.Label(ventana, text="Dirección:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=135)
        self.entry_direccion = tk.Entry(ventana)
        self.entry_direccion.place(x=200, y=135)

        tk.Button(ventana, text="Actualizar Datos", command=self.actualizar_paciente, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=16, height=1).place(x=140, y=210)

    def ventana_eliminar_buscar(self):
        ventana2 = tk.Toplevel(self.root)
        ventana2.title("Actualizar Paciente")
        ventana2.geometry(f"{400}x{200}+{550}+{250}")
        ventana2.config(bg="black")

        tk.Label(ventana2, text="ID Paciente:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=15, height=1).place(x=50,y=60)
        self.entry_id = tk.Entry(ventana2)
        self.entry_id.place(x=200,y=60)


        tk.Button(ventana2, text="Eliminar Paciente", command=self.eliminar_paciente, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=18, height=1).place(x=25, y=105)    
        
        tk.Button(ventana2, text="Buscar Paciente", command=self.buscar_paciente, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=16, height=1).place(x=220, y=105)

    def registrar_paciente(self):
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        contacto = self.entry_contacto.get()
        direccion = self.entry_direccion.get()
        self.paciente.registrar_paciente(nombre, edad, contacto, direccion)
        messagebox.showinfo("Éxito", "Paciente registrado exitosamente")
        self.root.destroy()

    def actualizar_paciente(self):
        id_paciente = self.entry_id.get()
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        contacto = self.entry_contacto.get()
        direccion = self.entry_direccion.get()
        self.paciente.actualizar_paciente(id_paciente,nombre, edad, contacto, direccion)
        messagebox.showinfo("Éxito", "Paciente actualizado exitosamente")
        self.root.destroy()
    

    def eliminar_paciente(self):
        id_paciente = self.entry_id.get()
        self.paciente.eliminar_paciente(id_paciente)
        messagebox.showinfo("Éxito", "Paciente eliminado exitosamente")

    def buscar_paciente(self):
        id_paciente = self.entry_id.get()
        paciente_data = self.paciente.buscar_paciente(id_paciente)
        
        if paciente_data:
            nombre, edad, contacto, direccion = paciente_data
            message = (f"Nombre: {nombre}\nEdad: {edad}\nContacto: {contacto}\nDirección: {direccion}")
            messagebox.showinfo("Paciente Encontrado", message)
        else:
            messagebox.showinfo("Busqueda", "No se encontró ningún paciente con ese ID.")


class Ventana_Doctores:

    def __init__(self, root, doctor):
        self.root = root
        self.root.title("Registrar Paciente")
        self.root.geometry(f"{400}x{280}+{550}+{200}")
        self.root.config(bg = "black")
        self.doctor = doctor
        self.agregar_componentes()

    def agregar_componentes(self):
        
        tk.Label(self.root, text="Nombre:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=50,y=35)
        self.entry_nombre_doctor = tk.Entry(self.root)
        self.entry_nombre_doctor.place(x=200,y=35)

        tk.Label(self.root, text="Especialidad:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=15, height=1).place(x=50,y=60)
        self.entry_especialidad = tk.Entry(self.root)
        self.entry_especialidad.place(x=200,y=60)

        tk.Label(self.root, text="Contacto:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=50, y=85)
        self.entry_contacto_doctor = tk.Entry(self.root)
        self.entry_contacto_doctor.place(x=200, y=85)

        tk.Button(self.root, text="Registrar", command=self.registrar_doctor, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=200, y=140)
        
        tk.Button(self.root, text="Mas Opciones", command=self.ventana_eliminar_buscar, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=15, height=1).place(x=220, y=220)
        
        tk.Button(self.root, text="Actualizar", command=self.ventana_actualizar, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=220)

    def ventana_actualizar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Actualizar Paciente")
        ventana.geometry(f"{400}x{280}+{550}+{200}")
        ventana.config(bg="black")

        tk.Label(ventana, text="ID Paciente:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=12, height=1).place(x=75,y=35)
        self.entry_id = tk.Entry(ventana)
        self.entry_id.place(x=200,y=35)

        tk.Label(ventana, text="Nombre:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90,y=60)
        self.entry_nombre = tk.Entry(ventana)
        self.entry_nombre.place(x=200,y=60)

        tk.Label(ventana, text="Edad:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90,y=85)
        self.entry_edad = tk.Entry(ventana)
        self.entry_edad.place(x=200,y=85)

        tk.Label(ventana, text="Contacto:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=110)
        self.entry_contacto = tk.Entry(ventana)
        self.entry_contacto.place(x=200, y=110)

        tk.Label(ventana, text="Dirección:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=135)
        self.entry_direccion = tk.Entry(ventana)
        self.entry_direccion.place(x=200, y=135)

        tk.Button(ventana, text="Actualizar Datos", command=self.actualizar_paciente, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=16, height=1).place(x=140, y=210)

    def ventana_eliminar_buscar(self):
        ventana2 = tk.Toplevel(self.root)
        ventana2.title("Actualizar Paciente")
        ventana2.geometry(f"{400}x{200}+{550}+{250}")
        ventana2.config(bg="black")

        tk.Label(ventana2, text="ID Paciente:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=15, height=1).place(x=50,y=60)
        self.entry_id = tk.Entry(ventana2)
        self.entry_id.place(x=200,y=60)


        tk.Button(ventana2, text="Eliminar Paciente", command=self.eliminar_doctor, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=18, height=1).place(x=25, y=105)    
        
        tk.Button(ventana2, text="Buscar Paciente", command=self.buscar_doctor, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=16, height=1).place(x=220, y=105)


    def registrar_doctor(self):
        nombre = self.entry_nombre_doctor.get()
        especialidad = self.entry_especialidad.get()
        contacto = self.entry_contacto_doctor.get()
        self.doctor.registar_doctor(nombre, especialidad, contacto)
        messagebox.showinfo("Éxito", "Doctor registrado exitosamente")
    
    def actualizar_doctor(self):
        id_paciente = self.entry_id.get()
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        contacto = self.entry_contacto.get()
        direccion = self.entry_direccion.get()
        self.paciente.actualizar_paciente(id_paciente,nombre, edad, contacto, direccion)
        messagebox.showinfo("Éxito", "Paciente actualizado exitosamente")
        self.root.destroy()
    

    def eliminar_doctor(self):
        id_paciente = self.entry_id.get()
        self.paciente.eliminar_paciente(id_paciente)
        messagebox.showinfo("Éxito", "Paciente eliminado exitosamente")

    def buscar_doctor(self):
        id_paciente = self.entry_id.get()
        paciente_data = self.paciente.buscar_paciente(id_paciente)
        
        if paciente_data:
            nombre, edad, contacto, direccion = paciente_data
            message = (f"Nombre: {nombre}\nEdad: {edad}\nContacto: {contacto}\nDirección: {direccion}")
            messagebox.showinfo("Paciente Encontrado", message)
        else:
            messagebox.showinfo("Busqueda", "No se encontró ningún paciente con ese ID.")

    def programar_cita(self):
        paciente_id = self.entry_paciente_id.get()
        doctor_id = self.entry_doctor_id.get()
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        self.crud.registrar_Cita(paciente_id, doctor_id, fecha, hora)
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
