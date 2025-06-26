diccionario = {"c1":"valor1", "c2":"valor2"}
print(type(diccionario))

resultado = diccionario["c1"]
print(resultado)

######################

cliente = {"nombre":"Juan", "apellido":"Fuentes", "peso":88, "talla":1.78}
consulta = (cliente["peso"])
print(consulta)

########################

dic = {"c1":55, "c2":[10,20,30], "c3": {"s1":100, "s2":200}}
print(dic["c2"][1])

dic = {"c1":["a","b","c"], "c2":["d","e","f"]}
print(dic["c2"][1].upper()) #poner lo seleccionado en mayusculas

######################

dic1 = {1:"a", 2:"b"}
print(dic1)

dic1[3] = "c"   #modificar el diccionar, esta vez agregando un elemento mas
print(dic1)

dic1[2] = "B"   #modificamos uno ya existente
print(dic1)

print(dic1.keys())  #dice solo las keys que hay en el diccionario
print(dic1.values())  #muestra los valores solamente
print(dic1.items())  #muestra todo lo que hay en el diccionario