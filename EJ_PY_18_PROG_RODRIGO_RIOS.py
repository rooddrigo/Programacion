import mysql.connector


#CREAMOS LA FUNCIÓN crear_categoria PARA PODER AÑADIR CATEGORIAS A LA BASE DE DATOS.
def crear_categoria():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        #CON LAS DOS PRIMERAS LINEAS, ACCEDEMOS A LA BASE DE DATOS.
        idcategoria = int(input("Ingrese el ID que quieras crear: "))
        nombre = str(input("Ingrese el nombre que recibirá esa categoria: "))
        #PEDIMOS EL ID NUEVO Y SU NOMBRE PARA AÑADIRLO CON EL .execute
        cursor.execute("INSERT INTO categoria (idcategoria, nombre) VALUES (%s, %s)", (idcategoria, nombre))
        conexion.commit()
        print(f"\nLa categoria {nombre}, ha sido creada correctamente")
    except:
        print(f"No se ha podido añadir la categoria{nombre}")
        #MEDIANTE EL TRY, HACEMOS QUE AL AÑADIR LA CATEGORIA, NOS LO CONFIRME.
    
    cursor.close()
    conexion.close()

#CREAMOS LA FUNCIÓN leer_categoria PARA PODER VER LAS CATEGORIAS DE LA BASE DE DATOS.
def leer_categorias():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM categoria")
    #CON EL .execute, SELECCIONAMOS LA TABLA DE CATEGORIAS Y LUEGOS LAS MOSTRAMOS CON EL .fetchall Y UN FOR
    categorias = cursor.fetchall()
    if categorias:
        print("Listado de Categorías:")
        for categoria in categorias:
            print(f"{categoria[0]} - {categoria[1]}")
        #CATEGORIA[O] ES EL NÚMERO Y LA 1 ES EL NOMBRE.
    else:
        print("No hay categorías disponibles.")
    cursor.close()
    conexion.close()

#CREAMOS LA FUNCIÓN actualizar_categoria PARA PODER ACTUALIZAR LAS CATEGORIAS DE LA BASE DE DATOS.
def actualizar_categoria():
    conexion = conectar()
    cursor = conexion.cursor()

    idcategoria = input("Ingrese el ID de la categoría a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre de la categoría: ")
    cursor.execute("UPDATE categoria SET nombre = %s WHERE idcategoria = %s", (nuevo_nombre, idcategoria))
    #LA FUNCIÓN .rowcount LA UTILIZAMOS PARA SABER SI HA ENCONTRADO AL MENOS UNA CATEGORIA CON ESE ID. DE LO CONTRARIO NOS IMPRIMIRÍA EL ELSE.
    if cursor.rowcount > 0:
        conexion.commit()
        print(f"La categoría con ID {idcategoria} ha sido actualizada a '{nuevo_nombre}'.")
    else:
        print(f"No se encontró una categoría con ID {idcategoria}.")

    cursor.close()
    conexion.close()


#CREAMOS LA FUNCIÓN eliminar_categoria PARA PODER ACTUALIZAR LAS CATEGORIAS DE LA BASE DE DATOS.
def eliminar_categoria():
    conexion = conectar()
    cursor = conexion.cursor()

    idcategoria = input("Ingrese el ID de la categoría a eliminar: ")
    cursor.execute("DELETE FROM producto WHERE idcategoria = %s", (idcategoria,))
    cursor.execute("DELETE FROM categoria WHERE idcategoria = %s", (idcategoria,))
    #DE NUEVO UTILIZAMOS EL ROWCOUNT (LO HE ENCONTRADO EN stackoverflow, un foro de programación).
    if cursor.rowcount > 0:
        conexion.commit()
        print(f"La categoría con ID {idcategoria} ha sido eliminada.")
    else:
        print(f"No se encontró una categoría con ID {idcategoria}.")

    cursor.close()
    conexion.close()
#EL CÓDIGO MENÚ ESTÁ EN OTRO ARCHIVO.

