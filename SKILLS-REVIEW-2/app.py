"""
2. N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.

Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.

Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros.
"""

print("----------JUEGOS OLIMPICOS 2022----------")

print("----------NOMBRES DE LOS ATLETAS FINALISTAS----------")

nombre1 = input("Escriba el nombre del atleta 1: ")
nombre2 = input("Escriba el nombre del atleta 2: ")
nombre3 = input("Escriba el nombre del atleta 3: ")

print("----------MARCAS DEL SALTO EN METROS DE LOS ATLETAS----------")

salto1 = int(input("Digite el salto del atleta 1: "))
salto2 = int(input("Digite el salto del atleta 2: "))
salto3 = int(input("Digite el salto del atleta 3: "))

if  salto1 > salto2 and salto3:     
        if salto1 > 15.50:
                print(f"El atleta {nombre1} ha rompido el record, recibió 500 millones")
        print(f"GANADOR {nombre1}, ha ganado la medalla de oro")

elif salto2 > salto3 and salto1:
        if salto2 > 15.50:
                print(f"El atleta {nombre2} ha rompido el record, recibió 500 millones")
        print(f"GANADOR {nombre2}, ha ganado la medalla de oro")

elif salto3 > salto1 and salto2:
        if salto3 > 15.50:
                print(f"El atleta {nombre3} ha rompido el record, recibió 500 millones")
        print(f"GANADOR {nombre3}, ha ganado la medalla de oro")

else:
    print("Ha habido un empate entre los atletas")
