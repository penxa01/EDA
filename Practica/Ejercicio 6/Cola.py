import numpy as np

class cola:
    __principio = 0
    __final = 0
    __cantidad = 0
    __tamano = 0
    __elementos = None
    def __init__(self,tamanio):
        self.__tamano = tamanio
        self.__elementos = np.empty(tamanio,dtype = int)
    
    def agregarCola(self,elemento):
        if self.lleno():
            print("Cola llena")
        else:
            self.__elementos[self.__final] = elemento
            self.__final = (self.__final + 1) % self.__tamano
            self.__cantidad +=1
    
    def quitarElemento(self):
        if self.vacio():
            print("Cola vacia")
        else:
            self.__principio = (self.__principio + 1) % self.__tamano
            self.__cantidad -=1
    
    def DevolverElemento(self):
        aux = None
        if self.__cantidad == 0:
            print("Cola vacia")
        else:
            aux = self.__elementos[self.__principio]
            self.__principio = (self.__principio + 1) % self.__tamano
            self.__cantidad -= 1
        return aux
    def vacio(self):
        return (self.__cantidad == 0)
    def lleno(self):
        return (self.__cantidad == self.__tamano)
    