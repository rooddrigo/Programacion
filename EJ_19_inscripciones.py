#Creamos la función por la cual nos conectaremos a la base de datos 'centro_deportivo'
import mysql.connector
def conectar_basedatos():
    return mysql.connector.connect(host='localhost', user='root', password='curso', database='centro_deportivo')
#Mediante esta función, visualizaremos articulos o clientes.
def mostrar_tablas():
    from prettytable import PrettyTable
    tabla_inscripciones = PrettyTable()
    return tabla_inscripciones

#La función mostrar inscripciones, seleccionara todas gracias al cursor.execute
def mostrar_inscripciones():
    conexion= conectar_basedatos()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM inscripciones')
    inscripciones = cursor.fetchall()
    #Comprobamos que existan inscripciones y las imprimimos mediante la función mostrar_tablas y un bucle for.
    if inscripciones:
        print('\n***Listado inscripciones***')
        tabla_inscripciones = mostrar_tablas()
        tabla_inscripciones.field_names = ['id_inscripcion','id_cliente','id_actividad'] #field_names, se refiere al nombre de las columnas.
        for inscripcion in inscripciones:
            tabla_inscripciones.add_row(inscripcion)
        print(tabla_inscripciones)
        return 
    cursor.close()
    conexion.close()
    #Cerramos la conexión.


#Para añadir inscripciones, necesitamos un insert into y pedir al usuario su idcliente y el id de la actividad.
def añadir_inscripciones():
    print('\n***Añadir inscripción***')
    try:
        conexion = conectar_basedatos()
        cursor = conexion.cursor()
        id_cliente = int(input('Introduzca su id_cliente: '))
        id_actividad= int(input('Introduzca la actividad deseada: '))
        cursor.execute('INSERT INTO inscripciones (id_cliente,id_actividad) VALUES (%s,%s)', (id_cliente,id_actividad))
        conexion.commit()
        print(f'Bienvenido cliente: {id_cliente}, se ha añadido a la actividad {id_actividad}')
        return 
    except:
        print('Algo ha fallado durante el registro.')
    conexion.close()
    cursor.close()


#Para actualizarlas, simplemente usaremos un update con los datos nuevos y un WHERE para localizara a dicha inscripción.
def actualizar_inscripciones():
    print('\n***Actualizar inscripciones***')
    try:
        conexion = conectar_basedatos()
        cursor = conexion.cursor()
        mostrar_inscripciones()
        idinscripcion = int(input('Introduce el id_inscripcion para actualizarla: '))
        id_cliente = int(input('Introduzca su id_cliente: '))
        id_actividad= int(input('Introduzca su especialidad: '))
        cursor.execute('UPDATE inscripciones SET id_cliente = %s, id_actividad = %s WHERE id_inscripcion = %s', (id_cliente,id_actividad,idinscripcion))
        #Comprobamos que exista el id mediante el rowcount.
        if cursor.rowcount > 0:
            conexion.commit()
            print(f'La inscripción con ID {idinscripcion} ha sido actualizada.')
            return 
        else:
            print(f'No se encontró una inscripcion con ese ID.')
    except:
        print('Algo ha fallado durante la actualización')

#Por último crearemos la opción de eliminar inscripciones valiendonos de un  DELETE y un WHERE para localizar la inscripción
def eliminar_inscripciones():
    print('\n***Eliminar inscripcion***')
    conexion = conectar_basedatos()
    cursor = conexion.cursor()
    idinscripcion = int(input('Introduce el id_inscripción para eliminarlo: '))
    cursor.execute('DELETE FROM inscripciones WHERE id_inscripcion = %s',(idinscripcion,))
    #De nuevo comprobamos la existencia de la inscripción.
    if cursor.rowcount > 0:
        conexion.commit()
        print(f'La inscripción {idinscripcion} se ha eliminado.')
        return 
    else:
        print(f'No se encontró una inscripción con ese ID.')
    cursor.close()
    conexion.close()

#Creamos el menú con el que manejaremos las inscripciones.

def menu_inscripciones():
    while True:
        print('\n****Menu inscripciones****')
        print('1.- Añadir inscripciones')
        print('2.- Actualizar inscripciones')
        print('3.- Eliminar inscripciones')
        print('4.- Ver lista inscripciones')
        print('5.- Volver al menú principal')
        eleccion = int(input('Elige una opción: '))
        if eleccion ==1:
            añadir_inscripciones()
        elif eleccion ==2:
           actualizar_inscripciones()
        elif eleccion ==3:
            eliminar_inscripciones()
        elif eleccion==4:
            mostrar_inscripciones()
        elif eleccion ==5:
            print('Volviendo al menú principal...')
            return 
