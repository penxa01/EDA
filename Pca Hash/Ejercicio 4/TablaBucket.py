import numpy as np
import sympy
import random

class TablaBucket:
    __tabla = None
    __enlaces = None
    __dimension = 0
    __tamano_bucket = 0
    __primario = 0

    def __init__(self,claves = 1000,bucket = 3):
        self.__tamano_bucket = bucket

        self.__dimension = self.generaPrimo(claves,bucket)
        print(self.__dimension)
        self.__tabla = np.empty(self.__dimension,dtype = np.ndarray)
        self.__enlaces = np.zeros(self.__dimension, dtype= int)

        for i in range(len(self.__tabla)):
            self.__tabla[i] = np.empty(self.__tamano_bucket,dtype=int)
    
    def generaPrimo(self,cant,bucket):
        dimension = cant // bucket
        while not sympy.isprime(dimension):
            dimension += 1
        self.__primario = dimension #Tamano de area primaria,es donde comienza el area de overflow, ultima posicion de area primaria es __primaria-1
        dimension = int(dimension *(1.3))
        return dimension
    
    def transformar(self,clave):
        cadena= str(clave)
        posicion = int(cadena[-3:])
        posicion = posicion % self.__primario
        return posicion
    
    def insertar(self,clave):
        posicion = self.transformar(clave)
        print(posicion)

        if self.__enlaces[posicion] == 3:
            if self.buscar(clave):
                print('La clave ya ha sido ingresada')
            else:
                self.overFlow(clave)
        else:
            self.__tabla[posicion][self.__enlaces[posicion]] = clave
            self.__enlaces[posicion] += 1
            print('Elemento Ingresado en la tabla')
    
    def buscar(self,clave):
        band = False
        i = 0
        j = 0
        while i < len(self.__tabla) and not band: 

            while j < self.__enlaces[i] and not band:

                if clave == self.__tabla[i][j]:
                    band = True
                    if i > self.__primario:
                        print('El elemento buscado se encuentra en el area de overflow')
                j += 1
            j = 0
            i +=1
        return band
    
    def overFlow(self,clave):
        i = self.__primario
        j = 0
        band = False
        while i < self.__dimension and not band:
            while j < self.__tamano_bucket and not band:
                if self.__tabla[i][j] == 0:
                    band = True
                    self.__tabla[i][j] = clave
                    self.__enlaces[i] += 1
                    print('Elemento insertado en el area de overflow, Bucket nro {} , elementos en bucket {}'.format(i+1,j+1))
                j += 1
            j = 0
            i += 1
        
            

if __name__ == '__main__':
    tabla = TablaBucket(1000)
    lis = []
    for i in range(1000):
        valor = random.randrange(0,1000)
        lis.append(valor)
        tabla.insertar(valor)
    
    for elemento in lis:
        if(tabla.buscar(elemento)):
            print('Elemento {} encontrado'.format(elemento))
    



