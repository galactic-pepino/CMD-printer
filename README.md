ASCII Image Converter

Este proyecto convierte cualquier imagen a una versión ASCII art que se puede imprimir en la consola.

📦 Requisitos
Python 3.x
Librería Pillow (para manejar imágenes)

Instalación de Pillow:

pip install Pillow
🖼 Uso
Coloca la imagen que quieres convertir en tu computadora y guarda la ruta.
Modifica la variable foto en el script con la ruta de tu imagen.
Ejecuta el script.
python tu_script.py
La imagen se convertirá a escala de grises y se redimensionará proporcionalmente para la consola.
Cada píxel se representa con un carácter ASCII según su brillo.
⚙️ Personalización

Carácteres ASCII: puedes cambiar la variable caracteres para usar más o menos detalle.

caracteres = ' .:-=+*#%@'
Factor de reducción: ajusta factor para que la imagen sea más grande o más pequeña en la consola.
Proporción vertical: el valor 0.5 en la altura corrige la proporción porque los caracteres no son cuadrados.
📝 Explicación del flujo
Abrir imagen y convertir a gris (Image.open().convert("L")).
Obtener tamaño original y calcular tamaño proporcional.
Redimensionar la imagen (.resize()).
Recorrer cada píxel con getpixel((x, y)).
Convertir el valor de gris a un carácter ASCII.
Imprimir cada línea para formar la imagen completa.
