from    EJ15_BD     import mostrar_menu_cat
from EJ_PY_16_PROG_Rodrigo_Rios import mostrar_menu_produc
import mysql.connector

def conectar():
    return mysql.connector.connect(host='localhost', user='root', password='curso', database='supermercado')

def tabla_mostrar_clientes():
    from prettytable import PrettyTable
    tabla_clientes = PrettyTable()
    return tabla_clientes

def nuevo_cliente():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        idcliente = str(input('Ingrese el ID que quieras crear: ')).upper()
        cia = str(input('Introduce la cia del cliente: '))
        contacto = str(input('Ingrese el nombre del cliente a añadir: '))
        cargo = str(input(f'Introduce el cargo de {contacto}: '))
        direccion = str(input(f'Introduce la direccion de {contacto}: '))
        cursor.execute('INSERT INTO cliente (idcliente,cia,contacto,cargo,direccion) VALUES (%s,%s,%s,%s,%s)', (idcliente,cia,contacto,cargo,direccion))
        conexion.commit()
        print(f'El cliente {contacto}, ha sido añdido correctamente')
    except:
        print(f'No se ha podido añadir al cliente {contacto}')
    cursor.close()
    conexion.close()
        
def leer_cliente():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM cliente')
    clientes = cursor.fetchall()
    if clientes:
        print('Listado de Clientes:')
        tabla_clientes = tabla_mostrar_clientes()
        tabla_clientes.field_names = ['idcliente','cia','contacto','cargo','direccion']
        for cliente in clientes:
            tabla_clientes.add_row(cliente)
        print(tabla_clientes)
    else:
        print('No hay clientes disponibles.')
    cursor.close()
    conexion.close()   
       
def actualizar_cliente():
    conexion = conectar()
    cursor = conexion.cursor()
    idcliente = str(input('Ingrese el ID del a actualizar: ')).upper()
    contacto = str(input('Ingrese el nuevo nombre del cliente: '))
    cia =str(input('Introduce la cia del cliente quieras añadirla: '))
    cargo = str(input(f'Introduce el cargo de {contacto}: '))
    direccion = input(f'Introduce la direccion de {contacto}: ')
    cursor.execute('UPDATE cliente SET contacto = %s,  cia = %s, cargo = %s,direccion = %s WHERE idcliente = %s', (contacto, cia, cargo, direccion, idcliente))
    if cursor.rowcount > 0:
        conexion.commit()
        print(f'El cliente con ID {idcliente} ha sido actualizada a {contacto}.')
    else:
        print(f'No se encontró un ciente con ese ID.')
    cursor.close()
    conexion.close()
     
def eliminar_cliente():
    conexion = conectar()
    cursor = conexion.cursor()
    idcliente = input('Ingrese el ID del cliente a eliminar: ').upper()
    cursor.execute('DELETE FROM cliente WHERE idcliente = %s',(idcliente,))
    if cursor.rowcount > 0:
        conexion.commit()
        print(f'El producto con ID:  {idcliente} ha sido eliminado.')
    else:
        print(f'No se encontró ningún producto con ese ID.')
    cursor.close()
    conexion.close()   
   
def mostrar_menu_clientes():
    while True:
        print('\nGestión de Clientes')
        print('Seleccione una opción:')
        print('1. Introducir nuevo cliente')
        print('2. Leer clientes existentes')
        print('3. Actualizar un cliente')
        print('4. Eliminar un cliente')
        print('5. Salir al menú principal\n')
        eleccion_usuario = int(input('Opción: '))
        if eleccion_usuario == 1:
            nuevo_cliente()
        elif eleccion_usuario == 2:
            leer_cliente()
        elif eleccion_usuario == 3:
            actualizar_cliente()
        elif eleccion_usuario == 4:
            eliminar_cliente()
        elif eleccion_usuario == 5:
            print('Saliendo de la gestión de producto. ¡Hasta pronto!')
            return
        else:
            print('Opción no válida. Intente de nuevo.')

def seleccion_tabla():
    while True:
        try: 
            eleccion = int(input('\nPulse 1.-Categorias, 2.-Productos , 3.-Clientes o 4.-Para salir del programa: '))
            if eleccion ==1:
                mostrar_menu_cat()
            elif eleccion==2:
                mostrar_menu_produc()
            elif eleccion ==3:
                mostrar_menu_clientes()
            elif eleccion ==4:
                print('Cerrando programa, Hasta la próxima.')
                break
            else:
                print('Introduce un número válido')
        except ValueError:
            print('Pulse 1.-Categorias, 2.-Productos , 3.-Clientes o 4.-Para salir del programa: ')
seleccion_tabla()


