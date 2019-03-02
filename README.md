# MLCiencias_2019_2

La primera tarea es clonar el repositorio de Github(ya subí las instrucciones) e instalar anaconda continuum, para ello deben de darse de alta en la página creando un usuario con contraseña.

Al rato seguiremos con formatos y protocolos(ya arreglé los problemas técnicos), si tienen RIU por favor recuerden sus credenciales. Vayan descargando postgres 10 y si pueden instalenlo. Completaremos con todo detalle el ejercicio de ayer y también lo haremos para usuarios mac-os. Dudas y comentarios con toda confianza me pueden escribir a mi correo.

Hay TAREA 1

sql="""
create table delitos2(
id serial primary key,
anio integer default null,
mes integer default null,
fechainicio timestamp default null,
alcaldia varchar(100) default null,
catdelito varchar(100) default null,
delito varchar(100) default null,
catdelitoibn varchar(100) default null,
delitoibn varchar(100) default null,
agencia varchar(100) default null,
uinvestigacion varchar(100) default null,
fiscalia varchar(100) default null,
calle varchar(100) default null,
colonia varchar(100) default null,
latitud real  not null,
longitud real not null,
peso real default null,
edad real default null,
estatura real default null
);
"""
