
class List():
    def agregar_elementos(selft, L, Animal):
        L.append(Animal)

    def mostrar_elementos(selft, L):
        print("La lista es: ", L)

    def vaciar_lista(self, L):
        L.clear()
        print("La lista es: ", L)

    def invertir_lista(self, L):
        L.reverse()
        print("La lista invertida es: ", L)

    def metodo_pop(self, L):
        print("El pop elimina a: ", L.pop())

    def tamaño_Lista(self, L):
        print("El tamaño de la lista: ", len(L))

