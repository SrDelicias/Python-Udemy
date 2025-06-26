texto = "Este es el texto de Alberto"

resultado = texto.upper() #pasar todo a mayusculas
resultado = texto.lower() #pasar todo a minusculas
resultado = texto.split() #pasar todo a añadir como una lista
#si en el parentesis del split ponemos una letra, hace de separacion en la lista, no aparece en el resultado
resultado = texto.find("s") #es buscar dentro del texto donde esta.
resultado = texto.replace("Alberto", "Guapo") #reemplaza la primera palabra por la segunda que ponemos

print(resultado)


a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d]) #anade los elemenos a una lista y lo forma como una frase

print(e)