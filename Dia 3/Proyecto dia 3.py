texto = "Hola a todos, mi nombre es Alberto, estamos bien"
texto1 = texto.lower()
palabras = ["a", "b", "c"]

print(texto1.index("a"))

texto1 = texto1.split()
print(len(texto1))

print(texto1[0:1])
print(texto1[::-1])

print("Python" in texto1)
