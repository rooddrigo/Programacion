
###-----------------------------------------------------------------------------------------------------------------------------------CUADRADO O RECTÁNGULO:
# # Rodrigo Ríos Payán
#CREAMOS UN BUCLE WHILE TRUE PARA QUE EL USUARIO ELIJA HASTA QUE INTRODUZCA EL NÚMERO '3' Y PARE EL PROGRAMA.
while True:
    try:
        eleccion =int(input("\nSelecciona la forma que deseas obtener, siendo 1-Cuadrado, 2-Rectángulo o 3-Para finalizar el programa: "))
        #SI ELIGE '1' MEDIANTE UN BUCLE FOR, EL PROGRAMA IMPRIMIRÁ LA BASE DEL CUADRADO POR '*' A FIN DE IMITAR LA FORMA DE ESTE.
        if eleccion == 1:
            basecuadrado =int(input("Elige el lado del cuadrado:  "))
            #EL RANGO DEL BUCLE FOR ES LA BASE DEL CUADRADO DEBIDO A QUE CADA LADO ES IGUAL
            for i in range(basecuadrado):
                print(basecuadrado*'*')
                #CREAMOS LAS VARIABLES PARA QUE IMPRIMA EL ÁREA Y PERÍMETRO DEL CUADRADO.
            areacuadrado= basecuadrado*basecuadrado
            print("\nEl Área del cuadrado es =",areacuadrado)
            perimetrocuadrado= basecuadrado*4
            print("El Perímetro del cuadrado =",perimetrocuadrado)
        #EN EL CASO DEL RECTÁNGULO, NOS ASEGURAMOS DE QUE LAS BASES SEAN DISTINTAN CON EL IF Y POSTERIORMENTE VOLVEMOS A UTILIZAR UN BUCLE FOR PARA IMPRIMIRLO.
        elif eleccion ==2:
            baserectangulo = int(input("Elige la base del rectángulo: "))
            alturarectangulo = int(input("Ahora, la altura del rectángulo: "))
            if baserectangulo == alturarectangulo:
                print("\n¡No pueden tener la misma base! Eso es un cuadrado")
            elif baserectangulo != alturarectangulo:
                #EL RANGO DEL BUCLE FOR, HA DE SER LA ALTURA DEL RECTÁNGULO Y NO LA BASE COMO EN EL CUADRADO.
                for i in range(alturarectangulo):
                    print(baserectangulo*'*')
                area=baserectangulo * alturarectangulo
                print("\nEl Área del rectángulo es =",area )
                perimetro = (baserectangulo*2) + (alturarectangulo*2)
                print("El Perímetro del rectángulo es =",perimetro)
            #EN CASO DE QUERER PARAR, SIMPLEMENTE PONEMOS UN BREAK PARA QUE CUANDO EL USUARIO PULSE '3', TERMINE EL PROGRAMA.
        elif eleccion ==3:
            print("El programa ha terminado, ¡¡Hasta luego!!")
            break
        else:
            print("\nOpción invalida, por favor elija una de las 3 disponibles: 1-Cuadrado, 2-Rectángulo o 3-Para finalizar el programa")
        #ESTA ÚLTIMA LINEA SE QUE NO ESTÁ EXPLICADA PERO ES MUY UTIL PARA QUE EL PROGRAMA NO DE ERROR AL INTRODUCIR UN STR EN LA ELECCIÓN EVITANDO ASI QUE SE PARE EL PROGRAMA.  
    except ValueError:
        print("\nOpción invalida, por favor elija una de las 3 disponibles: 1-Cuadrado, 2-Rectángulo o 3-Para finalizar el programa")
###----------------------------------------------------------------------------------------------------------------------------------------

###-----------------------------------------------------------------------------------------------------------------------------PIEDRA PAPEL O TIJERA
# # Rodrigo Rios Payan
#IMPORTAMOS UN RANDOM QUE NOS SERVIRÁ PARA LA ELECCIÓN DE LA MAQUINA
import random

