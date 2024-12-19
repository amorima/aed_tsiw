from PIL import Image

path_images = ".\\images\\"

def imageGrayScale():
    imagem=Image.open(path_images+"imageArt.jpg")
    pixel_map=imagem.load()

    for i in range(imagem.width):
        for j in range(imagem.height):
            p = pixel_map[i,j]
            red = p[0]
            green = p[1]
            blue = p[2]
            red = green = blue = int(0.299 * red + 0.587 * green + 0.144 * blue)
            pixel_map[i,j] = (red, green, blue)
    imagem.show()
    imagem.save(path_images+'grayscale.jpg')

imageGrayScale()