
name = (input("Ingresa tu nombre: "))
info = (f"Hola, {name}, vamos a probar unas cuantas cosas.")

print (info)
number = int(input("Ingresa el número: "))

def gen_pass(name,number):

  passwd = (f"{name[2]+name[3]}{number}")
  return passwd 

review = gen_pass(name,number)
print (f"Su clave es: {review}")









