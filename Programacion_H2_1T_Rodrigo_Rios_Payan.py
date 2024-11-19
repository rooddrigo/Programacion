import mysql.connector                          #usuario: 'root'   
                                                #contraseña: 'curso'
#Creamos la función conectar_basedatos por la cual accederemos a la base de datos adjunta en git.hub
def conectar_basedatos():
    return mysql.connector.connect(host='localhost', user='root', password='curso', database='HITO_PROG')

#Esta función la creamos para poder mostrar los productos, clientes, pedidos, etc...
def tabla_mostrar():
    from prettytable import PrettyTable
    tabla_productos = PrettyTable()
    return tabla_productos

#Para que el usuario pueda pertenecer a la base de datos deberá de registrarse o iniciar sesión.
def registrar_cliente():
    try:
        conexion = conectar_basedatos()
        cursor = conexion.cursor()
        #Nos conectamos a la base de datos
        nombre = str(input('Introduzca su nombre y apellidos: ')).title()
        direccion = input('Introduzca su dirección: ')
        tlf = int(input('Introduzca su número de teléfono: '))
        #Pedimos al usuario sus datos
        cursor.execute('INSERT INTO cliente (nombre,direccion,tlf) VALUES (%s,%s,%s)', (nombre,direccion,tlf))
        #Mediante el execute, introducimos los datos del cliente en la base de datos.
        conexion.commit()
        #Al estar 'alterando' datos de la base de datos, necesitamos usar un commit.
        idcliente = cursor.lastrowid
        #El comando lastrowid, nos recoge automaticamente el idcliente puesto que es una primary key que se autoincrementa.
        print(f'Bienvenido {nombre}, su id de cliente es {idcliente}')
    except:
        print('Algo ha fallado durante el registro.')
        #Añadimos un control de excepciones para asegurarse de que el usuario no experimente errores en el código y pueda continuar.
    finally:
        conexion.close()
        cursor.close()
        #Cerramos la conexión mediante un finally para que se cierre indistintamente de lo que ocurra.


#En caso de ya tener usuario, iniciaremos sesión.
def iniciar_sesion_cliente():    
    try: 
        conexion = conectar_basedatos()
        cursor = conexion.cursor()
        idcliente = int(input('Introduce tu idcliente: '))
        cursor.execute("SELECT * FROM cliente where idcliente =%s ", (idcliente,))
        #Comprobamos que exista el idcliente o de lo contrario nos saltará el else.
        nombres = cursor.fetchall()
        #Mediante el fetchall, seleccionamos todo pero solo imprimimos en este caso su nombre, a modo de hacerlo más realista.
        if nombres:
            for nombre_idcliente in nombres:
                print(f"Bienvenido/a de nuevo, {nombre_idcliente[1]}")
            #nombre_cliente[O] ES EL ID Y LA 1 ES EL NOMBRE.
            cursor.close()
            conexion.close()
        else:
            print("No se ha encontrado ese idcliente.") 
    finally:
        cursor.close()
        conexion.close()
        
        




#Creamos la función que utilizaremos para hacer pedidos.
def realizar_pedidos():
    cliente_pregunta=  int(input('¿Es usted cliente? Pulse 1.-Para registrarse o 2.-Para introducir tu idcliente: '))
    if cliente_pregunta == 1:
        registrar_cliente()
    elif cliente_pregunta == 2:
        iniciar_sesion_cliente()
        #Comprobamos que sea cliente.
    try:
        conexion = conectar_basedatos()
        cursor = conexion.cursor()

        # Pedimos el ID del cliente para introducir el pedido en su id.
        idcliente = int(input("Introduce tu ID de cliente: "))
        cursor.execute("SELECT * FROM cliente WHERE idcliente = %s", (idcliente,))
        cliente = cursor.fetchone()
        #Mediante el cursor.fetchone, seleccionamos unicamente el primer elemento de la fila, en este caso el idcliente para comprobar su existencia.
        if not cliente:
            print("Cliente no encontrado.")
            #En caso de que no exista, mediante el if not y el return nos aseguramos que vuelva atrás
            return
        
        # Creamos el pedido con el insert into y recogemos su id con el lastrowid.
        cursor.execute("INSERT INTO pedido (idcliente) VALUES (%s)", (idcliente,))
        idpedido = cursor.lastrowid

        # Para mostrar todos los productos utilizaremos la 'famosa' tabla gracias a la función tabla_mostrar().
        cursor.execute("SELECT * FROM producto")
        productos = cursor.fetchall()
        tabla_productos = tabla_mostrar()
        #field_names, se refiere al título de cada columna, recogidos de la base de datos
        tabla_productos.field_names = ['idproducto','nombre', 'medida', 'precio', 'stock']
        #Mediante un bucle for, recorremos la varible 'productos' que gracias al .fetchall() ha recogido todos los productos y los añadimos a nuestra nueva tabla.
        for producto in productos:
            tabla_productos.add_row(producto)
        print(tabla_productos)

        # Para añadir productos al pedido, nos aseguramos de que al escribir '0', se termine el pedido ya que ningún producto tiene el 0 por id.
        while True:
            idproducto = input("Introduce el ID del producto deseado (o 0 para finalizar): ")
            if idproducto == "0":
                break
            unidades = int(input("Cantidad: "))
            cursor.execute("SELECT precio FROM producto WHERE idproducto = %s", (idproducto,))
            precio = cursor.fetchone()[0] #Este [0] es para que asegurarnos de que recoja el precio del producto marcado.
            #Mediante este fetchone, recogemos el precio de los productos adquiridos, para añadirlo todo a la tabla detalles.
            cursor.execute("INSERT INTO detalle (idcliente, idpedido, idproducto, precio, unidades) VALUES (%s, %s, %s, %s, %s)",(idcliente, idpedido, idproducto, precio, unidades))
        conexion.commit()
        print(f"Pedido realizado con éxito. ID del pedido: {idpedido}")
        #Con este tipo de excepción, hacemos que podamos ver el error sin tener que parar el programa.
    except Exception as e:
        print(f"Error al realizar la compra: {e}")
    finally:
        cursor.close()
        conexion.close()


