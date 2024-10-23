## -------------------------------------------------------------------------------------------LISTA MÁS 5
# # Creamos una lista para añadir números con un while true para que termine solo cuando pongamos '0'.
# lista_numeros =[]
# while True: 
#     numeros_lista=int(input("\nIntroduce numeros en la lista para sumarles 5, siendo 0 el final: "))
#     if numeros_lista>0:
#         lista_numeros.append(numeros_lista)
#     elif numeros_lista<0:
#         lista_numeros.append(numeros_lista)  
#     elif numeros_lista ==0:
#         break 
# # Creamos la función que sumará 5 a cada número y usamos la función map() para que se aplique a toda la lista
# def lista_mas_5(numeros_lista):
#     return numeros_lista +5
# lista_con_aumento= list(map(lista_mas_5,lista_numeros))
# print("\nLos números de la lista +5: ",lista_con_aumento)
##----------------------------------------------------------------------------------------------

##----------------------------------------------------------------------------------------------FRASES A TÍTULOS
# #Creamos una lista para añadir frases con un while true para que termine solo cuando pongamos 'fin'.
# lista_frases =[]
# while True:
#     frases = str(input("\nIntroduce una frase a continuación, usando 'fin' para terminar: ")).lower()
#     if frases !='fin':
#         lista_frases.append(frases)
#     if frases =='fin':
#         break

# # Creamos la función que convertirá todas las primeras letros de las frases a letras mayúsculas y usamos la función map() para que se aplique a toda la lista
# def frases_titulos(frases):
#     return frases.title()
# lista_frases_titulos = list(map(frases_titulos,lista_frases))
# print("\nEstas son las frases empezando todas por mayúsculas: ",lista_frases_titulos)
##---------------------------------------------------------------------------------------------- 

##---------------------------------------------------------------------------------------------- DOBLE DE LOS NÚMEROS
# #Creamos una lista para añadir números con un while true para que termine solo cuando pongamos '0'.
# lista_numeros=[]
# while True:
#     numeros_lista = int(input("\nIntroduce números a continuación para obtener su doble, usando '0' para terminar: "))
#     if numeros_lista>0:
#         lista_numeros.append(numeros_lista)
#     elif numeros_lista<0:
#          lista_numeros.append(numeros_lista)  
#     elif numeros_lista ==0:
#         break 

# #Creamos la función que multplicará los números de la lista por 2 y usamos la función map() para que se aplique a toda la lista

# def numeros_doble(numeros_lista):
#     return numeros_lista * 2

# lista_numeros_dobles = list(map(numeros_doble, lista_numeros))
# print("\nEl doble de los números: ", lista_numeros_dobles)
##---------------------------------------------------------------------------------------------- 

##----------------------------------------------------------------------------------------------NUMEROS REDONDEADOS
#Creamos una lista para añadir números con un while true para que termine solo cuando pongamos '0'.
# lista_numeros=[]
# while True:
#     numeros_lista = float(input("\nIntroduce números decimales a continuación para obtener una lista con los números redondeados, usando '0' para terminar: "))
#     if numeros_lista>0:
#         lista_numeros.append(numeros_lista)
#     elif numeros_lista<0:
#          lista_numeros.append(numeros_lista)  
#     elif numeros_lista ==0:
#         break 

# #Creamos la función que redondea los números y usamos la función map() para que se aplique a toda la lista

# def numeros_redondeados(numeros):
#     return round(numeros)

# lista_numeros_redondeados = list(map(numeros_redondeados, lista_numeros))
# print("\nLos numeros redondeados son: ", lista_numeros_redondeados)
##----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------CONTAR LETRAS
# #Creamos una lista para añadir palabras con un while true para que termine solo cuando pongamos 'fin'.
# lista_palabras =[]
# while True:
#     palabras = str(input("\nIntroduce palabras a continuación, usando 'fin' para terminar: ")).lower()
#     if palabras !='fin':
#         lista_palabras.append(palabras)
#     if palabras =='fin':
#         break

# # Creamos la función que contará las letras de las palabras y usamos la función map() para que se aplique a toda la lista
# def longitud_palabras(palabras):
#     return len(palabras)
# lista_longitud_palabras = list(map(longitud_palabras,lista_palabras))
# print("\nEstas son las frases empezando todas por mayúsculas: ",lista_longitud_palabras)
# -------------------------------------------------------------------------------------------



# numeros = [4, 9, 16, 25, 1,7,12]


# def menor_de_10(n):
#     return n < 10  


# numeros_menores_10 = filter(menor_de_10, numeros)
# print(list(numeros_menores_10))  



# alturas = [1.60, 1.75, 1.80, 1.50]

# def alturas_en_centimetros(metros):
#     return metros * 100

# lista_en_centimetros = list(map(alturas_en_centimetros,alturas))
# print(lista_en_centimetros)
