import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def validar_longitud(longitud):
    if longitud < 8 or longitud > 32:
        print("La longitud debe estar entre 8 y 32 caracteres.")
        return False
    return True

def main():
    longitud = int(input("¿Cuántos caracteres quieres que tenga la contraseña? "))
    if not validar_longitud(longitud):
        return
    
    contrasena = generar_contrasena(longitud)
    print("Aquí tienes tu contraseña generada aleatoriamente:")
    print(contrasena)

main()
