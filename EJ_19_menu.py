from EJ_19_clientes import menu_clientes
from EJ_19_entrenadores import menu_entrenadores
from EJ_19_actividades import menu_actividades
from EJ_19_inscripciones import menu_inscripciones

#Importamos los menús de los otros archivos para que el funcionamiento radique en este único archivo de poco más de 20 líneas.
def menu_principal():
    while True:
        print('\n*****Menú principal*****')
        print('1.- Menú clientes')
        print('2.- Menú entrenadores')
        print('3.- Menú actividades')
        print('4.- Menú inscripciones')
        print('5.- Cerrar programa')
        eleccion = int(input('Elige una opción: '))
        if eleccion ==1:
            menu_clientes()
        elif eleccion ==2:
           menu_entrenadores()
        elif eleccion ==3:
            menu_actividades()
        elif eleccion==4:
            menu_inscripciones()
        elif eleccion ==5:
            print('Cerrando programa. Hasta la vista...')
            break
menu_principal()