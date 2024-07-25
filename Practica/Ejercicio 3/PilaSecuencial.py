import numpy as np

class pilaSecuencial:
    __pila = None
    __tope = None

    def __init__(self,dimension,tipo):
        self.__pila = np.empty(dimension,dtype = tipo)
        self.__tope = 0

    def insertar(self,nuevoElemento):

        if(self.lleno() == False):
            self.__pila[self.__tope] = nuevoElemento
            self.__tope += 1
        else:
            raise OverflowError('La pila esta llena')
    
    def desapilar(self):
        aux = None
        if(self.vacio() == False):
            self.__tope -=1
            aux = self.__pila[self.__tope]
            self.__pila[self.__tope] = None
        else:
            print('La pila no posee elementos')
        return aux

    def eliminar(self):

        if(self.vacio() == False):
            self.__pila[self.__tope-1] = None
            self.__tope -=1
        else:
            print('No hay nada que eliminar')
    
    def lleno(self):
        return (len(self.__pila) == self.__tope)
    
    def vacio(self):
        return (self.__tope == 0)

