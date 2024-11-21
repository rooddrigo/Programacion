import mysql.connector
def conectar_basedatos():
    return mysql.connector.connect(host='localhost', user='root', password='curso', database='centro_deportivo')

def mostrar_tablas():
    from prettytable import PrettyTable
    tabla_entrenadores = PrettyTable()
    return tabla_entrenadores

#La función mostrar entrenadores, seleccionara todas gracias al cursor.execute
def mostrar_entrenadores():
    conexion= conectar_basedatos()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM entrenadores')
    entrenadores = cursor.fetchall()
        #Comprobamos que existan entrenadores y los imprimimos mediante la función mostrar_tablas y un bucle for.
    if entrenadores:
        print('\n***Listado entrenadores***')
        tabla_entrenadores = mostrar_tablas()
        tabla_entrenadores.field_names = ['id_entrenador','nombre','especialidad']
        for entrenador in entrenadores:
            tabla_entrenadores.add_row(entrenador)
        print(tabla_entrenadores)
        return 
    cursor.close()
    conexion.close()

#Para añadir entrenadores, necesitamos un insert into y pedir al usuario su nombre y especialidad.

def inscribir_entrenadores():
    print('\n***Añadir entrenador***')
    try:
        conexion = conectar_basedatos()
        cursor = conexion.cursor()
        nombre = str(input('Introduzca su nombre y apellidos: ')).title()
        especialidad = str(input('Introduzca su especialidad: ')).title()
        cursor.execute('INSERT INTO entrenadores (nombre_entrenador,especialidad) VALUES (%s,%s)', (nombre,especialidad))
        conexion.commit()
        print(f'Bienvenido {nombre}')
    except:
        print('Algo ha fallado durante el registro.')
    conexion.close()
    cursor.close()


#Para actualizarlos, simplemente usaremos un update con los datos nuevos y un WHERE para localizará a dicho entrenador.

def actualizar_entrenadores():
    print('\n***Actualizar entrenadores***')
    try:
        conexion = conectar_basedatos()
        cursor = conexion.cursor()
        mostrar_entrenadores()
        identrenador = int(input('Introduce el id_entrenador para actualizarlo: '))
        nombre = str(input('Introduzca su nombre y apellidos: ')).title()
        especialidad = str(input('Introduzca su especialidad: ')).title()
        cursor.execute('UPDATE entrenadores SET nombre_entrenador = %s, especialidad = %s WHERE id_entrenador = %s', (nombre,especialidad,identrenador))
            #Comprobamos que exista el id mediante el rowcount.

        if cursor.rowcount > 0:
            conexion.commit()
            print(f'El entrenador con ID {identrenador} ha sido actualizada a {nombre}.')
            return 
        else:
            print(f'No se encontró un entrenador con ese ID.')
    except:
        print('Algo ha fallado durante la actualización')

#Por último crearemos la opción de eliminar entrenadores valiendonos de un  DELETE y un WHERE para localizar al entrenador

def eliminar_entrenadores():
    print('\n***Eliminar entrenador***')
    conexion = conectar_basedatos()
    cursor = conexion.cursor()
    identrenador = int(input('Introduce el id_entrenador para eliminarlo: '))
    cursor.execute('DELETE FROM entrenadores WHERE id_entrenador = %s',(identrenador,))

    if cursor.rowcount > 0:
        conexion.commit()
        print(f'El cliente con ID {identrenador} se ha eliminado.')
        mostrar_entrenadores()
        return 
    else:
        print(f'No se encontró un entrenador con ese ID.')
    cursor.close()
    conexion.close()


#Creamos el menú con el que manejaremos los entrenadores.

def menu_entrenadores():
    while True:
        print('\n****Menu entrenadores****')
        print('1.- Añadir entrenador')
        print('2.- Actualizar entrenadores')
        print('3.- Eliminar entrenadores')
        print('4.- Ver lista entrenadores')
        print('5.- Volver al menú principal')
        eleccion = int(input('Elige una opción: '))
        if eleccion ==1:
            inscribir_entrenadores()
        elif eleccion ==2:
           actualizar_entrenadores()
        elif eleccion ==3:
            eliminar_entrenadores()
        elif eleccion==4:
            mostrar_entrenadores()
        elif eleccion ==5:
            print('Volviendo al menú principal...')
            return
