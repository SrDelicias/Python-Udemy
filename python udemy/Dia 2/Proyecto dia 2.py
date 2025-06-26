
nombre = input("Dime tu nombre: ")
valor = input("¿Cuánto has ganado?: ")

valor = int(valor) #tranformamos el string a un integer

comision = valor * 13/100
comision = round(comision, 2)

print(f"Buenas {nombre}, esta es tu comision {comision}€")

"""
Esto se puede abreviar mas aun, abajo lo hacemos.
"""

nombre = input("Dime tu nombre: ")
valor = int(input("¿Cuánto has ganado?: "))

comision = round(valor * 13/100, 2)

print(f"Buenas {nombre}, esta es tu comision {comision}€")

#Lo que hemos hecho es integrar el integer directamente antes del imput, asi se transforma en numero.
#tambien el redondeo los hemos puesto directo en la operacion.