import numpy as np
from ClaseNodo import nodo

class ListaSecuencial:
    __componentes = None
    __cabeza = None
    __actual = None
    __EspLibres = None

    def __init__(self,dimension):
        self.__componentes = np.empty(dimension, dtype= nodo)
        self.__EspLibres = 0
        self.__cabeza = -1
        self.__actual = None
        self.__cantidad = 0
        for i in range(dimension-1):
            self.__componentes[i] = nodo(None,i+1)
        self.__componentes[dimension-1]= None

    def insertar(self, elemento, i):
        if self.__EspLibres == -1:
            if i == 0:
                nuevoNodo = nodo(elemento)
                nuevoNodo.setSiguiente(self.__cabeza)
                posNuevo = self.__EspLibres
                self.__componentes[self.__EspLibres] = nuevoNodo
                self.__cabeza = self.__EspLibres
                self.__EspLibres = self.__componentes[self.__EspLibres].getSiguiente()
            else:   
                if i <= self.__cantidad:
                    self.__actual = self.__cabeza
                    j = 0 
                    while j < i:
                        ant = self.__actual
                        self.__actual = self.__componentes[self.__actual].getSiguiente()
                        j +=1
                    nuevoNodo.setSiguiente(self.__actual)
                    self.__componentes[self.__actual] = nuevoNodo
                    self.__arreglo[ant].setSiguiente(posNuevo)
    

    

