# --------------------------------------------------------------------------CONTAR PARES
# definimos la función y añadimos el mensaje que mostrará
# def contar_pares(numeros): 
#     # creamos dos listas. una para añadir los numeros y otra para que unicamente se añadan los pares
#     lista_numeros =[]
#     lista_numeros_pares=[]
#     while True:
#         numeros = int(input("Introduce numeros enteros para obtener los pares: "))
#         if numeros == 0:
#               break
#         elif numeros % 2 !=0 and numeros !=0:
#               lista_numeros.append(numeros)
#         elif numeros % 2 == 0:
#                lista_numeros_pares.append(numeros)
#     print("En la lista introducida, hay", len(lista_numeros_pares),"números pares" )

# numeros = int(input("Introduce numeros enteros para obtener los pares: "))

# contar_pares(numeros)
# ----------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------NUMERO MAYOR
# def encontrar_maximo(numero_mayor): 
# # creamos una lista en la que todo número distinto de 0 será comprobado para ser el mayor
#     lista_numeros = []
#     while True:
#         numero_mayor = int(input("Introduce numeros enteros para obtener el valor máximo, utilizando '0' como el número final: "))
#         if numero_mayor == 0:
#               break
#         else:
#             lista_numeros.append(numero_mayor)
# # creamos una variable equivalente al primer numero de la lista
#     numero_mayor = lista_numeros[0]

# # utilizando un bucle for, recorreremos todos los numeros de la lista hasta que encuentre el mayor
#     for numero in lista_numeros:
#         if numero > numero_mayor:
#             numero_mayor = numero
#     print("El número mayor es", numero)

# numero_mayor = int(input("Introduce numeros enteros para obtener el valor máximo, utilizando '0' como el número final: "))

# encontrar_maximo(numero_mayor)
# --------------------------------------------------------------------------------------------------

# #PAra que un numero sea primo tiene que ser mayor que 1, y ser divisible por 1 y por el mismo únicamente, si se divide por cualquier otro número el resto será mayor que 0
# def es_primo(numero):
#     if numero > 1:
#         if numero % numero+1 == 0:
#             print('No es primo')
#         elif (numero % 1 == 0) and (numero % numero == 0):
#             print('Es primo')
#     else:
#         print ('Menor que 1, el número no puede ser primo')


# ##Programa principal empieza aqui
# numero = int(input("Introduce un número entero para averiguar si el número es primo o no, (utilizando '0' como el número final): "))

# es_primo(numero)

# ##############################################
# #Solucion con return en la funcion es_primo
# ############################################
# def es_primo(numero):
#     valor_devuelto = False
#     if numero > 1:
#         if numero % numero+1 == 0:
#             valor_devuelto = False
#         elif (numero % 1 == 0) and (numero % numero == 0):
#             valor_devuelto = True
#     else:
#         valor_devuelto = False
#     return valor_devuelto

# ##Programa principal empieza aqui
# numero = int(input("Introduce un número entero para averiguar si el número es primo o no, (utilizando '0' como el número final): "))

# valor_funcion = es_primo(numero)

# if valor_funcion == True:
#     print('Es primo')
# else:
#     print('No es primo')

