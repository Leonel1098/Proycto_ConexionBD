CREATE DATABASE Gestion_Citas_Medicas;
use Gestion_Citas_Medicas;

create table Paciente(
id_Paciente int primary key,
nombre_Paciente varchar(50) not null,
edad_Paciente int not null,
contacto_Paciente int not null,
direccion_Paciente varchar(50) not null,
);

select * from Paciente

create table Doctores(
id_Doctor int primary key,
nombre_Doctor varchar(50) not null,
especialidad_Doctor varchar(50) not null,
contacto_Doctor varchar(50) not null);
	
create table Citas(
id_cita int primary key identity (1,1),
id_Paciente int not null,
id_Doctor int not null,
fecha date not null,
hora time not null,
constraint fk_Citas_Paciente foreign key (id_Paciente)  references Paciente(id_Paciente),
constraint fk_Citas_Doctor foreign key (id_Doctor) references Doctores(id_Doctor)
);

drop table Citas
----Registrar Pacientes

create or alter procedure sp_Registrar_Paciente
	@id_Paciente int,
	@nombre_Paciente varchar(50),
	@edad_Paciente int,
	@contacto_Paciente int, 
	@direccion_Paciente varchar(50)
as 
begin
		begin try
			begin transaction;
				insert into Paciente values(@id_Paciente, @nombre_Paciente, @edad_Paciente, @contacto_Paciente, @direccion_Paciente);
				commit transaction;
		end try
		begin catch
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realizó un rollback de la transacción')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
	end catch
end;

---Registrar Doctores
create or alter procedure sp_Registrar_Doctores
	@id_Doctor int,
	@nombre_Doctor varchar(50),
	@especialidad_Doctor varchar (50),
	@contacto_Doctor varchar(50)
as
begin
		begin try
			begin transaction;
				insert into Doctores values(@id_Doctor, @nombre_Doctor, @especialidad_Doctor, @contacto_Doctor);
				commit transaction;
		end try
		begin catch
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realizó un rollback de la transacción')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
	end catch
end;

create or alter procedure sp_Agendar_Cita
	@id_Paciente int,
	@id_Doctor int,
	@fecha date,
	@hora time
as
begin
	if exists(select 1 from Citas where id_Doctor = @id_Doctor and fecha = @fecha and hora = @hora)
	begin
		
		raiserror('El Doctor ya tiene una cita',16,1);
		return;
	end
		insert into Citas values (@id_Paciente, @id_Doctor, @fecha,@hora);
end;

create or alter procedure sp_Mostar_Citas
as
begin
	select Citas.id_cita, Paciente.nombre_Paciente as Paciente, Doctores.nombre_Doctor as Doctor, Citas.fecha, Citas.hora from Citas
	join Paciente on Citas.id_Paciente = Paciente.id_Paciente
	join Doctores on Citas.id_Doctor = Doctores.id_Doctor;
end;

SELECT @@SERVERNAME AS ServerName;
SELECT SYSTEM_USER AS CurrentUser;

create or alter procedure sp_Historial_Citas_Pacientes
	@id_Paciente int
as
begin
	select Citas.id_cita, Doctores.nombre_Doctor as Doctor, Citas.fecha, Citas.hora from Citas
	join Doctores on Citas.id_Doctor = Doctores.id_Doctor
	where Citas.id_Paciente = @id_Paciente;
end;


SELECT * FROM sys.procedures WHERE name = 'Registrar_Paciente';
SELECT DB_NAME() AS BaseDeDatosActual;

SELECT 
    DB_NAME(dbid) AS BaseDeDatos, 
    hostname AS NombreDelHost, 
    loginame AS NombreDeUsuario, 
    status AS Estado
FROM sys.sysprocesses
WHERE dbid > 0;

SELECT 
    USER_NAME() AS UsuarioActual,
    HAS_PERMS_BY_NAME(DB_NAME(), 'DATABASE', 'EXECUTE') AS PermisoEjecutarProcedimientos;
