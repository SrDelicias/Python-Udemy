lista = ["a", "b", "c"]

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra: {numero_letra}: {letra}")

###################

lista2 = ["pablo", "laura", "julia", "alberto", "ana"]

for nombre in lista2:
    if nombre.startswith("l"):  #Esto es para dar enfasis en el nombre que empieza por L
        print(nombre)
    else:
        print("nombre que no empieza por l")

#############

numeros = [ 1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)

############

palabra = "python"

for letra in palabra:
    print(letra)

######################

dic = {"clave1":"a", "clave2":"b", "clave3":"c"}

for item in dic.items():  
    print(item)
for a,b in dic.items():
    print(a,b)