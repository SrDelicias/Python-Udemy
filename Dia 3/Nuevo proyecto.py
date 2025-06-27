texto = input("Escribe un texto: ")
letras = []
veces = 3

for vez in range(veces):
    letras.append(input("Escribe una letra: ").lower())


print("\n")
print("Canitdad de letras")
print("\n")
texto1 = texto.count(letras[0])
texto2 = texto.count(letras[1])
texto3 = texto.count(letras[2])

print(f"Hemos encontrado la cantidad de {letras[0]} en el texto {texto1} veces")
print(f"Hemos encontrado la cantidad de {letras[1]} en el texto {texto2} veces")
print(f"Hemos encontrado la cantidad de {letras[2]} en el texto {texto3} veces")

print("\n")
print("Cuantas palabra hay en el texto")
print("\n")
palabras = texto.split()
print(f"El texto se compone de {len(palabras)} palabras")

print("\n")
print("La primera letra y la ultima")
print("\n")
letra = texto
print(f"La pirmera letra es {letra[0]} y la ultima es {letra[-1]}")

print("\n")
print("El texto del revés")
print("\n")
