from PIL import Image
import random

path_images = ".\\images\\"

def image_art():
    new_size = (400, 400)
    imagem = Image.new(size=new_size, mode="RGB", color="white")
    pixel_map=imagem.load()
    for i in range (imagem.width):
        for j in range(imagem.height):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            pixel_map[i,j] = (red, green, blue)
    imagem.show()
    imagem.save(path_images+'imageArt.jpg')

image_art()