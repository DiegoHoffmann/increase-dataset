import os
import PIL.Image
import matplotlib.pyplot as plt
from torchvision  import transforms


def salvarImagem(imagem, transform, title, nomefig, diretorioSalvar):    
    imagem = PIL.Image.open(imagem)
    fig, ax = plt.subplots(1, 2 , figsize=(20, 5))
    ax[0].set_title(f'Image Original')
    ax[0].imshow(imagem)

    imagem = transform(imagem)
    ax[1].set_title(title)
    ax[1].imshow(imagem)
    plt.savefig(diretorioSalvar + title + nomefig)

diretorio = os.getcwdb().decode('utf-8')
nome = 'bird.jpg'
imagem =  diretorio + '/imagens/originais/' + nome
diretorioSalvar = diretorio + '/imagens/geradas/'

randomCrop = transforms.RandomCrop(90)
salvarImagem(imagem, randomCrop, 'Cropping', nome, diretorioSalvar)

resize = transforms.Resize(400)
salvarImagem(imagem, resize, 'Scalling', nome, diretorioSalvar)

randomHorizontalFlip = transforms.RandomHorizontalFlip(1)
salvarImagem(imagem, randomHorizontalFlip, 'Flipping', nome, diretorioSalvar)

randomRotation = transforms.RandomRotation(45)
salvarImagem(imagem, randomRotation, 'Rotation', nome, diretorioSalvar)

nome = 'dog.jpeg'
imagem =  diretorio + '/imagens/originais/' + nome
randomAffine = transforms.RandomAffine(degrees=(0, 0),translate=(0.2, 0.5))
salvarImagem(imagem, randomAffine, 'Translate', nome, diretorioSalvar)

colorJitter = transforms.ColorJitter(hue=0.5)
salvarImagem(imagem, colorJitter, 'Hue', nome, diretorioSalvar)

grayscale = transforms.Grayscale(num_output_channels=3)
salvarImagem(imagem, grayscale, 'Grayscale', nome, diretorioSalvar)

