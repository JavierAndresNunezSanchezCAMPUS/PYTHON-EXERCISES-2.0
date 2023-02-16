"""
3. En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional. El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos.
"""

print("--------------VUELTA A ESPAÑA--------------")

sueldo = int and float(input("Sueldo básico por kilometro recorrido: "))
kilometrosr = int and float(input("Número de kilometros recorridos: "))
kilometroslider = int and float(input("Número de kilometros recorridos con camisa de lider: "))

print("VALOR TOTAL A PAGAR:")
resultado = (sueldo*kilometrosr)
print(resultado)

if kilometroslider > 1.800:
    print("Obtiene recargo de 20%")

if kilometrosr == 3.277:
    print("Ha ganado la vuelta a españa, ha recibo 700 millones de pesos")
