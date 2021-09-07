import os
import time
from exer import review
from graf import *
from oxpciones import *

# Ingreso
indexing = input("Ingrese la clave: ")
con = 0
limit = 3

while indexing != review:

    if con <= limit:
        print(f"Queda {limit-con} intentos")

    else:
       time.sleep(3)
       exit()

    indexing = input(f"Error, clave incorrecta. \n Ingrese la clave nuevamente: ")
    con+=1


# Proceso a bienvenida
time.sleep(3)
os.system('clear')

print (welcome)
time.sleep(3)

print (logo)
time.sleep(3)

# uso
print (aviso)
opciones()
