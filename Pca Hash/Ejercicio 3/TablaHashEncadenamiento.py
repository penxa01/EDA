import numpy as np
import sympy
import random
from Lista import lista

class TablaEncadenamiento:
    __arreglo = None
    __dimension = 0
    __mayor_colision = 0

    def __init__(self,cantClaves = 10000,colisiones_Permitidas = 3):
        self.__dimension = self.generaDimension(cantClaves,colisiones_Permitidas)
        self.__arreglo = np.empty(self.__dimension,dtype = lista)
        self.__mayor_colision = 0
        for i in range(self.__dimension):
            self.__arreglo[i] = lista()
        
    def generaDimension(self,cantClaves,colisiones):
        dimension = cantClaves // colisiones
        while not sympy.isprime(dimension):
            dimension +=1
        return dimension
    
    def insertar(self,dato):
        posicion = self.transformar(dato)
        self.__arreglo[posicion].insertar(dato)
    
    def buscar(self,dato):
        posicion =self.transformar(dato)
        self.__arreglo[posicion].buscar(dato)
        longitudList = self.__arreglo[posicion].longitud()
        if self.__mayor_colision < longitudList:
            self.__mayor_colision = longitudList


    def transformar(self,valor):
        cadena = str(valor)
        posicion = valor
        for i in range(len(cadena), 0 , -len(str(self.__dimension))):
            if len(cadena[i-len(str(self.__dimension)):i]) == 3:
                posicion += int(cadena[i-len(str(self.__dimension)):i])
            elif len(cadena[i-len(str(self.__dimension))+1:i])== 2:
                posicion += int(cadena[i-len(str(self.__dimension))+1:i])
            elif len(cadena[i-len(str(self.__dimension))+2:i])== 1:
                posicion += int(cadena[i-len(str(self.__dimension))+2:i])
        
        posicion = posicion % self.__dimension
        return posicion

    def mostrar_mayor_lista(self):
        print(self.__mayor_colision)

if __name__ == '__main__':
    tabla = TablaEncadenamiento()
    lis = []
    for i in range(1000):
        valor = random.randrange(0,1000000)
        lis.append(valor)
        tabla.insertar(valor)
    
    for elemento in lis:
        tabla.buscar(elemento)
    
    tabla.mostrar_mayor_lista()