print("Bienvenido a Piedra, Papel o Tijera, buena suerte")
#ESTOS SON LOS RESULTADOS DE LA MAQUINA Y DEL USUARIO DEPENDIENDO EL NÚMERO QUE SAQUE.
# 1=Piedra
# 2=Papel
# 3=Tijeras
#CREAMOS UN CONTADOR PARA POSTERIORMENTE SABER QUIEN HA GANADO, EL PRIMERO QUE LLEGUE A 3 RONDAS GANADADAS
contador_usuario = 0
contador_programa = 0
#UTILIZANDO UN BUCLE WHILE, NOS ASEGURAMOS DE QUE EL PROGRAMA TERMINE SIEMPRE QUE UNO DE LOS JUGADORES ALCANZE 3 RONDAS GANADAS.
while contador_programa!=3 and contador_usuario !=3:
    try:
        #CREAMOS LA VARIABLE ELECCIÓN QUE Y ELECCIÓN ALEATORIO, UTILIZANDO UN .randint PARA QUE ELIJA UN NÚMERO DEL 1-3.
        eleccion = int(input("\nEscoge '1' para sacar piedra, '2' para sacar Papel o '3' para sacar Tijera: "))
        eleccion_aleatoria = random.randint(1,3)
        #DESARROLLAMOS EL CÓDIGO EN FUNCIÓN DE CUANDO GANA EL USUARIO Y CUANDO PIERDE LA MAQUINA Y VICEVERSA.
        if eleccion == 1 and eleccion_aleatoria == 1:
            print("Has seleccionado piedra")
            print("El programa ha seleccionado Piedra, Empate")
            contador_usuario = contador_usuario + 0
            contador_programa = contador_programa + 0
            #AÑADIMOS QUE IMPRIMA EL RESULTADO DE LOS CONTADORES EN CADA RONDA.
            print("\nEl programa lleva",contador_programa, "rondas ganadas")
            print("Llevas", contador_usuario, "rondas ganadas")
        if eleccion == 1 and eleccion_aleatoria == 2:
            print("Has seleccionado piedra")
            print("El programa ha seleccionado Papel, has perdido")
            contador_usuario = contador_usuario + 0
            contador_programa = contador_programa + 1
            print("\nEl programa lleva",contador_programa, "rondas ganadas")
            print("Llevas", contador_usuario, "rondas ganadas")
        if eleccion == 1 and eleccion_aleatoria == 3:
            print("Has seleccionado piedra")
            print("El programa ha seleccionado Tijeras, has Ganado")
            contador_usuario = contador_usuario + 1
            contador_programa = contador_programa + 0
            print("\nEl programa lleva",contador_programa, "rondas ganadas")
            print("Llevas", contador_usuario, "rondas ganadas")
        if eleccion == 2 and eleccion_aleatoria == 2:
            print("Has seleccionado papel")
            print("El programa ha seleccionado Papel, Empate")
            contador_usuario = contador_usuario + 0
            contador_programa = contador_programa + 0
            print("\nEl programa lleva",contador_programa, "rondas ganadas")
            print("Llevas", contador_usuario, "rondas ganadas")
        if eleccion == 3 and eleccion_aleatoria == 3:
            print("Has seleccionado tijeras")
            print("El programa ha seleccionado Tijera, Empate")
            contador_usuario = contador_usuario + 0
            contador_programa = contador_programa + 0
            print("\nEl programa lleva",contador_programa, "rondas ganadas")
            print("Llevas", contador_usuario, "rondas ganadas")
        if eleccion == 2 and eleccion_aleatoria == 1:
            print("Has elegido papel")
            print("El programa ha elegido Piedra, has ganado")
            contador_usuario = contador_usuario + 1
            print("\nEl programa lleva",contador_programa, "rondas ganadas")
            print("Llevas", contador_usuario, "rondas ganadas")
        if eleccion == 2 and eleccion_aleatoria == 3:
            print("Has elegido papel")
            print("El programa ha elegido tijeras, has perdido")
            contador_programa = contador_programa +1
            print("\nEl programa lleva",contador_programa, "rondas ganadas")
            print("Llevas", contador_usuario, "rondas ganadas")
        if eleccion == 3 and eleccion_aleatoria == 1:
            print("Has elegido tijeras")
            print("El programa ha elegido Piedra, has perdido")
            contador_programa = contador_programa + 1
            print("\nEl programa lleva",contador_programa, "rondas ganadas")
            print("Llevas", contador_usuario, "rondas ganadas")
        if eleccion == 3 and eleccion_aleatoria == 2:
            print("Has elegido tijeras")
            print("El programa ha elegido Papel, has ganado")
            contador_usuario = contador_usuario + 1
            print("\nEl programa lleva",contador_programa, "rondas ganadas")
            print("Llevas", contador_usuario, "rondas ganadas")
            #CON ESTA LINEA DE IF, NOS ASEGURAMOS DE QUE EL USUARIO ELIJA UN NÚMERO DEL 1-3.
        if eleccion >3 or eleccion <0:
            print("Elige un número del 1 al 3")
            #DE NUEVO UTILIZO LA UNA EXCEPCIÓN PARA ASEGURARME DE QUE EL PROGRAMA NO DE ERROR, EN CASO DE QUE ALGUIÉN UTILIZE ALGÚN CARACTER DE TIPO STR EN LA ELECCIÓN.
    except ValueError:
       print("\nOpción invalida, por favor elija una de las 3 disponibles: 1-Piedra, 2-Papel o 3-Tijeras:")
       #CON UN ÚLTIMO IF, DEPENDIENDO QUIÉN GANE, SALTARÁ UN MENSAJE U OTRO.
if contador_programa == 3:
    print("\nEl programa ha llegado a 3 rondas ganadas")
    print("Has perdido contra un robot, que vergüenza...")
elif contador_usuario == 3:
    print("\nHas llegado a 3 rondas ganadas")
    print("Enhorabuena, has ganado, SIIUUU")
  
###--------------------------------------------------------------------------------------------------------------------------------------


