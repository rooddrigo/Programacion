# mi_nombre = "Rodrigo"
# mi_edad = "17"
# print("Mi nombre es", mi_nombre)
# print("Tengo",mi_edad,"Años")


# lado = 5
# area = lado * lado
# print("El área del cuadrado es",area)


# edad = 17
# es_adulto = edad >= 18
# print("Es adulto?", es_adulto)


# edad = input("Introduce tu edad: ")
# edad = int(edad)
# edad_futura = edad + 10
# print("En 10 años tendrás:", edad_futura, "años")

# nombre = "Rodrigo"
# apellido = "Ríos"
# nombre_completo = nombre + " " + apellido
# print(nombre_completo)

# frase = "Hola cara de cola "
# repetida = frase * 3
# print(repetida)

# frase = "Python"
# longitud = len(frase)
# print(longitud)


# frase = "poa"
# letra = frase[6]
# print(letra)



# dia = str(input("dime que dia es hoy:"))
# dia_normal = dia.lower()

# match dia_normal:
#     case "lunes":
#         print("Hoy es lunes")
#     case "martes":
#         print("Hoy es martes")
#     case _:
#         print("Es otro día de la semana")


# edad = int(input("¿Cuál es tu edad?"))
# if edad < 5:
#     print("Tu entrada es gratuita")
# elif edad >= 5 and edad <= 12:
#     print("Tu entrada cuesta 5 euros")
# elif edad >= 13 and edad <= 17:
#     print("Tu entrada cuesta 7 euros")
# else:
#     print("Tu entrada cuesta 10 euros")


# nota = int(input("Dime tu nota"))

# match nota:
#     case 90:
#         print("La calificación obtenida es A")
#     case 80:
#         print("La calificación obtenida es B")
#     case 70:
#         print("La calificación obtenida es C")


# nota = int(input("Dime tu nota"))

# if nota >= 90:
#     print("La calificación obtenida es A")
# elif nota >= 80 and nota <= 90:
#     print("La calificación obtenida es B")
# elif nota >= 70 and nota <= 80:
#     print("La calificación obtenida es C")
# elif nota >= 60 and nota <= 70:
#     print("La calificación obtenida es D")
# else:
#     print("La calificación obtenida es F")



# dia = int(input("Dime un número del 1-7: "))

# match dia:
#     case 1:
#         print("Hoy es lunes")
#     case 2:
#         print("Hoy es Martes")
#     case 3:
#         print("Hoy es Miercoles")
#     case 4:
#         print("Hoy es Jueves")
#     case 5:
#         print("Hoy es Viernes")
#     case 6:
#         print("Hoy es Sabado")
#     case 7:
#         print("Hoy es Domingo")
#     case _:
#         print("Número invalido")


# edad = int(input("¿Cuál es tu edad?"))



# if edad < 12:
#      print("Niño")
# elif edad >= 12 and edad <= 17:
#      print("Adolescente")
# elif edad >= 18 and edad <= 59:
#      print("Adulto")
# else:
#      print("Adulto mayor")

# idioma = str(input("¿Cuál es tu idioma preferido?"))


# match idioma:
#      case "es":
#         print("Buenos dias")
#      case "en":
#         print("Good morning")
#      case "fr":
#           print("Bonjour")
#      case _:
#           print("Idioma no valido")



# vehiculo = str(input("¿Qué tipo de vehículo quieres?"))
# vehiculo_total = vehiculo.lower()
# if vehiculo_total == "coche":
#     print("Vehículo de 4 ruedas")
# elif vehiculo_total == "moto":
#     print("Vehículo de 2 ruedas")
# elif vehiculo_total == "bici":
#     print("Vehículo no motorizado")
# else:
#     print("Tipo de vehículo no reconocido")

# color = str(input("¿Qué color quieres?"))
# color_total = color.lower()
# match color_total:
#     case "rojo":
#         print("Has seleccionado el color rojo")
#     case "azul":
#         print("Has seleccionado el color azul")
#     case "verde":
#         print("Has seleccionado el color verde")
#     case _:
#         print("Color no disponible")


# numero1 = float(input("Dime el primer número"))
# numero2 = float(input("Dime el primer número"))

# operacion = str(input("¿Qué operación quieres hacer?"))
# operacion_final = operacion.lower()

# match operacion_final:
#     case "sumar":
#         resultado = numero1 + numero2
#         print("La suma da", resultado)
#     case "restar":
#         resultadoresta = numero1 - numero2
#         print("La resta da", resultadoresta)
#     case "multiplicar":
#         resultadoproducto = numero1 * numero2
#         print("El producto da", resultadoproducto)
#     case "dividir":
#         if numero2 == 0:
#             print("Error")
#         else:
#             resultadocociente = numero1 / numero2
#             print("La division da", resultadocociente)
#     case _:
#         print("Selecciona una operación permitida")


