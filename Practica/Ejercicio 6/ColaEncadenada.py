from ClaseNodo import nodo

class ColaEncadenada:
    __comienzo = None
    __actual = None

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
    
    def insertar(self,elemento):
        nuevoElemento = nodo(elemento)
        if self.vacio():
            self.__comienzo = nuevoElemento
            self.__actual = self.__comienzo
        else:
            self.__actual.setSiguiente(nuevoElemento)
            self.__actual = nuevoElemento
    
    def suprimir(self):
        if self.vacio():
            print('La cola esta vacia')
        else:
            self.__comienzo = self.__comienzo.getSiguiente()
            if self.vacio():
                self.__actual = self.__comienzo
    
    def obtenerPrimer(self):
        dato = None
        if self.vacio():
            print('La cola esta vacia')
        else:
            aux = self.__comienzo.getDato()
            self.__comienzo = self.__comienzo.getSiguiente()
            if self.vacio():
                self.__actual = self.__comienzo
        return dato
    
    def vacio(self):
        return self.__comienzo == None

        

