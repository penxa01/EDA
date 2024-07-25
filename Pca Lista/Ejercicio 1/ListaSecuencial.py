import numpy as np

class ListaSecuencial:
    __dimension = None
    __arreglo = None
    __ultimo = None

    def __init__(self,dimension,tipo):
        self.__dimension = dimension
        self.__arreglo = np.empty(dimension,dtype = tipo)
        self.__ultimo = -1
    
    def insertar(self,elemento, posicion):
        posicion = posicion -1
        if self.__ultimo >= self.__dimension:
            print('La lista esta llena')
        
        if posicion < 0 or self.__ultimo < posicion-1:
            print('No se puede insertar en la posicion {}, la lista solo tiene {} componentes'.format(posicion,self.__ultimo+1))
        
        for i in range(self.__ultimo-posicion+1):
            self.__arreglo[self.__ultimo-i+1] = self.__arreglo[self.__ultimo-i]
        
        self.__arreglo[posicion] = elemento
        self.__ultimo += 1

    def recuperar(self,posicion):
        posicion = posicion -1
        if posicion < 0 or posicion > self.__ultimo:
            print('No se puede recuperar un elemento de la posicion {},la lista solo tiene {} elementos'.format(posicion,self.__ultimo))
    
    def vacia(self):
        return self.__ultimo == -1
    
    def suprimir(self,posicion):
        posicion = posicion -1
        if self.vacia():
            print('La lista esta vacia, no hay elementos para suprimir')
        if posicion < 0:
            print('La posicion debe ser mayor o igual a 1')
        if posicion > self.__ultimo:
            print('No se puede suprimir el elemento {}, la lista solo tiene {} elementos'.format(posicion,self.__ultimo))

        elemento = self.__arreglo[posicion]
        for i in range(self.__ultimo- posicion):
            self.__arreglo[posicion+i] = self.__arreglo[posicion+i+1]
        
        self.__ultimo -=1

        return elemento


    def primer_elemento(self):
        return self.__arreglo[0]
    
    def ultimo_elemento(self):
        return self.__arreglo[self.__ultimo]
    
    def siguiente(self, posicion):
        return self.recuperar(posicion+1)
    
    def anterior(self, posicion):
        return self.recuperar(posicion-1)
    
    def recorrer(self, operacion):
        for i in range(self.__ultimo+1):
            operacion(self.__arreglo[i])