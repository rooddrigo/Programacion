# ------------------------------------------------------------Adivinar el número con while
# import random 

# num = random.randint(1,100)
# num2 = int(input("Intenta adivinar el número: "))

# while num2 != num:
#     if num2 > num:
#         print("Demasiado alto")
#     elif num2 < num:
#         print("Demasiado bajo")
    
#     num2 = int(input("Intenta adivinar el número: "))

# print("Enhorabuena, has adivinado el número")    
# -------------------------------------------------------------------



# -------------------------------------------------------------Suma NNN
# i = int(input("Dime un numero de tipo NNN: "))
# if i <=0:
#     print("no es posible")
# else:
#     suma = 0
#     for i in range(1, i + 1):
#         suma +=i
#         print("el resultado es", suma)
# ----------------------------------------------------------------


# -----------------------------------------------------------------------------Numero Par o impar
# num = int(input("Dime un número: "))

# if num % 2 == 0:
#     print("El número es par")
# else:
#     print("El número es impar")
# --------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------Calculadora
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
# ------------------------------------------------------------------------------------------





# ----------------------------------------------------------Contar vocales
# cadena = str(input("Ingresa una cadena de texto: "))
# vocales = "aeiouAEIOU"
# contador = sum(1 for caracter in cadena if caracter in vocales)
# print("La cantidad de vocales en la cadena es: ",contador)
# -------------------------------------------------------------------------