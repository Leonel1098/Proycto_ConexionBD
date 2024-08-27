CREATE DATABASE Gestion_Citas_Medicas;
use Gestion_Citas_Medicas;

create table Paciente(
id_Paciente int primary key identity (1,1),
nombre_Paciente varchar(50) not null,
edad_Paciente int not null,
contacto_Paciente int not null,
direccion_Paciente varchar(50) not null,
);

select * from Paciente
drop table Paciente


create table Doctores(
id_Doctor int primary key identity (1,1),
nombre_Doctor varchar(50) not null,
especialidad_Doctor varchar(50) not null,
contacto_Doctor varchar(50) not null);

select * from Doctores
drop table Doctores



create table Citas(
id_cita int primary key identity (1,1),
id_Paciente int not null,
id_Doctor int not null,
fecha date not null,
hora time not null,
constraint fk_Citas_Paciente foreign key (id_Paciente)  references Paciente(id_Paciente),
constraint fk_Citas_Doctor foreign key (id_Doctor) references Doctores(id_Doctor)
);

select * from Citas
drop table Citas

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
				insert into Paciente values(@nombre_Paciente, @edad_Paciente, @contacto_Paciente, @direccion_Paciente);
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
				insert into Doctores values(@nombre_Doctor, @especialidad_Doctor, @contacto_Doctor);
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

create or alter procedure sp_Mostar_Citas
as
begin
	select Citas.id_cita, Paciente.nombre_Paciente as Paciente, Doctores.nombre_Doctor as Doctor, Citas.fecha, Citas.hora from Citas
	join Paciente on Citas.id_Paciente = Paciente.id_Paciente
	join Doctores on Citas.id_Doctor = Doctores.id_Doctor;
end;

---Mostrar las citas de un Paciente
create or alter procedure sp_Historial_Citas_Pacientes
	@id_Paciente int
as
begin
	select Citas.id_cita, Doctores.nombre_Doctor as Doctor, Citas.fecha, Citas.hora from Citas
	join Doctores on Citas.id_Doctor = Doctores.id_Doctor
	where Citas.id_Paciente = @id_Paciente;
end;






