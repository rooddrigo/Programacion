# -----------------------------------------------------------------------------------------------------------------------------------FORMAS
# while True:
#     eleccion =int(input("Selecciona la forma que deseas obtener, siendo 1-Cuadrado, 2-Rectángulo o 3-Para finalizar el programa: "))
#     if eleccion == 1:
#         basecuadrado =int(input("Elige el lado del cuadrado:  "))
#         for i in range(basecuadrado):
#             print(basecuadrado*'*')
#         areacuadrado= basecuadrado*basecuadrado
#         print("Área =",areacuadrado)
#         perimetrocuadrado= basecuadrado*4
#         print("Perímetro =",perimetrocuadrado)
#     elif eleccion ==2:
#         baserectangulo = int(input("Elige la base del rectángulo: "))
#         alturarectangulo = int(input("Ahora, la altura del rectángulo: "))
#         if baserectangulo == alturarectangulo:
#             print("!No pueden tener la misma base¡ Eso es un cuadrado")
#         elif baserectangulo != alturarectangulo:
#             for i in range(alturarectangulo):
#                 print(baserectangulo*'*')

#             area=baserectangulo * alturarectangulo
#             print("Área =",area )
#             perimetro = (baserectangulo*2) + (alturarectangulo*2)
#             print("Perímetro =",perimetro)
#     elif eleccion ==3:
#         print("El programa ha terminado, ¡¡Hasta luego!!")
#         break
#     elif eleccion != 1 or eleccion !=2 or eleccion !=3:
#         print("Opción invalida, por favor elija una de las 3 disponibles: 1-Cuadrado, 2-Rectángulo o 3-Para finalizar el programa:")
# ----------------------------------------------------------------------------------------------------------------------------------------

import random

print("Bienvenido a Piedra, Papel o Tijera, buena suerte")
# 1=Piedra
# 2=Papel
# 3=Tijeras
contador_usuario = 0
contador_programa = 0
while True:
    eleccion = int(input("Escoge '1' para sacar piedra, '2' para sacar Papel o '3' para sacar Tijera: "))
    # lista_aleatoria =[1,2,3]
    hola = random.choice([1,2,3])
    if eleccion == 1 and hola == 1:
        print("Has seleccionado piedra")
        print("El programa ha seleccionado Piedra, Empate")
        print("El programa lleva: ",contador_programa, "rondas ganadas")
        print("Llevas", contador_usuario, "rondas ganadas")
    elif eleccion == 2 and hola == 2:
        print("Has seleccionado papel")
        print("El programa ha seleccionado Papel, Empate")
        print("El programa lleva: ",contador_programa, "rondas ganadas")
        print("Llevas", contador_usuario, "rondas ganadas")
    elif eleccion == 3 and hola == 3:
        print("Has seleccionado tijeras")
        print("El programa ha seleccionado Tijera, Empate")
        print("El programa lleva: ",contador_programa, "rondas ganadas")
        print("Llevas", contador_usuario, "rondas ganadas")
    elif eleccion == 2 and hola == 1:
        print("Has elegido papel")
        print("El programa ha elegido Piedra, has ganado")
        contador_usuario = contador_usuario + 1
        print("El programa lleva: ",contador_programa, "rondas ganadas")
        print("Llevas", contador_usuario, "rondas ganadas")
    elif eleccion == 2 and hola == 3:
        print("Has elegido papel")
        print("El programa ha elegido tijeras, has perdido")
        contador_programa = contador_programa +1
        print("El programa lleva: ",contador_programa, "rondas ganadas")
        print("Llevas", contador_usuario, "rondas ganadas")
    elif eleccion == 3 and hola == 1:
        print("Has elegido tijeras")
        print("el programa ha elegido Piedra, has perdido")
        contador_programa = contador_programa + 1
        print("El programa lleva: ",contador_programa, "rondas ganadas")
        print("Llevas", contador_usuario, "rondas ganadas")
    elif eleccion == 3 and hola == 2:
        print("Has elegido tijeras")
        print("el programa ha elegido Papel, has ganado")
        contador_usuario = contador_usuario + 1
        print("El programa lleva: ",contador_programa, "rondas ganadas")
        print("Llevas", contador_usuario, "rondas ganadas")
    if contador_usuario == 3 or contador_programa == 3:
        break











# lista_aleatoria =['Piedra','Papel','Tijera']
# eleccion_aleatoria = random.choices(lista_aleatoria)
# if eleccion == 1:
#     eleccion ='Piedra'
#     print
#     if eleccion_aleatoria == 'Piedra':
#         print("Has elegido 1-Piedra")
#         print("El programa ha elegido Piedra,Empate")
#     elif eleccion_aleatoria == 'Papel':
#         print("Has elegido 1-Piedra")
#         print("El programa ha elegido Papel,Has perdido")
#     elif eleccion_aleatoria == 'Tijeras':
#         print("Has elegido 1-Piedra")
#         print("El programa ha elegido Tijeras,Free elo zorritas")
        
# elif eleccion == 2:
#         eleccion ='Papel'
# elif eleccion == 3:
#         eleccion ='Tijeras'
# elif eleccion == 1 and eleccion_aleatoria == 'Piedra':
#         print("Has elegido 1-Piedra")
#         print("El programa ha elegido Piedra,Empate")
# elif eleccion == 1 and eleccion_aleatoria == 'Papel':
#         print("Has elegido 1-Piedra")
#         print("El programa ha elegido Papel,Has perdido")
# elif eleccion == 1 and eleccion_aleatoria == 'Tijeras':
#         print("Has elegido 1-Piedra")
#         print("El programa ha elegido Tijeras,Free elo zorritas")
        






