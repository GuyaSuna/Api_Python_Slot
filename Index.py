import random
from PIL import Image
from flask import  jsonify

# Lista de nombres de las imágenes de iconos

nombres_iconos = ("Imagenes_Maquina/7.webp", "Imagenes_Maquina/Bar.webp", "Imagenes_Maquina/Banana.webp", "Imagenes_Maquina/Bell.webp", "Imagenes_Maquina/Cherry.webp", "Imagenes_Maquina/Grape.webp", "Imagenes_Maquina/Lemon.webp", "Imagenes_Maquina/Orange.webp", "Imagenes_Maquina/Watermelon.webp")
iconos_elegidos = [None] * 9  # Inicializar la lista con 9 elementos vacíos

# Cargar imágenes de iconos elegidos
for i in range(9):
    numero = random.randint(1, 30)
    if numero == 1:
        iconos_elegidos[i] = 1
    elif numero == 2:
        iconos_elegidos[i] = 0
    else:
        iconos_elegidos[i] = random.randrange(2, 8)

# Mezclar aleatoriamente el orden de los iconos elegidos
random.shuffle(iconos_elegidos)

# Tamaño de cada icono (79x79)
ancho_icono = 79
alto_icono = 79

# Crear una nueva imagen larga para los iconos fusionados
ancho_total = ancho_icono
alto_total = alto_icono * 9
imagen_fusionada = Image.new("RGBA", (ancho_total, alto_total))

# Colocar cada icono en la imagen fusionada
for i, indice in enumerate(iconos_elegidos):
    y = i * alto_icono
    icono = Image.open(nombres_iconos[indice])  # Cargar imagen basada en el índice
    imagen_fusionada.paste(icono, (0, y))

# Guardar la imagen fusionada
imagen_fusionada.save("imagen_fusionada.png")

# Guardar el orden de los íconos para controlar el puntaje
orden_iconos = [nombres_iconos[indice] for indice in iconos_elegidos]
print("Orden de íconos:", orden_iconos)