def mostrar_menu_cat():
    while True:
        print("\nGestión de Categorías")
        print("Seleccione una opción:")
        print("1. Crear nueva categoría")
        print("2. Leer categorías existentes")
        print("3. Actualizar una categoría")
        print("4. Eliminar una categoría")
        print("5. Salir\n")
        
        eleccion_usuario= int(input("Opción: "))
        
        if eleccion_usuario == 1:
            crear_categoria()
        elif eleccion_usuario == 2:
            leer_categorias()
        elif eleccion_usuario == 3:
            actualizar_categoria()
        elif eleccion_usuario == 4:
            eliminar_categoria()
        elif eleccion_usuario == 5:
            print("Saliendo de la gestión de categorías. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
            print('Saliendo de la gestión de productos. ¡Hasta pronto!')
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
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
            print('Saliendo de la gestión de clientes. ¡Hasta pronto!')
            return
        else:
            print('Opción no válida. Intente de nuevo.')

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def tabla_mostrar_pedidos():
    from prettytable import PrettyTable
    tabla_pedidos = PrettyTable()
    return tabla_pedidos

def tabla_mostrar_detalles():
    from prettytable import PrettyTable
    tabla_detalles = PrettyTable()
    return tabla_detalles

def conectar():
    return mysql.connector.connect(host='localhost', user='root', password='curso', database='supermercado')

def mostrar_pedidos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM pedido')
    pedidos = cursor.fetchall()
    if pedidos:
        print('Listado de Pedidos:')
        tabla_pedidos = tabla_mostrar_pedidos()
        tabla_pedidos.field_names = ['idpedidos','idcliente','fechapedido','fechaentrega']
        for pedido in pedidos:
            tabla_pedidos.add_row(pedido)
        print(f'\n\nTabla de pedidos:\n{tabla_pedidos}')
    else:
        print('No hay pedidos disponibles.')
    while True:
        detalles_pedido = int(input('Pulsa 1.-Detalles de un pedido en particular o 2.- Para salir al menú: '))
        if detalles_pedido ==1:
            print('\nAccediendo a la base de datos de los detalles de pedidos...\n')
            mostrar_detalles_pedidos()
        elif detalles_pedido ==2:
            print('Volviendo al menú principal...')
            return
        conexion.close()
        cursor.close()

def mostrar_detalles_pedidos():
    conexion = conectar()
    cursor = conexion.cursor()
    idpedido = int(input('Introduce el ID de tu pedido para mostrar los detalles: '))
    cursor.execute('SELECT * FROM detalle WHERE idpedido = %s', (idpedido,))
    detalles = cursor.fetchall()
    if detalles:
        conexion.commit()
        tabla_detalles= tabla_mostrar_detalles()
        tabla_detalles.field_names = ['idpedidos','idproducto','precio','unidades','descuento']
        for detalle in detalles:
            tabla_detalles.add_row(detalle)
        print(f'Los detalles del pedido {idpedido} son:\n{tabla_detalles}')
    else:
        print('Pedido no encontrado, intentelo de nuevo')
    conexion.close()
    cursor.close()
    

def crear_nuevo_pedido():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        idpedido = int(input('Introduce el id del pedido a crear: ' ))
        idproducto = int(input('Introduce un id de producto: '))
        unidades = int(input('Introduce el número de unidades: '))
        cursor.execute('SELECT precio FROM producto WHERE idproducto = %s', (idproducto,))
        resultado = cursor.fetchone()
        precio = resultado[0]
        descuento = 0
        cursor.execute('INSERT INTO detalle (idpedido,idproducto,precio,unidades,descuento) VALUES (%s,%s,%s,%s,%s)', (idpedido,idproducto,precio,unidades,descuento))
        conexion.commit()
        print(f'Pedido con id {idpedido}creado con exito')
    except:
        print(f'No se ha podido crear un pedido con id{idpedido}')
    conexion.close()
    cursor.close()


def eliminar_pedido():
    conexion = conectar()
    cursor = conexion.cursor()
    idpedido = int(input('Introduce el id del pedido a borrar: '))
    idproducto = int(input('Introduce el id del producto a borrar: '))
    cursor.execute('DELETE FROM detalle WHERE idpedido = %s AND idproducto =%s', (idpedido,idproducto))
    if cursor.rowcount > 0:
        conexion.commit()
        print(f'El pedido con ID:  {idpedido} ha sido eliminado.')
    else:
        print(f'No se encontró ningún pedido con ese ID.')
    cursor.close()
    conexion.close()   


def actualizar_pedido():
    conexion = conectar()
    cursor = conexion.cursor()
    idpedido = int(input('Introduce el id del pedido a modificar : '))
    idproducto = int(input('Introduce un id de producto: '))
    unidades = int(input('Introduce el número de unidades: '))
    cursor.execute('SELECT precio FROM producto WHERE idproducto = %s', (idproducto,))
    resultado = cursor.fetchone()
    precio = resultado[0]
    descuento = 0
    cursor.execute('UPDATE detalle SET unidades = %s, precio= %s,descuento = %s WHERE idpedido = %s AND idproducto =%s', ( unidades, precio, descuento, idpedido,idproducto))
    if cursor.rowcount > 0:
        conexion.commit()
        print(f'El pedido con ID {idpedido} ha sido actualizado.')
    else:
        print(f'No se encontró un pedido con ese ID.')
    cursor.close()
    conexion.close()

def mostrar_menu_pedidos():
    while True:
        print('\nGestión de Pedidos')
        print('Seleccione una opción:')
        print('1. Crear nuevo pedido')
        print('2. Leer pedidos existentes')
        print('3. Actualizar un pedido')
        print('4. Eliminar un pedido')
        print('5. Salir al menú principal\n')
        eleccion_usuario = int(input('Opción: '))
        if eleccion_usuario == 1:
            crear_nuevo_pedido()
        elif eleccion_usuario == 2:
            mostrar_pedidos()
        elif eleccion_usuario == 3:
            actualizar_pedido()
        elif eleccion_usuario == 4:
            eliminar_pedido()
        elif eleccion_usuario == 5:
            print('Saliendo de la gestión de pedidos. ¡Hasta pronto!')
            return
        else:
            print('Opción no válida. Intente de nuevo.')

def seleccion_tabla():
    while True:
        try: 
            eleccion = int(input('\nPulse 1.-Categorias, 2.-Productos , 3.-Clientes , 4.-Pedidos o 5.-Salir: '))
            if eleccion ==1:
                mostrar_menu_cat()
            elif eleccion==2:
                mostrar_menu_produc()
            elif eleccion ==3:
                mostrar_menu_clientes()
            elif eleccion ==4:
                mostrar_menu_pedidos()
            elif eleccion ==5:
                print('Cerrando programa. Hasta la vista.')
                break
            else:
                print('Introduce un número válido')
        except ValueError:
            print('Pulse 1.-Categorias, 2.-Productos , 3.-Clientes , 4.-Pedidos o 5.-Salir: ')
seleccion_tabla()