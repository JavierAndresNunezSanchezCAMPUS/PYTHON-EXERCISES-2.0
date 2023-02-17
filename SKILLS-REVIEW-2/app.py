"""
4. Una empresa tiene 500 almacenes. Cada almacén debe
reportar el nombre y 5 registros c/u, contiene el tipo de articulo
y el número de unidades vendidas de ese artículo.

Haga un programa en Python para determinar cuál fue el
almacén que mas vendió, cual fue el articulo más vendido de
ese almacén y cual el más vendido en general.
"""

print("-----------------------EMPRESA-----------------------\n")

print("-------------------Almacen de Ropa-------------------")
camisas = int(input("Camisas vendidas: "))
pantalones = int(input("Pantalones vendidos: "))
boxers = int(input("Boxers vendidos: "))
camisillas = int(input("Camisillas vendidas: "))
medias = int(input("Medias vendidas: "))


d1 = dict([
    ("Camisas",(camisas)), 
    ("Pantalones",(pantalones)), 
    ("Boxers",(boxers)), 
    ("Camisillas",(camisillas)), 
    ("Medias",(medias)),
])

print(d1)

print("-------------------Almacen de Frutas-------------------")
piñas = int(input("Piñas vendidas: "))
bananos = int(input("Bananos vendidos: "))
peras = int(input("Peras vendidas: "))
manzanas = int(input("Manzanas vendidas: "))
naranjas = int(input("Naranjas vendidas: "))

d2 = dict([
    ("Piñas",(piñas)), 
    ("Bananos",(bananos)), 
    ("Peras",(peras)), 
    ("Manzanas",(manzanas)), 
    ("Naranjas",(naranjas)),
])

print(d2)


ropavendida = ((camisas)+(pantalones)+(boxers)+(camisillas)+(medias))
frutavendida = ((piñas)+(bananos)+(peras)+(manzanas)+(naranjas))
print("ALMACEN QUE MÁS VENDIÓ: ")

if ropavendida > frutavendida:
    print("ALMACEN DE ROPA")
    print(ropavendida)

else: print("ALMACEN DE FRUTAS")
print(frutavendida)

# Solo pude hacer que imprimiera el almacen que más productos vendió, no supe hacer los otros 2 factores.
