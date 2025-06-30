if 10 == 9:
    print("es correcto")
else:
    print("no es correcto")

####################

mascota = "loro"

if mascota == "gato":
    print("tienes un gato")
elif mascota == "perro":
    print("tienes un perro")
elif mascota == "pez":
    print("tienes un pez")
else:
    print("no se que animal tienes")

##########################

edad = 16
calificacion = 9

if edad < 18:
    print("eres menor de edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("No aprobado")
else:
    print("adulto")

###############
#se puede usar el "not, and y or" en vez del True y False.