import time
import qrcode
import sys

def generado_Codigo():
    print("***********************************************************************************************")
    print("Hola mundo! Soy fcoterroba, puedes visitar mi web en www.fcoterroba.com")
    time.sleep(2)
    print("Este es un programa que te pide un enlace o texto y te genera un código QR en formato PNG.")
    time.sleep(3)
    codificar = input(f"COMENCEMOS!\n¿Qué palabra o enlace quieres que te codifique en QR? ")
    print("Codificando...")
    time.sleep(3)
    img = qrcode.make(codificar)
    f = open(codificar+"_QR.png", "wb")
    img.save(f)
    print(f"LISTO!\nTienes la imagen correctamente creado con el nombre {codificar}_QR.png")
    time.sleep(2)
    preguntar_Opcion()

def preguntar_Opcion():
    opcion = input(f"¿Qué quieres hacer ahora? (H)acer otro código | (S)alir del programa\n")
    if opcion=='h' or opcion=='H':
        generado_Codigo()
    else:
        time.sleep(0.4)
        print("Hasta pronto! No olvides visitar mi web www.fcoterroba.com")
        sys.exit()

generado_Codigo()
