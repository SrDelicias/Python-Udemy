mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
mi_lista3 = mi_lista + mi_lista2

mi_lista3[0] = "alfa" #sobre escribles el elemento de la lista seleccionado
mi_lista3.append("g") #agregas un elemento a la lista original
mi_lista3.pop(2) #eliminas un elemento de la lista, si dejas el parentesis vacio elimina el ultimo elemnto de la lista
eliminado = mi_lista3.pop(2) #sacas de la lista el elemento entre parentesis

print(mi_lista3)
print(eliminado)


lista = ["g", "o", "b", "m", "c"]
lista.sort()  #ordena la lista alfabeticamente
lista.reverse()  #ordena la lista alfabeticamente del reves
print(lista)