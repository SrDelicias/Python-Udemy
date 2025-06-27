mi_set = set([1,2,3,4,5,]) #no mostrara si hay elementos iguales dentro del set
print(type(mi_set))
print(mi_set)


###################

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2) #unir los elementos

print(s3)

##################

c1 = {1,2,3}

c1.add(4)  #agregar un dato al set
c1.remove(2)  #elimina un dato al set
c1.discard(2) #elimina un dato al set, pero si descarta uno que no existe, no da error en el terminal
c1.pop()  #elimina un elemento aleatorio si no hay nada entre parentesis, esta bien para sorteos
c1.clear()  #vacia el set

print(c1)