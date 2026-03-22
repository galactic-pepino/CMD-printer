from PIL import Image

foto = input("Introduce la ruta completa de la imagen: ")

imagen = Image.open(foto).convert("L")

anchura_original = imagen.width
altura_original = imagen.height

factor = 2
anchura = anchura_original // factor
altura = int((altura_original // factor) * 0.5)  


imagen = imagen.resize((anchura, altura))

caracteres = ' .:-=+*#%@'

def caractear_imagen():
    for y in range(altura):          
        linea = ""                    
        for x in range(anchura):      
            valor_gris = imagen.getpixel((x, y))              
            indice = int((valor_gris / 255) * (len(caracteres)-1)) 
            linea += caracteres[indice]                         
        print(linea) 

caractear_imagen()