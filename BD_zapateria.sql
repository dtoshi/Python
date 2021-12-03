DROP DATABASE BD_gesTarea;
CREATE DATABASE BD_gesTarea;
use BD_gesTarea;

CREATE TABLE usuario(
    id int AUTO_INCREMENT,
    nombre varchar (50),
    apellido varchar(50),
    direccion varchar(50),
    email varchar(50),
    user varchar(50),
    pass varchar(50),
    PRIMARY KEY (id)
);

insert into usuario values (1,"Angie","Ortiz","Coltauco", "angie@hotmail.com", "angie", "123");

CREATE TABLE dificultad(
    id int AUTO_INCREMENT,
    nivel varchar (10),
    PRIMARY KEY (id)
);
insert into dificultad values (1, "Facil"),(2, "Dificil");

CREATE TABLE estado(
    id int AUTO_INCREMENT,
    n_estado varchar (10),
    PRIMARY KEY (id)
);
insert into estado values (1, "Completado"),(2, "Imcompleto");

CREATE TABLE area(
    id int AUTO_INCREMENT,
    n_area varchar (20),
    creditos int,
    PRIMARY KEY (id)
);
insert into area values (1, "Matematica",20),(2, "Biologia", 20),(3, "Lenguaje", 50),(4, "Ingles", 15);

CREATE TABLE tarea(
    id int AUTO_INCREMENT,
    codigo varchar(20),
    area_fk int,
    titulo varchar (50),
    fecha DATETIME,
    dificultad_fk int,
    estado_fk int,

    PRIMARY KEY (id),
    FOREIGN KEY (area_fk) REFERENCES area(id),
    FOREIGN KEY (dificultad_fk) REFERENCES dificultad(id),
    FOREIGN KEY (estado_fk) REFERENCES estado(id)
);


/*                       id,codigo, area, titulo,    fecha,              d,pr,estd,    comen,   */
insert into tarea values (1,"bio01", 2, "La Celula",'2015-01-01 10:10:10', 1, 1),
                        (2,"ing01", 4, "Verb Tobe",'2018-08-01 20:30:11', 2, 2);



/*Procedure par listar area*/
DROP PROCEDURE IF EXISTS mostrarAreas;
CREATE PROCEDURE mostrarAreas()
SELECT n_area, creditos
FROM area ORDER BY id ASC;

CALL mostrarAreas;

/* funcion SUM*/
SELECT SUM(creditos) AS 'Creditos totales' FROM area;

/* Procedimiento con innerjoin para listar tareas*/
DROP PROCEDURE IF EXISTS mostrarTareas;
CREATE PROCEDURE mostrarTareas()
SELECT  codigo, area.n_area, titulo, fecha, dificultad.nivel, estado.n_estado
FROM tarea 
JOIN area on tarea.area_fk = area.id
inner JOIN dificultad on tarea.dificultad_fk = dificultad.id
            inner JOIN estado on tarea.estado_fk = estado.id
ORDER BY tarea.id ASC;

CALL mostrarTareas;

/*tigger para udadate*/
DROP TRIGGER up_fechaTarea;

CREATE TRIGGER up_fechaTarea
BEFORE UPDATE ON tarea FOR EACH ROW 
    SET NEW.fecha = NOW();


/*FUNCTION ver detalle tareas*/
DROP FUNCTION IF EXISTS detalletarea;
CREATE FUNCTION detalletarea(titulo_in varchar(30))
   RETURNS varchar(250)
   RETURN (
            select CONCAT(area.n_area," / ",titulo," / ",dificultad.nivel," / ",estado.n_estado," / ",fecha)
            from tarea 
            inner JOIN area on tarea.area_fk = area.id
            inner JOIN dificultad on tarea.dificultad_fk = dificultad.id
            inner JOIN estado on tarea.estado_fk = estado.id
            where titulo= titulo_in);
    
select detalletarea('La Celula') as 'Detalle de Tarea' ;

