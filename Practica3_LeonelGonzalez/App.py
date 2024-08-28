import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk, messagebox
from CRUD import CRUD
from database import BaseDeDatos
from Paciente import Paciente
from Doctor import Doctor
from Cita import Cita

class App:
    #Se crea la ventana principal y las instancias de las clases importadas
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
        
        tk.Button(self.frame_Principal, text="Gestionar Citas",command= self.ventana_Registrar_Cita,bg="gray", fg="black",
                  font=("Courier New", 14, "bold","italic"),width=20, height=1).grid(row=2, column=0, pady=10)
        
        tk.Button(self.frame_Principal, text="Historial Pacientes",command=self.ventana_Historial_Paciente,bg="gray", fg="black",
                  font=("Courier New", 14, "bold","italic"),width=20, height=1).grid(row=3, column=0, pady=10)

    def ventana_Registrar_Paciente(self):
        ventana_paciente = tk.Toplevel(self.root)
        Ventana_Pacientes(ventana_paciente, self.paciente)

    def ventana_Registar_Doctor(self):
        ventana_doctor = tk.Toplevel(self.root)
        Ventana_Doctores(ventana_doctor, self.doctor)

    def ventana_Registrar_Cita(self):
        ventana_cita = tk.Toplevel(self.root)
        Ventana_Citas(ventana_cita, self.cita)

    def ventana_Historial_Paciente(self):
        ventana_historial = tk.Toplevel(self.root)
        Ventana_Historial(ventana_historial, self.paciente)

#Aqui se crea la ventana que muestra el historial de citas al hacer la busqueda por el id del paciente
class Ventana_Historial:
    def __init__(self, root, paciente):
        self.root = root
        self.root.title("Historial de Citas por ID de Paciente")
        self.root.geometry("1010x400+250+200")
        self.root.config(bg = "black")
        self.paciente = paciente
        tk.Button(self.root, text="Mostrar Historial de Citas", command=self.ventana_historial).pack(pady=20)

    #Se crean los componentes que lleva la ventan, como el treeview que sirve para mostrar los datos
    def ventana_historial(self):

        # Frame para ingresar el ID del paciente
        self.historial_frame = tk.Frame(self.root, bg="black")
        self.historial_frame.pack(padx=10, pady=10, fill="x")

        tk.Label(self.historial_frame, text="ID del Paciente:", bg="black", fg="white").grid(row=0, column=0, padx=5, pady=5)
        self.entry_id_paciente = tk.Entry(self.historial_frame)
        self.entry_id_paciente.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.historial_frame, text="Buscar Historial", command=self.buscar_historial).grid(row=0, column=2, padx=5, pady=5)

        # Frame para el Treeview
        self.treeview_frame = tk.Frame(self.root)
        self.treeview_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Treeview para mostrar el historial de citas
        self.treeview = ttk.Treeview(self.treeview_frame, columns=("ID_CITA", "Doctor", "Fecha", "Hora"), show="headings")
        self.treeview.heading("ID_CITA", text="ID_CITA")
        self.treeview.heading("Doctor", text="Doctor")
        self.treeview.heading("Fecha", text="Fecha")
        self.treeview.heading("Hora", text="Hora")

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.treeview_frame, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)

        # Colocar Treeview y Scrollbar en el grid
        self.treeview.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Configurar el grid para el Treeview
        self.treeview_frame.grid_rowconfigure(0, weight=1)
        self.treeview_frame.grid_columnconfigure(0, weight=1)

    #En este metodo se crea la funcionalidad para agregar los datos al treeview 
    def buscar_historial(self):
        #Recibe el dato ingresado
        id_paciente = self.entry_id_paciente.get()
        #Valida que se haya ingresado un dato
        if not id_paciente:
            messagebox.showwarning("Advertencia", "Por favor, ingrese el ID del paciente.")
            return
        try:
            # Obtener el historial de citas desde la base de datos
            citas = self.paciente.historial_pacientes(id_paciente)
            
            # Limpiar el Treeview antes de cargar nuevas citas
            for row in self.treeview.get_children():
                self.treeview.delete(row)

            # Verifica si se obtuvieron citas y si no está vacío
            if citas:
                for cita in citas:
                    self.treeview.insert("", "end", values=(cita[0], cita[1], cita[2].strftime('%d-%m-%Y'), cita[3].strftime('%H:%M')))
            else:
                messagebox.showinfo("Información", "No se encontraron citas para el ID del paciente ingresado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener datos: {e}")

