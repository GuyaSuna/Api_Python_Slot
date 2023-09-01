from flask import Flask, jsonify, send_file
import random
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def randomizar():
    iconos_elegidos = [None] * 20 
    for i in range(20):
        numero = random.randint(1, 30)
        if numero == 1:
            iconos_elegidos[i] = 1
        elif numero == 2:
            iconos_elegidos[i] = 0
        else:
            iconos_elegidos[i] = random.randrange(2, 8)
    random.shuffle(iconos_elegidos)
    return iconos_elegidos

@app.route('/get_images_and_orders', methods=['GET'])
def get_images_and_orders():
    nombres_iconos = ["Imagenes_Maquina/7.webp", "Imagenes_Maquina/Bar.webp", "Imagenes_Maquina/Banana.webp", "Imagenes_Maquina/Bell.webp", "Imagenes_Maquina/Cherry.webp", "Imagenes_Maquina/Grape.webp", "Imagenes_Maquina/Lemon.webp", "Imagenes_Maquina/Orange.webp", "Imagenes_Maquina/Watermelon.webp"]

    imagenes = []
    ordenes = []

    for _ in range(5):
        iconos_elegidos = randomizar()
        imagen_fusionada = Image.new("RGBA", (79, 79 * 20))

        for i, indice in enumerate(iconos_elegidos):
            y = i * 79
            icono = Image.open(nombres_iconos[indice])
            imagen_fusionada.paste(icono, (0, y))

        imagen_path = f"C:\\Users\\xxxia\\Desktop\\React\\Trabajos_Next\\app-prueba\\public\\Imagenes\\imagen_fusionada{_ + 1}.png"
        imagen_fusionada.save(imagen_path)
        orden_iconos = [nombres_iconos[indice] for indice in iconos_elegidos]
        
        imagenes.append(imagen_path)
        ordenes.append(orden_iconos)

    return jsonify({
        'images_urls': ['imagen_fusionada1.png', 'imagen_fusionada2.png', 'imagen_fusionada3.png', 'imagen_fusionada4.png', 'imagen_fusionada5.png'],
        'orders': ordenes
    })


if __name__ == '__main__':
    app.run(debug=True)
