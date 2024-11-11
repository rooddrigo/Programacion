from    EJ15_BD     import mostrar_menu_cat
import mysql.connector

def conectar():
    return mysql.connector.connect(host='localhost', user='root', password='curso', database='supermercado')

def tabla_productos():
    from prettytable import PrettyTable
    tabla = PrettyTable()
    return tabla

def mostrar_menu_produc():
    while True:
        print('\nGestión de Productos')
        print('Seleccione una opción:')
        print('1. Introducir nuevo producto')
        print('2. Leer productos existentes')
        print('3. Actualizar un producto')
        print('4. Eliminar un producto')
        print('5. Salir al menú principal\n')
        eleccion_usuario = int(input('Opción: '))
        if eleccion_usuario == 1:
            nuevo_producto()
        elif eleccion_usuario == 2:
            leer_producto()
        elif eleccion_usuario == 3:
            actualizar_producto()
        elif eleccion_usuario == 4:
            eliminar_producto()
        elif eleccion_usuario == 5:
            print('Saliendo de la gestión de producto. ¡Hasta pronto!')
            return
        else:
            print('Opción no válida. Intente de nuevo.')
        return mostrar_menu_produc()
    
def nuevo_producto():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        idproducto = int(input('Ingrese el ID que quieras crear: '))
        nombre = str(input('Ingrese el nombre del producto a añadir: '))
        idcategoria = int(input('Introduce el Idcategoria al que quieras añadirla: '))
        medida = input(f'Introduce las medidas de {nombre}: ')
        precio = int(input(f'Introduce el precio de {nombre}: '))
        stock = int(input(f'Introduce el stock disponible de {nombre}'))
        cursor.execute('INSERT INTO producto (idproducto, nombre, idcategoria, medida, precio, stock) VALUES (%s, %s, %s, %s, %s, %s)', (idproducto, nombre, idcategoria, medida,precio,stock))
        conexion.commit()
        print(f'El producto {nombre}, ha sido añdido correctamente')
    except:
        print(f'No se ha podido añadir la categoria{nombre}')
    cursor.close()
    conexion.close()
        
def leer_producto():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM producto')
    productos = cursor.fetchall()
    if productos:
        print('Listado de productos:')
        tabla = tabla_productos()
        tabla.field_names = ['idproducto', 'Producto', 'Categoria', 'Medida', 'Precio (€)', 'Stock']
        for producto in productos:
            tabla.add_row(producto)
        print(tabla)
    else:
        print('No hay productos disponibles.')
    cursor.close()
    conexion.close()   
       
def actualizar_producto():
    conexion = conectar()
    cursor = conexion.cursor()
    idproducto = input('Ingrese el ID del a actualizar: ')
    nuevo_nombre = input('Ingrese el nuevo nombre del producto: ')
    idcategoria = int(input('Introduce el Idcategoria al que quieras añadirla: '))
    medida = input(f'Introduce las medidas de {nuevo_nombre}: ')
    precio = int(input(f'Introduce el precio de {nuevo_nombre}: '))
    stock = int(input(f'Introduce el stock disponible de {nuevo_nombre}'))
    cursor.execute('UPDATE producto SET nombre = %s,  idcategoria = %s, medida = %s,precio = %s ,stock = %s WHERE idproducto = %s', (nuevo_nombre,idcategoria, medida, precio, stock, idproducto))
    if cursor.rowcount > 0:
        conexion.commit()
        print(f'El producto con ID {idproducto} ha sido actualizada a {nuevo_nombre}.')
    else:
        print(f'No se encontró un producto con ese ID.')
    cursor.close()
    conexion.close()
     
def eliminar_producto():
    conexion = conectar()
    cursor = conexion.cursor()
    idproducto = input('Ingrese el ID del producto a eliminar: ')
    cursor.execute('DELETE FROM producto WHERE idproducto = %s', (idproducto,))
    if cursor.rowcount > 0:
        conexion.commit()
        print(f'El producto con ID: {idproducto} ha sido eliminado.')
    else:
        print(f'No se encontró ningún producto con ese ID.')
    cursor.close()
    conexion.close()   
   
# def seleccion_tabla():
#     while True:
#         try: 
#             eleccion = int(input('\nPulse 1.-Categorias, 2.-Productos o 3.-Para cerrar el programa: '))
#             if eleccion ==1:
#                 mostrar_menu_cat()
#             elif eleccion==2:
#                 mostrar_menu_produc()
#             elif eleccion ==3:
#                 print('Cerrando programa')
#                 break
#             else:
#                 print('Introduce un número válido')
#         except ValueError:
#             print('Pulse 1.-Categorias, 2.-Productos o 3.-Para cerrar el programa: ')
# seleccion_tabla()