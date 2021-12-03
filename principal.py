import os
from BD.Conexion import DAO
import funciones


def menuPrincipal(): #funcioin principal
    print(" ")
    print("=============================================================")
    print("=            Bienvenido al gestor de Tareas Weeby           =")
    print("=============================================================")
    print(" ")
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("================== MENÚ PRINCIPAL ==================")
            print(" ")
            print("1.- Ver Areas")
            print("2.- Registrar un Nuevo Area")
            print("3.- Eliminar area")
            print(" ")
            print("4.- Listar Tareas")
            print("5.- Registrar Nueva Tarea")
            print("6.- Actualizar Tarea")
            print("7.- Eliminar Tarea")
            print(" ")
            print("8.- Salir")
            print(" ")
            print("=====================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 8:
                os.system('cls')
                print(" ")
                print("     Opción incorrecta, ingrese nuevamente...")
                print(" ")
            elif opcion == 8:
                continuar = False
                os.system('cls')
                print(" ")
                print("¡Gracias por usar este sistema!")
                print(" ")
                break
            else:
                continuar = True
                os.system('cls')
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()
    #================crud para cursos=================================#
    if opcion == 1: #mostrar areas
        try:
            print("=======================================")
            print("              Mis Áreas                ")
            print("=======================================") 
            area = dao.listarAreas()
            sumaarea= dao.sumarCreditos()
            if len(area) > 0:
                funciones.listarArea(area)
                funciones.sumArea(sumaarea)
                print("=======================================")
                print(" ")
            else:
                print("No se encontraron áreas...")###
        except: 
            print("Ocurrió un error...")
    elif opcion == 2:#Registrar areas
        area = funciones.pedirDatosRegistro()
        try:
            dao.AgregarAreas(area)
            print("=======================================")
            print(" ")
        except:
            print("Ocurrió un error...")
    elif opcion == 3:#Eliminnar areas
        try:
            print("=======================================")
            print("              Mis Áreas                ")
            print("=======================================") 
            areas1 = dao.listarAreas()
            if len(areas1) > 0:
                NombreEliminar = funciones.pedirDatosEliminacion(areas1)
                if not(NombreEliminar == ""):
                    dao.eliminarAreas(NombreEliminar)
                else:
                    print("Nombre de área no encontrado...\n")
            else:
                print("No se encontraron áreas...")
        except:
            print("Ocurrió un error...")

     #======================crud para tareas============================
    elif opcion == 4:#Listar tareas
        try:
            print("==========================================================================")
            print("                                  Mis Tareas                    ")
            print("==========================================================================") 
            tarea = dao.listarTareas()
            if len(tarea) > 0:
                funciones.listarTarea(tarea)
                print("==========================================================================")
                print(" ")
            else:
                print("No se encontraron tareas...")
        except: 
            print("Ocurrió un error...")
    elif opcion == 5:#agregar tareas
        try:
            print("===================================================")
            print("                      Mis Áreas                    ")
            print("===================================================") 
            area1 = dao.listarAreas()
            if len(area1) > 0:
                curso = funciones.pedirDatosAgregar(area1)
                if curso:
                    print("===================================================")
                    dao.AgregarTareas(curso)
                else:
                    print("Código de curso a actualizar no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    elif opcion == 6:#actualizar tareas
        try:
            print("===================================================")
            print("                  Lista de Áreas                    ")
            print("===================================================") 
            area1= dao.listarAreas()
            if len(area1) > 0:
                area = funciones.listarArea(area1)
                print("==========================================================================")
                print("                           Lista de Tareas                    ")
                print("==========================================================================")
                tarea1 = dao.listarTareas()
                if len(tarea1) > 0:
                    tarea = funciones.pedirDatosActualizacion(tarea1)
                    if tarea:
                        dao.actualizarTareas(tarea)
                else:
                    print("Código de curso a actualizar no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    elif opcion == 7:#Eliminar tareas
        print("==========================================================================")
        print("                              Mis Tareas                                  ")
        print("==========================================================================") 
        tarea1 = dao.listarTareas()
        if len(tarea1) > 0:
            tareaEliminar = funciones.pedirDatosEliminacionTA(tarea1)
            if not(tareaEliminar == ""):
                dao.eliminarTarea(tareaEliminar)
            else:
                print("id de tarea no encontrado...\n")
        else:
            print("No se encontraron tareas...")
    else:
        print("Opción no válida...")


menuPrincipal()