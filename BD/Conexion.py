import mysql.connector
from mysql.connector import Error


class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='BD_gesTarea'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    ###======================procedimientos para crud Area==================================       
    def listarAreas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('mostrarAreas')
                for result in cursor.stored_results():
                    resultado = result.fetchall()
                    return resultado
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def sumarCreditos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT SUM(creditos) FROM area")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def AgregarAreas(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO area (n_area, creditos) VALUES ('{0}', {1})"
                cursor.execute(sql.format(curso[0], curso[1]))
                self.conexion.commit()
                print(" ")
                print("¡Área registrada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarAreas(self, NombreAreaEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM area WHERE n_area = '{0}'"
                cursor.execute(sql.format(NombreAreaEliminar))
                self.conexion.commit()
                print("¡Area eliminada!\n")
                print(" ")
                print("=======================================")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    ###======================procedimientos y funciones para crud Area================================== 

    def listarTareas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('mostrarTareas')
                for result in cursor.stored_results():
                    resultado = result.fetchall()
                    return resultado
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))  

    def AgregarTareas(self, tarea):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO tarea (codigo,area_fk,titulo,dificultad_fk,estado_fk) VALUES ('{0}',{1},'{2}',{3},{4})"
                cursor.execute(sql.format(tarea[0], tarea[1], tarea[2], tarea[3], tarea[4]))
                self.conexion.commit()
                print(" ")
                print("¡Tarea Agregada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex)) 

    def actualizarTareas(self, tarea):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE tarea SET area_fk = {0},titulo='{1}', dificultad_fk = {2}, estado_fk = {3} WHERE codigo='{4}'"
                cursor.execute(sql.format(tarea[1], tarea[2], tarea[3], tarea[4], tarea[0]))
                self.conexion.commit()
                print(" ")
                print("¡Tarea actualizada!\n")
                print("==========================================================================\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarTarea(self, NombreTareaEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM tarea WHERE codigo = '{0}'"
                cursor.execute(sql.format(NombreTareaEliminar))
                self.conexion.commit()
                print("¡Tarea eliminada!\n")
                print(" ")
                print("=======================================")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
