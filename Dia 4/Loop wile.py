respuesta = "s"

while respuesta == "s":
    respuesta = input("Quieres segur? (s/n)")
else:
    print("Gracias")

#####
#si tenemos un while sin completar, podemos poner un pass
while respuesta == "s":
    pass

####

nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == "r":
        break
    print(letra)

#break lo que hace es parar hasta que ve la letra "r", tambien esta continue, que para en la letra " y continua con lo que sigue"