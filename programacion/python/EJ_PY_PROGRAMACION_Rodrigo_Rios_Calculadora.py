# calculadora
import math
operacion = str(input("¿Qué operación quieres hacer? "))
if operacion =='sumar' or operacion == 'restar' or operacion =='producto' or operacion =='cociente':
    numero1 = float(input("Dime el primer número: "))
    numero2 = float(input("Dime el primer número: "))
if operacion =='raiz':
    numeroraiz = float(input("Introduce un número para obtener su raíz cuadrado: "))
if operacion =='sen' and operacion !='raiz':
    numerosen = int(input("Introduce un número para calcular su seno: "))
    senradians = math.radians(numerosen)
if operacion =='cos' and operacion !='raiz':
    numerocos = int(input("Introduce un número para calcular su coseno: "))
    cosradians = math.radians(numerocos)
if operacion =='tan' and operacion !='raiz':
    numerotg = int(input("Introduce un número para calcular su tangente: "))
    tgradians = math.radians(numerotg)

operacion_final = operacion.lower()

match operacion_final:
    case "sumar":
        resultado = numero1 + numero2
        print("La suma da", resultado)
    case "restar":
        resultadoresta = numero1 - numero2
        print("La resta da", resultadoresta)
    case "multiplicar":
        resultadoproducto = numero1 * numero2
        print("El producto da", resultadoproducto)
    case "dividir":
        if numero2 == 0:
            print("Error")
        else:
            resultadocociente = numero1 / numero2
            print("La division da", resultadocociente)
    case 'raiz':
        resultadoraiz = math.sqrt(numeroraiz)  
        print("La raiz cuadrada de",numeroraiz, "es", resultadoraiz)
    case'sen':
        resultadoseno = math.sin(senradians)
        print("El seno de", numerosen, "es", resultadoseno)
    case'cos':
        resultadocoseno = math.cos(cosradians)
        print("El coseno de", numerocos, "es", resultadocoseno)
    case'tan':
        resultadotangente = math.tan(tgradians)
        print("La tangente de", numerotg, "es", resultadotangente)

    case _:
        print("Introduce una función disponible (Suma, Resta, Producto, Cociente, Raíz, sen, cos o tg)")



# #++++++++++++++++++++++++++++++++++++++++FECHA
# import datetime
# fecha = datetime.datetime.now()
# print(fecha)
# #++++++++++++++++++++++++++++++++++++++++ 


# while True:
#     try:
#         suma = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")


# Esto es el ejercicio de la division



# num = int(input("Dime un número: "))

# if num % 2 == 0:
#     print("El número es par")
# else:
#     print("El número es impar")





# suma


# i = int(input("Dime un numero de tipo NNN: "))
# if i <=0:
#     print("no es posible")
# else:
#     suma = 0
#     for i in range(1, i + 1):
#         suma +=i
#         print("el resultado es", suma)





# texto = str(input("Escribe una cadena de texto para que pueda contar las vocales: "))
# num = len(texto)
# print(num)


# numeros = [1, 2, 3, 4, 5]
# suma = 0

# for numero in range(1,6):
#     suma += numero

# print("La suma es", suma)


# contar numeros pares


# num = int(input("Dime un número entero positivo: "))
# contador = 0
# for numero in range(1,num+1):
#     if numero % 2 == 0:
#         contador +=1

# print("Hay",contador,"números pares entre 1 y", num)



# suma hasta uno negativo

# num = int(input("Dame un numero entero: "))
# suma = num
# while num > 0:
#     num = int(input("Dame un numero entero positivo: "))
#     if num <0:
#         break
#     suma += num
# print("La suma total es", suma)

# TABLA DE MULTIPLICAR

# num = int(input("Dime un número entero positivo"))
# contador = 0
# if num >0:
#     for numero in range(1,11):
#         numero = num * numero
#         contador +=1
#         print(num, "x", contador, "=", numero)
# else:
#     print("HE DICHO ENTERO POSITIVO")

# ADIVINAR EL NUMERO


# import random 

# num = random.randint(1,100)
# num2 = int(input("Intenta adivinar el número: "))

# while num2 != num:
#     if num2 > num:
#         print("Demasiado alto")
#     elif num2 < num:
#         print("Demasiado bajo")
    
#     num2 = int(input("Intenta adivinar el número: "))

# print("SIUUUUUUUUUU")    





# palabra = str(input("Dime una palabra: "))
# palabra2 = reversed(palabra)
# for palabra_inversa in palabra2:
#         print(palabra_inversa)




# playlist = []

# cancion = input("Introduce el nombre de la canción: ")
# while cancion != "fin":
#     playlist.append(cancion)
#     cancion = input("Introduce el nombre de otra canción: ").lower()

# print(playlist)

# for i in range(len(playlist)):
#     print(f"{i}.-{playlist[i]}")

# cancion_reproduciendo = int(input("Dime el número de la canción a escuchar"))

# print(f"Estás escuchando :{playlist[cancion_reproduciendo]}")





# canciones = [[input("dime otra cancion")]]
# print(canciones)



