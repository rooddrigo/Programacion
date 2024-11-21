import mysql.connector
def conectar_basedatos():
    return mysql.connector.connect(host='localhost', user='root', password='curso', database='centro_deportivo')

def mostrar_tablas():
    from prettytable import PrettyTable
    tabla_entrenadores = PrettyTable()
    return tabla_entrenadores

#La función mostrar actividades, seleccionara todas gracias al cursor.execute

def mostrar_actividades():
    conexion= conectar_basedatos()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM actividades')
    actividades = cursor.fetchall()
        #Comprobamos que existan clientes y los imprimimos mediante la función mostrar_tablas y un bucle for.

    if actividades:
        print('\n***Listado actividades***')
        tabla_actividades = mostrar_tablas()
        tabla_actividades.field_names = ['id_actividad','nombre_actividad','horario','duracion','id_entrenador']
        for actividad in actividades:
            tabla_actividades.add_row(actividad)
        print(tabla_actividades)
        return 
    cursor.close()
    conexion.close()

#Para añadir actividades, necesitamos un insert into y pedir al usuario el nombre y datos de la actividad.

def crear_actividades():
    print('\n***Añadir actividad***')
    try:
        conexion = conectar_basedatos()
        cursor = conexion.cursor()
        nombre = str(input('Introduzca el nombre de la actividad: ')).title()
        horario = input('Introduzca el horario: ').title()
        duracion = int(input(f'Introduzca la duración de una clase de {nombre}: '))
        from EJ_19_entrenadores import mostrar_entrenadores
        mostrar_tabla_entrenadores = mostrar_entrenadores()
        print(mostrar_tabla_entrenadores)
        entrenador= int(input('Introduzca el id del entrandor que dará la clase: '))
        cursor.execute('INSERT INTO actividades (nombre_actividad,horario,duracion,id_entrenador) VALUES (%s,%s,%s,%s)', (nombre,horario,duracion,entrenador))
        conexion.commit()
        print(f'Se ha creado la actividad {nombre}')
        return 
    except:
        print('Algo ha fallado durante el registro.')
    conexion.close()
    cursor.close()

#Para actualizarlos, simplemente usaremos un update con los datos nuevos y un WHERE para localizará a dicha actividad.


def actualizar_actividades():
    print('\n***Actualizar actividades***')
    try:
        conexion = conectar_basedatos()
        cursor = conexion.cursor()
        mostrar_actividades()
        idactividad = int(input('Introduce el id_actividad para actualizarlo: '))
        nombre = str(input('Introduzca el nombre de la actividad: ')).title()
        horario = input('Introduzca el horario: ').title()
        duracion = int(input(f'Introduzca la duración de una clase de {nombre}: '))
        from EJ_19_entrenadores import mostrar_entrenadores
        mostrar_tabla_entrenadores = mostrar_entrenadores()
        print(mostrar_tabla_entrenadores)
        entrenador = int(input('Introduzca el id del entrandor que dará la clase: '))
        cursor.execute('UPDATE actividades SET nombre_actividad = %s, horario = %s, duracion = %s, id_entrenador = %s WHERE id_actividad = %s', (nombre,horario,duracion,entrenador,idactividad))
        if cursor.rowcount > 0:
            conexion.commit()
            print(f'La actividad con ID {idactividad} ha sido actualizada a {nombre}.')
            return 
        else:
            print(f'No se encontró un a actividad con ese ID.')
    except:
        print('Algo ha fallado durante la actualización')

#Por último crearemos la opción de eliminar actividades valiendonos de un  DELETE y un WHERE para localizar la actividad

def eliminar_actividades():
    print('\n***Eliminar actividad***')
    conexion = conectar_basedatos()
    cursor = conexion.cursor()
    idactividad = int(input('Introduce el id_actividad para eliminarla: '))
    cursor.execute('DELETE FROM inscripciones WHERE id_actividad= %s',(idactividad,))
    if cursor.rowcount > 0:
        conexion.commit()
    cursor.execute('DELETE FROM actividades WHERE id_actividad= %s',(idactividad,))
    if cursor.rowcount > 0:
        conexion.commit()
        print(f'La actividad con ID {idactividad} se ha eliminado.')
        mostrar_actividades()
        return 
    else:
        print(f'No se encontró una actividad con ese ID.')
    cursor.close()
    conexion.close()

#Creamos el menú con el que manejaremos las actividades.

def menu_actividades():
    while True:
        print('\n****Menu actividades****')
        print('1.- Añadir actividad')
        print('2.- Actualizar actividad')
        print('3.- Eliminar actividad')
        print('4.- Ver lista actividades')
        print('5.- Volver al menú principal')
        eleccion = int(input('Elige una opción: '))
        if eleccion ==1:
            crear_actividades()
        elif eleccion ==2:
           actualizar_actividades()
        elif eleccion ==3:
            eliminar_actividades()
        elif eleccion==4:
            mostrar_actividades()
        elif eleccion ==5:
            print('Volviendo al menú principal...')
            return
