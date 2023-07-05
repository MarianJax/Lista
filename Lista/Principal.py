from Animal import Perro
from Lista import List 

animales = []
lista = List()

while True:
    print("********* MENÚ ************")
    print("1. Agregar elemento")
    print("2. Mostrar lista")
    print("3. Eliminar ultimo elemento")
    print("4. Vaciar lista")
    print("5. Invertir lista")
    print("6. Tamaño de lista")
    print("7. Salir")
    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del elemento: ")
            peso = float(input("Ingrese el peso del elemento: "))
            perro = Perro(nombre, peso)
            lista.agregar_elementos(animales, perro)
        case "2":
            lista.mostrar_elementos(animales)
        case "3":
            lista.metodo_pop(animales)
        case "4":
            lista.vaciar_lista(animales)
        case "5":
            lista.invertir_lista(animales)
        case "6":
            lista.tamaño_Lista(animales)
        case "7":
            print("Saliendo del programa...")
            break
