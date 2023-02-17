"""
4. Una empresa tiene 500 almacenes. Cada almacén debe
reportar el nombre y 5 registros c/u, contiene el tipo de articulo
y el número de unidades vendidas de ese artículo.

Haga un programa en Python para determinar cuál fue el
almacén que mas vendió, cual fue el articulo más vendido de
ese almacén y cual el más vendido en general.
"""

print("-----------------------EMPRESA-----------------------\n")

print("-------------------Almacen de Ropa-------------------\n")

d1 = dict([
    ("Camisas",70), 
    ("Pantalones",40), 
    ("Boxers",30), 
    ("Camisillas",30), 
    ("Medias",100),
])

moreVR = max(d1,key=d1.get)

print(d1)

total=sum(d1.values())
print("TOTAL DE UNIDADES VENDIDAS EN EL ALMACEN DE ROPA:\n")
print(total)

print("-------------------Almacen de Frutas-------------------\n")

d2 = dict([
    ("Piñas",50), 
    ("Bananos",90), 
    ("Peras",80), 
    ("Manzanas",40), 
    ("Naranjas",70),
])

moreVF = max(d2,key=d2.get)

print(d2)

total2=sum(d2.values())

totald1=sum(d1.values())
totald2=sum(d2.values())


print("TOTAL DE UNIDADES EN EL ALMACEN DE FRUTAS CON MÁS ARTICULOS VENDIDOS:\n")
print(total2)
print("----------------------------------------------------------")
print(f"El almacen que más vendió fue el de frutas con {total2} unidades\n")
print(f"El articulo más vendido de este almacén fue {moreVF} con 90 unidades\n")
print(f"El articulo más vendido en general es {moreVR} con 100 unidades\n")
print("-----------------|> Fin del comunicado <|-----------------")
