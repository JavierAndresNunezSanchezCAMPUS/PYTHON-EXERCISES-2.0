"""
1. Campus requiere administrar algunos datos de sus Campers
como por ejemplo, la creación, eliminación o búsqueda de los
developers, entre otros, por tal razón, ha solicitado el diseño de
un programa que cuente con el siguiente menú como panel de
control:
"""

print("-----------------------MENU-----------------------")
print("1. CREAR GRUPO ARTEMIS")
print("1.1 LISTAR CAMPERS DE ARTEMIS")
print("1.2 AGREGAR CAMPERS A ARTEMIS")
print("1.3 ELIMINAR CAMPERS DE ARTEMIS")
print("1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS")
print("1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS")
print("2. CREAR GRUPO SPUTNIK")
print("2.1 LISTAR CAMPERS DE SPUTNIK")
print("2.2 AGREGAR CAMPERS A SPUTNIK")
print("2.3 ELIMINAR CAMPERS DE SPUTNIK")
print("2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK")
print("2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK")


a = float(input("Digite opcion: "))
if a == 1.:
    print("-----------------------Crear grupo artemis-----------------------")
    name = input("Digite el nombre del grupo artemis: ")
    print(f"El grupo se llama {name}")

elif a == 1.1:
    print("-----------------------Listar campers de artemis-----------------------")
    list=['Roberto','Alicia','Daniel','Carlos','Vannessa']
    print(list)

elif a == 1.2:
    print("-----------------------Agregar campers a artemis-----------------------")
    list=['Roberto','Alicia','Daniel','Carlos','Vannessa']
    print(list)
    name = input("Digite el nombre del nuevo camper: ")
    list.insert(5,(name))
    print("El camper se ha añadido exitosamente:")
    print(list)

elif a == 1.3:
    print("-----------------------Eliminar campers de artemis-----------------------")
    list=['Roberto','Alicia','Daniel','Carlos','Vannessa']
    print(list)
    name = int(input("Digite la posicion del camper que desea eliminar: "))
    del list[(name)]
    print("El camper se ha eliminado exitosamente:")
    print(list)

elif a == 1.4:
    print("-----------------------Lista de artemis ordenada alfabeticamente-----------------------")
    list=['Roberto','Alicia','Daniel','Carlos','Vannessa']
    ordenados = sorted(list)
    print(ordenados)

elif a == 1.5:
    print("-----------------------Buscar campers en la lista de artemis-----------------------")
    list=['Roberto','Alicia','Daniel','Carlos','Vannessa']
    print(list)
    name = int(input("Digite la posicion del camper que desea buscar: "))
    print(list[name])
    print("CAMPER ENCONTRADO")

elif a == 2.:
    print("-----------------------Crear grupo sputnik-----------------------")
    name = input("Digite el nombre del grupo sputnik: ")
    print(f"El grupo se llama {name}")

elif a == 2.1:
    print("-----------------------Listar campers de sputnik-----------------------")
    list=['Sebastian','Javier','Juan','Andres','Daniel']
    print(list)

elif a == 2.2:
    print("-----------------------Agregar campers a sputnik-----------------------")
    list=['Sebastian','Javier','Juan','Andres','Daniel']
    print(list)
    name = input("Digite el nombre del nuevo camper: ")
    list.insert(5,(name))
    print("El camper se ha añadido exitosamente:")
    print(list)

elif a == 2.3:
    print("-----------------------Eliminar campers de sputnik-----------------------")
    list=['Sebastian','Javier','Juan','Andres','Daniel']
    print(list)
    name = int(input("Digite la posicion del camper que desea eliminar: "))
    del list[(name)]
    print("El camper se ha eliminado exitosamente:")
    print(list)

elif a == 2.4:
    print("-----------------------Lista de sputnik ordenada alfabeticamente-----------------------")
    list=['Sebastian','Javier','Juan','Andres','Daniel']
    ordenados = sorted(list)
    print(ordenados)

elif a == 2.5:
    print("-----------------------Buscar campers en la lista de sputnik-----------------------")
    list=['Sebastian','Javier','Juan','Andres','Daniel']
    print(list)
    name = int(input("Digite la posicion del camper que desea buscar: "))
    print(list[name])
    print("CAMPER ENCONTRADO")