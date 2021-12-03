###===================Funciones para crud Area=======================###

def listarArea(area):
    contador = 1
    for datos in area:
        area = "{0}. Nombre: {1}   | Creditos: {2}"
        print(area.format(contador, datos[0], datos[1]))
        contador = contador + 1

def sumArea(sumaarea):
    for datos in sumaarea:
        print(" ")
        sumaarea = "Creditos totales: {0}"
        print(sumaarea.format(datos[0]))

def pedirDatosRegistro():
    print(" ")
    print("===================================================")
    print(" ")
    nombre = input("Ingrese nombre de nuevo area: ")
    creditosCorrecto = False
    while(not creditosCorrecto):
        creditos = input("Ingrese créditos: ")
        if creditos.isnumeric():
            if (int(creditos) > 0):
                creditosCorrecto = True
                creditos = int(creditos)
            else:
                print("Los créditos deben ser mayor a 0.")
        else:
            print("Créditos incorrectos: Debe ser un número únicamente.")
    curso = (nombre, creditos)
    return curso

def pedirDatosEliminacion(areas1):
    listarArea(areas1)
    existeNombre = False
    print("=======================================")
    print("")
    NombreEliminar = input("Ingrese el nombre del Area a eliminar: ")
    print(" ")
    for cur in areas1:
        if cur[0] == NombreEliminar:
            existeNombre = True
            break
    if not existeNombre:
        NombreEliminar = ""
    return NombreEliminar

###===================Funciones para crud Tarea=======================###

def listarTarea(tarea):
    contador = 1
    for datos in tarea:
        area = "{0}. Codigo: {1} | Area: {2}  | Titulo: {3} | Fecha: {4} | Dificultad: {5} | Estado {6}"
        print(area.format(contador, datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]))
        contador = contador + 1

def pedirDatosAgregar(areas1):
    listarArea(areas1)
    print(" ")
    print("===================================================")
    print(" ")
    codigo = input("Ingrese un codigo para tarea: ")
    nombre = input("Ingrese id de un area: ")
    titulo = input("Ingrese un titulo: ")
    dificultad = input("Seleccione una dificultad(1=Facil) (2=Dificil): ")
    estado = input("Seleccione un estado (1 = Completado) (2 = Incompleto): ")
    curso = (codigo, nombre, titulo, dificultad, estado)
    return curso

def pedirDatosActualizacion(tarea1):
    listarTarea(tarea1)
    print(" ")
    print("===================================================")
    print(" ")
    codigo = input("Ingrese el codigo de tarea que desea modificar: ")
    nombre = input("Ingrese id de un area: ")
    titulo = input("Ingrese un titulo: ")
    dificultad = input("Seleccione una dificultad (1=Facil) (2=Dificil): ")
    estado = input("Seleccione un estado (1 = Completado) (2 = Incompleto): ")
    curso = (codigo, nombre, titulo, dificultad, estado)
    return curso

def pedirDatosEliminacionTA(tarea1):
    listarTarea(tarea1)
    existe = False
    print("==========================================================================")
    print("")
    tareaEliminar = input("Ingrese el codigo de la tarea a eliminar: ")
    print(" ")
    for curs in tarea1:
        if curs[0] == tareaEliminar:
            existe = True
            break
    if not existe:
        tareaEliminar = ""
    return tareaEliminar