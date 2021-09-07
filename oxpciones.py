import webbrowser
import os
import time
import platform



aviso = ("""A continuación escriba la opción que desea.
    1. Acceder a google                  3. Salir
    2. Acceder a Youtube                 4. Salir y apagar """)


def opciones():

    opcion = int(input("> : " ))

    while (opcion <= 0 or opcion >= 5):
        print("Opción Incorrecta \n Introduzca una opción valida")
        opcion = int(input("> : "))

    if (opcion == 1):
        print("Accediendo a Google ...")
        webbrowser.open('https://www.google.com')

    elif (opcion == 2):
        print("Accediendo a Youtube ...")
        webbrowser.open('https://www.youtube.com')

    elif (opcion == 3):
        print("Cerrando ...")
        time.sleep(2)
        exit()

    else:
        syso = platform.system()
        print("El programa se cerrará. \n El equipo se apagará.")
        time.sleep(2)

        if (syso == "Windows"):
            os.system('shutdown /s /t 200')

        elif (syso == "Linux"):
            os.system('shutdown 3')
        exit()

