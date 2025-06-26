

edad = input("Dime tu edad: ")

print(type(edad))

edad = int(edad)
nueva_edad = 1 + edad
print(nueva_edad)

print("Tu nueva edad sera: " + nueva_edad) #esto no se podria ya que hay un string y un integer y no puede juntarse, habria que formatear la cadena
