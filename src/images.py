from customtkinter import CTkImage
from PIL import Image

def user():
    return CTkImage(Image.open('img/user-solid.png'))

def adm():
    return CTkImage(Image.open('img/book-solid.png'))

def relatorio():
    return CTkImage(Image.open('img/file-contract-solid.png'))

def registro_ok():
    return CTkImage(Image.open('img/check-to-slot-solid.png'))

def registro_erro():
    return CTkImage(Image.open('img/square-xmark-solid.png'))