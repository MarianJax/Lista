class Animal:
    def __init__(self, nombre, peso):
        self.__nombre = nombre
        self.__peso = peso

    def getNombre(self):
        return self.__nombre
    
    def getPeso(self):
        return self.__peso

class Perro(Animal):
    def __init__(self, nombre, peso):
        super().__init__(nombre, peso)

    def __repr__(self):
        return f"Perro (nombre={self.getNombre()}, peso={self.getPeso()})"  
    
    