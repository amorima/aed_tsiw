from PIL import Image

path_images = ".\\images\\"

def imageMoldura():
    imagem=Image.open(path_images+"imageArt.jpg")
    pixel_map=imagem.load()

    for i in range(imagem.width):
        for j in range(imagem.height):
            if j <20 or j > imagem.height-20:
                pixel_map[i,j]= (0, 0, 255)
            elif i <20 or i > imagem.height-20:
                pixel_map[i,j]= (0, 0, 255) 
    imagem.show()
    imagem.save(path_images+'moldura.jpg')

imageMoldura()