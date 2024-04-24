from customtkinter import CTkImage
from PIL import Image

def user():
    return CTkImage(Image.open('img/user-solid.png'))

def adm():
    return CTkImage(Image.open('img/book-solid.png'))

def relatorio():
    return CTkImage(Image.open('img/file-contract-solid.png'))