CREATE DATABASE Gestion_Citas_Medicas;
use Gestion_Citas_Medicas;

create table Paciente(
id_Paciente int primary key identity (1,1),
nombre_Paciente varchar(50) not null,
edad_Paciente int not null,
contacto_Paciente int not null,
direccion_Paciente varchar(50) not null,
);

create table Doctores(
id_Doctor int primary key identity (1,1),
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

----Registrar Pacientes
create or alter procedure sp_Registrar_Paciente
	@nombre_Paciente varchar(50),
	@edad_Paciente int,
	@contacto_Paciente int, 
	@direccion_Paciente varchar(50)
as 
begin
		begin try
			begin transaction;
				insert into Paciente (nombre_Paciente,edad_Paciente,contacto_Paciente,direccion_Paciente) values(@nombre_Paciente, @edad_Paciente, @contacto_Paciente, @direccion_Paciente);
				commit transaction;
		end try
		begin catch
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realiz� un rollback de la transacci�n')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
	end catch
end;

----Actualizar Pacientes
create or alter procedure sp_Actualizar_Paciente
	@id_Paciente int,
	@nombre_Paciente varchar(50),
	@edad_Paciente int,
	@contacto_Paciente int, 
	@direccion_Paciente varchar(50)
	
as
begin
	if exists (select 1 from Paciente where id_Paciente = @id_Paciente)
	begin
	update Paciente set nombre_Paciente = @nombre_Paciente, edad_Paciente = @edad_Paciente,contacto_Paciente = @contacto_Paciente,direccion_Paciente = @direccion_Paciente where id_Paciente = @id_Paciente;
	end
	else
	begin
	raiserror('El paciente con el ID proporcionado no existe.', 16, 1);
	end
end;


----Eliminar Pacientes
create or alter procedure sp_Eliminar_Paciente
    @id_Paciente int
as
begin
    declare @contador_citas int;
    select @contador_citas = count(*)
    from Citas
    where id_paciente = @id_Paciente;

    if @contador_citas > 0
    begin
        raiserror('El paciente tiene citas programadas. ¿Desea continuar con la eliminación?', 16, 1);
    end
    else
    begin
        delete from  Paciente
        where id_Paciente = @id_Paciente;
    end
end;

---Registrar Doctores
create or alter procedure sp_Registrar_Doctores
	@nombre_Doctor varchar(50),
	@especialidad_Doctor varchar (50),
	@contacto_Doctor varchar(50)
as
begin
		begin try
			begin transaction;
				insert into Doctores (nombre_Doctor,especialidad_Doctor,contacto_Doctor) values(@nombre_Doctor, @especialidad_Doctor, @contacto_Doctor);
				commit transaction;
		end try
		begin catch
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realiz� un rollback de la transacci�n')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
	end catch
end;

----Actualizar Doctores
create or alter procedure sp_Actualizar_Doctor
	@id_Doctor int,
	@nombre_Doctor varchar(50),
	@especialidad_Doctor varchar(50),
	@contacto_Doctor varchar(50) 
	
as
begin
	if exists (select 1 from Doctores where id_Doctor = @id_Doctor)
	begin
	update Doctores set nombre_Doctor = @nombre_Doctor, especialidad_Doctor = @especialidad_Doctor,contacto_Doctor = @contacto_Doctor where id_Doctor = @id_Doctor;
	end
	else
	begin
	raiserror('El Doctor con el ID proporcionado no existe.', 16, 1);
	end
end;

---Eliminar Doctores
create or alter procedure sp_Eliminar_Doctor
    @id_Doctor int
as
begin
    declare @contador_citas int;
    select @contador_citas = count(*)
    from Citas
    where id_doctor = @id_Doctor;

    if @contador_citas > 0
    begin
        raiserror('El Doctor tiene citas programadas. ¿Desea continuar con la eliminación?', 16, 1);
    end
    else
    begin
        delete from  Doctores
        where id_Doctor = @id_Doctor;
    end
end;

---Registrar Citas
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

---Actualizar Cita
create or alter procedure sp_Actualizar_Cita
	@id_cita int,
	@id_Paciente int,
	@id_Doctor int,
	@fecha date,
	@hora time
	
as
begin
	if exists (select 1 from Citas where id_cita = @id_cita)
	begin
	update Citas set id_Paciente = @id_Paciente, id_Doctor = @id_Doctor,fecha = @fecha,hora = @hora where id_cita = @id_cita;
	end
	else
	begin
	raiserror('El Doctor con el ID proporcionado no existe.', 16, 1);
	end
end;

----Eliminar Citas
CREATE OR ALTER PROCEDURE sp_Eliminar_Cita
    @id_cita INT
AS
BEGIN
    -- Eliminar la cita correspondiente al ID
    DELETE FROM Citas
    WHERE id_cita = @id_cita;
END




-----Muestra todas las citas
create or alter procedure sp_Mostar_Citas
as
begin
	select Citas.id_cita, Paciente.nombre_Paciente as Paciente, Doctores.nombre_Doctor as Doctor, Citas.fecha, Citas.hora from Citas
	join Paciente on Citas.id_Paciente = Paciente.id_Paciente
	join Doctores on Citas.id_Doctor = Doctores.id_Doctor;
end;

-----Filtrar las Citas por Paciente
CREATE OR ALTER PROCEDURE sp_Filtrar_Citas_Paciente
    @paciente VARCHAR(100)
AS
BEGIN
    SELECT Citas.id_cita, Paciente.nombre_Paciente AS Paciente, Doctores.nombre_Doctor AS Doctor, Citas.fecha, Citas.hora
    FROM Citas
    INNER JOIN Paciente ON Citas.id_Paciente = Paciente.id_Paciente
    INNER JOIN Doctores ON Citas.id_Doctor = Doctores.id_Doctor
    WHERE Paciente.nombre_Paciente = @paciente;
END;

----Filtrar las Citas por Doctor
CREATE OR ALTER PROCEDURE sp_Filtrar_Citas_Doctor
    @doctor NVARCHAR(100)
AS
BEGIN
    SELECT Citas.id_cita, Paciente.nombre_Paciente AS Paciente, Doctores.nombre_Doctor AS Doctor, Citas.fecha, Citas.hora
    FROM Citas
    INNER JOIN Paciente ON Citas.id_Paciente = Paciente.id_Paciente
    INNER JOIN Doctores ON Citas.id_Doctor = Doctores.id_Doctor
    WHERE Doctores.nombre_Doctor = @doctor;
END;

---filtrar las citas por fecha
CREATE OR ALTER PROCEDURE sp_Filtrar_Citas_Fecha
    @fecha DATE
AS
BEGIN
    SELECT Citas.id_cita, Paciente.nombre_Paciente AS Paciente, Doctores.nombre_Doctor AS Doctor, Citas.fecha, Citas.hora
    FROM Citas
    INNER JOIN Paciente ON Citas.id_Paciente = Paciente.id_Paciente
    INNER JOIN Doctores ON Citas.id_Doctor = Doctores.id_Doctor
    WHERE Citas.fecha = @fecha;
END;





---Mostrar las citas de un Paciente
create or alter procedure sp_Historial_Citas_Pacientes
	@id_Paciente int
as
begin
	select Citas.id_cita, Doctores.nombre_Doctor as Doctor, Citas.fecha, Citas.hora from Citas
	join Doctores on Citas.id_Doctor = Doctores.id_Doctor
	where Citas.id_Paciente = @id_Paciente;
end;






select * from Paciente
drop table Paciente

select * from Doctores
drop table Doctores

select * from Citas
drop table Citas


EXEC sp_Actualizar_Cita 
    @id_cita = 1, 
    @id_Paciente = 1, 
    @id_Doctor = 1, 
    @fecha = '2024-08-28', 
    @hora = '10:00:00'

EXEC sp_Mostar_Citas;

EXEC sp_Filtrar_Citas_Paciente @paciente = 'Lionel Messi'
EXEC sp_Filtrar_Citas @paciente = NULL, @doctor = 'Mario Bros', @fecha = NULL;
EXEC sp_Filtrar_Citas @paciente = NULL, @doctor = NULL, @fecha = '2024-08-27';
-- Prueba sin filtros
EXEC sp_Filtrar_Citas @paciente = NULL, @doctor = NULL, @fecha = NULL;

select * from Citas where id_Paciente = 1002

exec sp_Historial_Citas_Pacientes @id_Paciente = 1002