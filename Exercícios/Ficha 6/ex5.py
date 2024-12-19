from PIL import Image

path_images = ".\\images\\"

def imageJanela():
    imagem=Image.open(path_images+"teste.jpeg")
    pixel_map=imagem.load()

    for i in range(imagem.width):
        for j in range(imagem.height):
            if j <=10 or j > imagem.height-10:
                pixel_map[i,j]= (0, 0, 255)
            elif i <=10 or i > imagem.height-10:
                pixel_map[i,j]= (0, 0, 255)
            elif int(imagem.width/2)-5<=i and i<=int((imagem.width/2)+5):
                pixel_map[i,j]= (0, 0, 255)
            elif int(imagem.height/2)-5<=j and j<=int((imagem.height/2)+5):
                pixel_map[i,j]= (0, 0, 255)
    imagem.show()
    imagem.save(path_images+'janela.jpg')

imageJanela()