from PIL import Image

path_images = ".\\images\\"

new_size=(240, 240)
imagem=Image.new(size=new_size, mode="RGB", color="white")

def franca():
    pixel_map=imagem.load()
    for i in range(imagem.width):
        for j in range(imagem.height):
            if i <80:
                pixel_map[i,j]= (0, 0, 255)
            elif i < 160:
                pixel_map[i,j]= (255, 255, 255)
            else:
                pixel_map[i,j]= (255, 0, 0)

    imagem.show()
    imagem.save(path_images+'bandeira.jpg')

franca()