#Aqui se crean todas las ventanas que se utilizan para la gestion de los pacientes
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
        ventana2.title("Eliminar Paciente")
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

    
    #Aqui van los metodos utilizados para las funcionalidades de las ventanas y gestionar los datos con la base de datos
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

    def buscar_paciente(self):
        id_paciente = self.entry_id.get()
        paciente_data = self.paciente.buscar_paciente(id_paciente)
        
        if paciente_data:
            nombre, edad, contacto, direccion = paciente_data
            message = (f"Nombre: {nombre}\nEdad: {edad}\nContacto: {contacto}\nDirección: {direccion}")
            messagebox.showinfo("Paciente Encontrado", message)
        else:
            messagebox.showinfo("Busqueda", "No se encontró ningún paciente con ese ID.")

#Aqui se crean todas las ventanas que se utilizan para la gestion de los doctores
class Ventana_Doctores:

    def __init__(self, root, doctor):
        self.root = root
        self.root.title("Registrar Doctor")
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
        
        tk.Button(self.root, text="Más Opciones", command=self.ventana_eliminar_buscar, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=15, height=1).place(x=220, y=220)
        
        tk.Button(self.root, text="Actualizar", command=self.ventana_actualizar, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=220)

    def ventana_actualizar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Actualizar Doctor")
        ventana.geometry(f"{400}x{280}+{550}+{200}")
        ventana.config(bg="black")

        tk.Label(ventana, text="ID Doctor:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=12, height=1).place(x=75,y=35)
        self.entry_id = tk.Entry(ventana)
        self.entry_id.place(x=200,y=35)

        tk.Label(ventana, text="Nombre:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90,y=60)
        self.entry_nombre = tk.Entry(ventana)
        self.entry_nombre.place(x=200,y=60)

        tk.Label(ventana, text="Especialidad:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=15, height=1).place(x=50,y=85)
        self.entry_especialidad = tk.Entry(ventana)
        self.entry_especialidad.place(x=200,y=85)

        tk.Label(ventana, text="Contacto:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=110)
        self.entry_contacto = tk.Entry(ventana)
        self.entry_contacto.place(x=200, y=110)

        tk.Button(ventana, text="Actualizar Datos", command=self.actualizar_doctor, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=16, height=1).place(x=140, y=210)

    def ventana_eliminar_buscar(self):
        ventana2 = tk.Toplevel(self.root)
        ventana2.title("Eliminar Doctor")
        ventana2.geometry(f"{400}x{200}+{550}+{250}")
        ventana2.config(bg="black")

        tk.Label(ventana2, text="ID Doctor:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=15, height=1).place(x=50,y=60)
        self.entry_id = tk.Entry(ventana2)
        self.entry_id.place(x=200,y=60)


        tk.Button(ventana2, text="Eliminar Doctor ", command=self.eliminar_doctor, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=18, height=1).place(x=25, y=105)    
        
        tk.Button(ventana2, text="Buscar Doctor", command=self.buscar_doctor, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=16, height=1).place(x=220, y=105)

    #Aqui van los metodos utilizados para las funcionalidades de las ventanas y gestionar los datos con la base de datos
    def registrar_doctor(self):
        nombre = self.entry_nombre_doctor.get()
        especialidad = self.entry_especialidad.get()
        contacto = self.entry_contacto_doctor.get()
        self.doctor.registrar_doctor(nombre, especialidad, contacto)
        messagebox.showinfo("Éxito", "Doctor registrado exitosamente")
    
    def actualizar_doctor(self):
        id_doctor = self.entry_id.get()
        nombre = self.entry_nombre.get()
        especialidad = self.entry_especialidad.get()
        contacto = self.entry_contacto.get()
        self.doctor.actualizar_doctor(id_doctor,nombre, especialidad, contacto)
        messagebox.showinfo("Éxito", "Doctor actualizado exitosamente")
        self.root.destroy()
    

    def eliminar_doctor(self):
        id_doctor = self.entry_id.get()
        self.doctor.eliminar_doctor(id_doctor)

    def buscar_doctor(self):
        id_doctor = self.entry_id.get()
        doctor_data = self.doctor.buscar_doctor(id_doctor)
        #Se valida que el id ingresado exista en la base de datos
        if doctor_data:
            nombre, especialidad, contacto = doctor_data
            message = (f"Nombre: {nombre}\nEspecialidad: {especialidad}\nContacto: {contacto}")
            messagebox.showinfo("Doctor Encontrado", message)
        else:
            messagebox.showinfo("Busqueda", "No se encontró ningún doctor con ese ID.")


#En esta clase tenemos todos los metodos para crear las ventanas y las funiones para manejar las citas de la base de datos
class Ventana_Citas:
    def __init__(self, root, cita):
        self.root = root
        self.root.title("Registrar Cita")
        self.root.geometry(f"{400}x{280}+{550}+{200}")
        self.root.config(bg = "black")
        self.cita = cita
        self.agregar_componentes()

    def agregar_componentes(self):

        tk.Label(self.root, text="ID Paciente:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=12, height=1).place(x=70,y=35)
        self.entry_id_paciente = tk.Entry(self.root)
        self.entry_id_paciente.place(x=200,y=35)
        
        tk.Label(self.root, text="ID Doctor:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90,y=60)
        self.entry_id_doctor = tk.Entry(self.root)
        self.entry_id_doctor.place(x=200,y=60)

        tk.Label(self.root, text="Fecha:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=85)
        self.fecha_entry = DateEntry(self.root, date_pattern='YYYY-MM-DD',width=17)
        self.fecha_entry.place(x=200, y=85)

        tk.Label(self.root, text="Hora:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=110)
        
        horas = self.reloj()
        self.combobox_hora = ttk.Combobox(self.root, values=horas,width=17)
        self.combobox_hora.place(x=200, y=110)
        self.combobox_hora.current(0)

        tk.Button(self.root, text="Registrar", command=self.programar_cita, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=200, y=140)
        
        tk.Button(self.root, text="Mas Opciones", command=self.ventana_eliminar_buscar, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=15, height=1).place(x=220, y=220)
        
        tk.Button(self.root, text="Actualizar", command=self.ventana_actualizar, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=220)

    def ventana_actualizar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Actualizar Cita")
        ventana.geometry(f"{400}x{280}+{550}+{200}")
        ventana.config(bg="black")

        tk.Label(ventana, text="ID Cita:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=12, height=1).place(x=90,y=35)
        self.entry_id = tk.Entry(ventana)
        self.entry_id.place(x=200,y=35)

        tk.Label(ventana, text="ID Paciente:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=12, height=1).place(x=70,y=60)
        self.entry_id_paciente = tk.Entry(ventana)
        self.entry_id_paciente.place(x=200,y=60)
        
        tk.Label(ventana, text="ID Doctor:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90,y=85)
        self.entry_id_doctor = tk.Entry(ventana)
        self.entry_id_doctor.place(x=200,y=85)


        tk.Label(ventana, text="Fecha:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=110)
        self.fecha_entry = DateEntry(ventana, date_pattern='YYYY-MM-DD', width=17)
        self.fecha_entry.place(x=200, y=110)

        tk.Label(ventana, text="Hora:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=10, height=1).place(x=90, y=135)
        horas = self.reloj()
        self.combobox_hora = ttk.Combobox(ventana, values=horas,width=17)
        self.combobox_hora.place(x=200, y=135)
        self.combobox_hora.current(0)

        tk.Button(ventana, text="Actualizar Datos", command=self.actualizar_cita, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=16, height=1).place(x=140, y=210)

    def ventana_eliminar_buscar(self):
        ventana2 = tk.Toplevel(self.root)
        ventana2.title("Eliminar Cita")
        ventana2.geometry(f"{400}x{200}+{550}+{250}")
        ventana2.config(bg="black")

        tk.Label(ventana2, text="ID Cita:",bg="black", fg="white",
                 font=("Courier New", 12, "bold","italic"), width=15, height=1).place(x=50,y=60)
        self.entry_id_cita = tk.Entry(ventana2)
        self.entry_id_cita.place(x=200,y=60)


        tk.Button(ventana2, text="Eliminar Cita", command=self.eliminar_cita, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=18, height=1).place(x=25, y=105)   
        
        tk.Button(ventana2, text="Mostrar Citas", command=self.ventana_mostrar_citas, bg="gray", fg="black",
                  font=("Courier New", 12, "bold","italic"), width=16, height=1).place(x=220, y=105)


    def ventana_mostrar_citas(self):
        self.ventana3 = tk.Toplevel(self.root)
        self.ventana3.title("Filtrar Citas")
        self.ventana3.geometry("1080x400+100+250")
        self.ventana3.config(bg="black")

        # Frame para los filtros
        self.filtros_frame = tk.Frame(self.ventana3, bg="black")
        self.filtros_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Filtros
        tk.Label(self.filtros_frame, text="Filtrar por Paciente:", bg="black", fg="white").grid(row=0, column=0, padx=5, pady=5)
        self.entry_paciente = tk.Entry(self.filtros_frame)
        self.entry_paciente.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.filtros_frame, text="Filtrar por Doctor:", bg="black", fg="white").grid(row=0, column=2, padx=5, pady=5)
        self.entry_doctor = tk.Entry(self.filtros_frame)
        self.entry_doctor.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.filtros_frame, text="Filtrar por Fecha:", bg="black", fg="white").grid(row=0, column=4, padx=5, pady=5)
        self.entry_fecha = tk.Entry(self.filtros_frame)
        self.entry_fecha.grid(row=0, column=5, padx=5, pady=5)

        tk.Button(self.filtros_frame, text="Filtrar", command=self.filtrar_citas).grid(row=0, column=6, padx=5, pady=5)

        # Frame para el Treeview
        self.treeview_frame = tk.Frame(self.ventana3)
        self.treeview_frame.grid(row=1, column=0, sticky="nsew")

        # Configurar el grid del Frame para que el Treeview se expanda
        self.treeview_frame.grid_rowconfigure(0, weight=1)
        self.treeview_frame.grid_columnconfigure(0, weight=1)
        self.treeview_frame.grid_columnconfigure(1, weight=0)

        # Treeview para mostrar citas
        self.treeview = ttk.Treeview(self.treeview_frame, columns=("ID", "Paciente", "Doctor", "Fecha", "Hora"), show="headings")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Paciente", text="Paciente")
        self.treeview.heading("Doctor", text="Doctor")
        self.treeview.heading("Fecha", text="Fecha")
        self.treeview.heading("Hora", text="Hora")

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.treeview_frame, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)

        # Colocar Treeview y Scrollbar en el grid
        self.treeview.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Configurar el grid para el Treeview
        self.treeview_frame.grid_rowconfigure(0, weight=1)
        self.treeview_frame.grid_columnconfigure(0, weight=1)

        self.cargar_citas()

    #Aqui van los metodos utilizados para las funcionalidades de las ventanas y gestionar los datos con la base de datos
    horas=[]
    def reloj(self):
            horas = []
            for hora in range(8, 17): 
                for minuto in (0, 30):  
                    horas.append(f"{hora:02d}:{minuto:02d}")
            return horas
    
    def programar_cita(self):
        paciente_id = self.entry_id_paciente.get()
        doctor_id = self.entry_id_doctor.get()
        fecha = self.fecha_entry.get()
        hora = self.combobox_hora.get()
        self.cita.registrar_cita(paciente_id, doctor_id, fecha, hora)
        messagebox.showinfo("Éxito", "Cita programada exitosamente")

    def eliminar_cita(self):
        id_cita = self.entry_id_cita.get()
        self.cita.eliminar_cita(id_cita)
        messagebox.showinfo("Éxito", "Cita eliminada exitosamente.")

    def actualizar_cita(self):
        id_cita = self.entry_id.get()
        id_paciente = self.entry_id_paciente.get()
        id_doctor = self.entry_id_doctor.get()
        fecha = self.fecha_entry.get_date()
        hora = self.combobox_hora.get()
        hora_formateada = f"{hora}:00"
        print(hora_formateada)
        self.cita.actualizar_cita(int(id_cita),int(id_paciente),int(id_doctor),fecha, hora_formateada)
        messagebox.showinfo("Éxito", "Cita actualizada exitosamente")
        self.root.destroy()

    #Con este metodo cargamos las citas al treeview para que las muestre
    def cargar_citas(self):
        # Limpiar el Treeview antes de cargar nuevas citas
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Obtener las citas desde la base de datos
        citas = self.cita.visualizar_citas()

        # Verifica si se obtuvieron citas y si no está vacío
        if citas and len(citas) > 0:
            for cita in citas:
                print(cita)  # Verifica cada cita que se inserta
                # Inserta la cita en el Treeview
                self.treeview.insert("", "end", values=(cita[0], cita[1], cita[2], cita[3].strftime('%d-%m-%Y'), cita[4].strftime('%H:%M')))
        else:
            messagebox.showinfo("Información", "No hay citas para mostrar.")

    #En este metodo se validadn los datos ingresados y dependiendo el dato se buscan 
    # las citas en la base de datos que concuerdan con los datos ingresados
    def filtrar_citas(self):
        paciente = self.entry_paciente.get()
        doctor = self.entry_doctor.get()
        fecha = self.entry_fecha.get()

        citas_filtradas = []

        if paciente:
            citas_filtradas = self.cita.filtrar_citas_paciente(paciente)
            print(type(paciente))
            print("paciente", paciente)
        elif doctor:
            citas_filtradas = self.cita.filtrar_citas_doctor(doctor)
        elif fecha:
            citas_filtradas = self.cita.filtrar_citas_fecha(fecha)
        else:
            # Mostrar mensaje de advertencia si no se especifica ningún filtro
            messagebox.showwarning("Advertencia", "Debe ingresar al menos un filtro.")

        # Limpiar el Treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Cargar citas filtradas
        if citas_filtradas:
            for cita in citas_filtradas:
                self.treeview.insert("", tk.END, values=(cita[0], cita[1], cita[2], cita[3].strftime('%d-%m-%Y'), cita[4].strftime('%H:%M')))
        else:
            messagebox.showinfo("Información", "No se encontraron citas con los filtros especificados.")







if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
