# -------------------------------------------------------PLAYLIST
# playlist = []

# cancion = input("Introduce el nombre de la canción: ")
# while cancion != "fin":
#     playlist.append(cancion)
#     cancion = input("Introduce el nombre de otra canción: ").lower()

# print(playlist)

# for i in range(len(playlist)):
#     print(f"{i}.-{playlist[i]}")

# cancion_reproduciendo = int(input("Dime el número de la canción a escuchar: "))

# print(f"Estás escuchando:{playlist[cancion_reproduciendo]}")
# --------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------agenda
# dic1 ={}
# while True:
#     nombre = input("introduce el nombre: ").lower()   
#     if nombre != 'fin':
#         tlf = int(input("Introduce su número de teléfono: "))
#         dic1[nombre] = tlf
#     else:
#         break

# print(dic1)

# cambios_busqueda = (str(input("¿Quieres cambiar algo O Encontrar a alguien?  ")))
# if cambios_busqueda !="no":
#     nombre_busqueda = input("introduce el nombre: ").lower() 
#     tlf_busqueda= input("introduce el número de teléfono: ")
#     dic1[nombre_busqueda] = tlf_busqueda
#     print(dic1)
# else:
#     print("Perfecto, esta es tu agenda", dic1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------------ITINERARIO DE VIAJE
# itinerario = ("Madrid", "Barcelona", "Bilbao", "Roma", "Paris")
# print("Este es mi itinerario de viaje...")
# for i in range(len(itinerario)):
#     print(f"{i}.-{itinerario[i]}")

# ciudad_visita =int(input("Selecciona el número de la ciudad que quieras visitar tú: "))
# print("Has seleccionado:", (itinerario[ciudad_visita]))
# ---------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------ASIGNATURAS
# lista = []
# suma = 0
# dic1 = {}
# contador = 0
# while True:
#     asig = str(input("introduce el nombre de la asignatura: ")).lower()   
#     if asig != 'fin':
#         nota = int(input("Introduce la calificación de la asignatura: "))
#         dic1[asig] = nota
#         lista.append(asig)
#         suma = suma + nota
#         contador = contador + 1
#     else:
#         break

# print("Estas son tus calificaciones")
# print(dic1)

# media = suma / contador
# print("Tu nota media es:", media )
# -----------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------MENU
# menu = {
#     "Café": (1.5, 50),
#     "Té": (1.0, 0),
#     "Bocadillo": (3.0, 300),
#     "Ensalada": (2.5, 150)
# }


# print("Menú:")
# for producto, (precio, calorias) in menu.items():
#     print(f"- {producto}: {precio}€ ({calorias} cal)")

# pedido = []
# total_precio = 0
# total_calorias = 0

# while True:
#     producto = input("\nIngresa el nombre del producto que deseas agregar (o 'fin' para terminar): ")
#     if producto == 'fin':
#         break
#     elif producto in menu:
#         pedido.append(producto)
#         total_precio += menu[producto][0]
#         total_calorias += menu[producto][1]
#     else:
#         print("Producto no disponible. Por favor, elige otro.")

# print("\nTu pedido:")
# for item in pedido:
#     print(f"- {item}")

# print(f"\nTotal a pagar: {total_precio}€")
# print(f"Calorías totales: {total_calorias} cal")


    











