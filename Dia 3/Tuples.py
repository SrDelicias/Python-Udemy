mi_tuple = (1,2,3,4)   #tambien puede ser sin parentesis

mi_tuple = list(mi_tuple) #podemos cambiarlo a variable lista

print(type(mi_tuple))

######################

t = (1,2,3)
x,y,z = t
print(x,y,z)

#####################

t1 = (1,2,3,1)

print(t1.count(1)) #no dice cuantos hay del numero que queremos
print(t1.index(1))  #