### -------------------------------------------------------------------------------------------------------------------------------BANCO 
#Rodrigo Rios Payan
#CREAMOS UN MENSAJE DE BIENVENIDA, A MODO DE HACERLO MÁS REALISTA, HE INTRODUCIDO UNA LIBRERIA DE FECHA PARA FINGIR UN REGISTRO DE ACCESO MEDIANTE LA HORA.
print("Bienvenido a tu banco")
print("\nPor su seguridad llevaremos un registro de acceso")
import datetime
fecha = datetime.datetime.now()
print("Fecha de entrada a la cuenta", fecha)
#MEDIANTE UN WHILE TRUE, EL PROGRAMA PEDIRÁ AL USUARIO EL INGRESO INICIAL DE SU CUENTA BANCARIA.
while True:
    try:
        #NOS ASEGURAMOS DE QUE SEA UN SALDO POSITIVO Y PONEMOS UN BREAK AL INTRODUCIR UN SALDO VÁLIDO PARA COMENZAR CON EL MENÚ.
        saldo_inicial=float(input("\nIntroduce el saldo de tu cuenta para poder tener un registro: "))
        if saldo_inicial<0:
            print("Introduce un saldo positivo")
        elif saldo_inicial>0:
            break
        #DE NUEVO UTILIZO UNA EXCEPCIÓN.
    except ValueError:
       print("\nOpción invalida, por favor introduzca el saldo")
#CREAMOS CONTADORES PARA LOS INGRESOS Y RETIRADAS
contador_ingresos = 0
contador_retiradas = 0
#MEDIANTE OTRO WHILE TRUE, EL PROGRAMA QUEDARÁ EN FUNCIONAMIENTO HASTA QUE EL USUARIO INTRODUZCA EL NÚMERO '4'.
while True:
    try: 
        #DESARROLLAMOS EL CÓDIGO COMO PIDE EL EJERCICIO.
        menu=int(input("\nSelecciona una de las opciones: 1-Ingresar dinero, 2-Retirar dinero, 3-Mostrar saldo disponible,  4-Salir o 5-Para ver los ingresos y las retiradas de dinero efectuadas: "))
        if menu ==1:
            dinero_ingresar = float(input("Introduce la cantidad a ingresar: "))
            #VOLVEMOS A UTILIZAR LA VARIBLE saldo_inicial PARA QUE TENGAMOS LOS INGRESOS Y RETIRADAS DE FORMA REALISTA.
            saldo_inicial = saldo_inicial + dinero_ingresar
            #SUMAMOS LA CANTIDAD PEDIDA Y SIEMPRE SE AÑADE UNO AL CONTADOR DE INGRESOS
            contador_ingresos = contador_ingresos +1
            ingresos_realizados = print("\nHas realizado un ingreso de",dinero_ingresar,"€")
        elif menu ==2:
            if saldo_inicial >0:
                dinero_retirar = float(input("Introduce la cantidad a retirar: "))
                saldo_inicial = saldo_inicial - dinero_retirar
                #RESTAMOS LA CANTIDAD PEDIDA Y SIEMPRE SE AÑADE UNO AL CONTADOR DE INGRESOS
                contador_retiradas = contador_retiradas + 1
                retiradas_realizados = print("\nHas realizado una retirada de",dinero_retirar,"€")
                #EN CASO DE QUE EL SALDO INICIAL SEA <= QUE 0, EL PROGRAMA NO DEJARÁ RETIRAR MÁS DINERO
            elif saldo_inicial <= 0:
                print("No puedes sacar más dinero, compruebe su saldo.")
        elif menu ==3:
            #MOSTRAMOS EL SALDO
            print("El saldo actual de tu cuenta es de", saldo_inicial,"€")
        elif menu ==4:
            #TERMINAMOS EL PROGRAMA
            print("Hasta luego.")
            break
        #MEDIANTE LOS CONTADORES CREADOS ANTERIORMENTE, OBTENEMOS LOS MOVIMIENTOS REALIZADOS
        elif menu ==5 and contador_retiradas>0 or contador_ingresos >0:
            print("Has retirado dinero",contador_retiradas, "veces.")
            print("Has ingresado dinero",contador_ingresos, "veces.")
        # elif menu == 5 and contador_ingresos>0:
        #     print("Has ingresado dinero",contador_ingresos, "veces.")
        elif menu ==5 and contador_ingresos==0 and contador_retiradas==0:
            print("No has realizado ningún ingreso o retirada.")
        #     #DE NUEVO UNA EXCEPCIÓN PARA EL STR.
        else:
            print("\nOpción invalida, seleccione una de las 5 opciones.")
    except ValueError:
       print("\nOpción invalida, Seleccione una de las 5 opciones.")

# A MODO DE HACERLO MÁS REALISTA, IMPORTAMOS UNA LIBRERIA PARA QUE VUELVA A IMPRIMIR LA HORA DE SALIDA DEL BANCO.
import datetime
fecha = datetime.datetime.now()
print("\nFecha de salida de la cuenta", fecha)
# # ##-----------------------------------------------------------------------------------------------------------------------