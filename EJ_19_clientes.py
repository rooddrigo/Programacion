import mysql.connector
def conectar_basedatos():
    return mysql.connector.connect(host='localhost', user='root', password='curso', database='centro_deportivo')

def mostrar_tablas():
    from prettytable import PrettyTable
    tabla_clientes = PrettyTable()
    return tabla_clientes

#La función mostrar clientes, seleccionara todas gracias al cursor.execute

def mostrar_clientes():
    conexion= conectar_basedatos()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    #Comprobamos que existan clientes y los imprimimos mediante la función mostrar_tablas y un bucle for.

    if clientes:
        print('\n***Listado clientes***')
        tabla_clientes = mostrar_tablas()
        tabla_clientes.field_names = ['id_cliente','nombre','edad','tipo_membresia']
        for cliente in clientes:
            tabla_clientes.add_row(cliente)
        print(tabla_clientes)
        return 
    cursor.close()
    conexion.close()

#Para añadir clientes, necesitamos un insert into y pedir al usuario su idcliente y el id de la actividad.

def inscribir_clientes():
    print('\n***Añadir clientes***')
    try:
        conexion = conectar_basedatos()
        cursor = conexion.cursor()
        nombre = str(input('Introduzca su nombre y apellidos: ')).title()
        edad = int(input('Introduzca su edad: '))
        membresia = str(input('Introduzca la membresia deseada: Premium, Básica o Estándar: ')).title()
        cursor.execute('INSERT INTO clientes (nombre,edad,tipo_membresia) VALUES (%s,%s,%s)', (nombre,edad,membresia))
        conexion.commit()
        print(f'Bienvenido {nombre}')
        return 
    except:
        print('Algo ha fallado durante el registro.')
    conexion.close()
    cursor.close()

#Para actualizarlos, simplemente usaremos un update con los datos nuevos y un WHERE para localizará a dicho cliente.

def actualizar_clientes():
    print('\n***Actualizar clientes***')
    try:
        conexion = conectar_basedatos()
        cursor = conexion.cursor()
        mostrar_clientes()
        idcliente = int(input('Introduce el idcliente para actualizarlo: '))
        nombre = str(input('Introduzca su nombre y apellidos: ')).title()
        edad =int(input('Introduzca su edad: ')) 
        membresia = str(input('Introduzca la membresia deseada: Premium, Básica o Estándar: ')).title()
        cursor.execute('UPDATE clientes SET nombre = %s, edad = %s, tipo_membresia = %s WHERE id_cliente = %s', (nombre,edad,membresia,idcliente))
        if cursor.rowcount > 0:
            conexion.commit()
            print(f'El cliente con ID {idcliente} ha sido actualizada a {nombre}.')
            return 
        else:
            print(f'No se encontró un cliente con ese ID.')
    except:
        print('Algo ha fallado durante la actualización')

#Por último crearemos la opción de eliminar clientes valiendonos de un  DELETE y un WHERE para localizar al cliente

def eliminar_clientes():
    print('\n***Eliminar clientes***')
    conexion = conectar_basedatos()
    cursor = conexion.cursor()
    idcliente = int(input('Introduce el idcliente para eliminarlo: '))
    cursor.execute('DELETE FROM clientes WHERE id_cliente = %s',(idcliente,))
        #Comprobamos que exista el id mediante el rowcount.
    if cursor.rowcount > 0:
        conexion.commit()
        print(f'El cliente con ID {idcliente} se ha eliminado.')
        mostrar_clientes()
        return 
    else:
        print(f'No se encontró un cliente con ese ID.')
    cursor.close()
    conexion.close()


#Creamos el menú con el que manejaremos los clientes.

def menu_clientes():
    while True:
        print('\n****Menu clientes****')
        print('1.- Añadir cliente')
        print('2.- Actualizar clientes')
        print('3.- Eliminar clientes')
        print('4.- Ver lista clientes')
        print('5.- Volver al menú principal')
        eleccion = int(input('Elige una opción: '))
        if eleccion ==1:
            inscribir_clientes()
        elif eleccion ==2:
           actualizar_clientes()
        elif eleccion ==3:
            eliminar_clientes()
        elif eleccion==4:
            mostrar_clientes()
        elif eleccion ==5:
            print('Volviendo al menú principal...')
            return