#Creamos la función de seguir los pedidos siendo un usuario. Más tarde entenderemos el por qué de esta aclaración.
def seguimiento_pedido():
    conexion = conectar_basedatos()
    cursor = conexion.cursor()
    #Como hemos hecho anteriormente, seleccionamos un pedido en concreto mediante su id.
    try:
        idpedido = int(input('Introduce el id del pedido para realizar su seguimiento: '))
        cursor.execute('SELECT * FROM detalle WHERE idpedido = %s', (idpedido,))
        pedidos = cursor.fetchall()
        if pedidos:
            print('*****Listado de pedidos*****')
            #Lo imprimimos mediante las 'grandiosa' tabla.
            tabla_pedidos = tabla_mostrar()
            tabla_pedidos.field_names = ['idcliente','idpedido','idproducto','precio','unidades','fecha']
            for pedido in pedidos:
                tabla_pedidos.add_row(pedido)
            print(tabla_pedidos)
        else:
            print('No se ha podido seguir ese pedido.')

    except ValueError:
        print('Introduce un id válido')
    finally:
        cursor.close()
        conexion.close()



#Creamos un control de acceso para que solo las personas con las credenciales puedan acceder a la base de todos los clientes.
def menu_control_clientes():
    print('\n**Usted ha accedido a la base de datos de clientes**\n')
    print('Seleccione que desea hacer:')
    print('Pulse 1 para acceder a la base de datos de los clientes. ')
    print('Pulse 2 para volver al menú')
    eleccion = int(input('Introduzca la opción deseada: '))
    if eleccion == 1:
        conexion = conectar_basedatos()
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM cliente')
        clientes = cursor.fetchall()
        #Imprimimos todos los clientes mediante una tabla.
        if clientes:
            print('Listado de clientes')
            tabla_clientes = tabla_mostrar()
            tabla_clientes.field_names = ['idcliente','nombre','direccion','tlf']
            for cliente in clientes:
                tabla_clientes.add_row(cliente)
            print(tabla_clientes)
            conexion.close()
            cursor.close()
            #En caso de querer saber más a cerca de un cliente, como sus pedidos, simplemente marcaremos su id.
            while True:
                info_cliente = int(input('Introduzca el id del cliente para acceder a sus pedidos o "0" para volver al inicio de sesión: '))
                if info_cliente ==0:
                    print('\nVolviendo al inicio de sesión...')
                    return 
                conexion = conectar_basedatos()
                cursor = conexion.cursor()
                cursor.execute('SELECT idcliente FROM cliente WHERE idcliente = %s', (info_cliente,))
                #Con este fetchone, nos aseguramos de coger un id real.
                idcliente = cursor.fetchone()
                if idcliente:
                    conexion = conectar_basedatos()
                    cursor = conexion.cursor()
                    cursor.execute('SELECT * FROM detalle WHERE idcliente = %s', (info_cliente,))
                    pedidos = cursor.fetchall()
                    #De nuevo, una tablita para mostrar los detalles de los pedidos de ese usuario.
                    if clientes:
                        print(f'Información de pedidos del id{info_cliente}')
                        tabla_pedidos = tabla_mostrar()
                        tabla_pedidos.field_names = ['idcliente','idpedido','idproductos','precio','unidades', 'fecha']
                        for pedido in pedidos:
                            tabla_pedidos.add_row(pedido)
                        print(tabla_pedidos)
                else: 
                    print('Introduce un id existente')
        else:
            print('\nNo se ha encontrado ningún cliente con ese id.')
    elif eleccion == 2:
        print('Volviendo al menú...')
        return 



#Estamos ante la creación del menú de todo el programa.
def menu_principal():
    print(f'\n¿Desea acceder a la base de datos de los clientes o realizar/seguir un pedido?')
    while True:
        try:
            #Creamos las diferentes opciones.
            acceso = int(input(f'1.-Base de datos Clientes, 2.-Realizar un pedido , 3.-Seguimiento de un pedido o 4.-Salir: '))
            if acceso == 1:
                while True:
                    #Nos aseguramos de que si no recordamos las credenciales podamos volver atrás sin parar el programa.
                    usuario = str(input('Introduce el usuario para acceder a la base de datos: '))
                    contraseña = str(input('Introduce la contraseña: '))
                    if usuario != 'root' or contraseña != 'curso':
                        print('Usuario o contraseña incorrectos, intentelo de nuevo.')
                        salir = int(input('1.-Volver a intentarlo o 2.-Salir al menú: '))
                        if salir == 2:
                            print('Volviendo al menú...')
                            return menu_principal()
                        elif salir == 1:
                            print('Volviendo al inicio de sesión...\n')
                        else: 
                            print('Introduce un número válido')
                    #Al poner el usuario y la contraseña, nos llevará directos al control de los clientes.
                    elif usuario == 'root' and contraseña == 'curso':
                        print('\nAcceso permitido, accediendo a la base de datos de los clientes.')
                        menu_control_clientes()
            elif acceso == 2:
                realizar_pedidos()
            elif acceso == 3:
                print('\n**Accediendo al seguimiento de pedidos**\n')
                seguimiento_pedido()
            elif acceso ==4:
                print('\nCerrando programa. Hasta la vista.')
                break
        except ValueError:
            print('Introduce un número válido')
menu_principal()

#Espero que haya gustado ;)))))