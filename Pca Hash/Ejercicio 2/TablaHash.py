import numpy as np
import random

class TablaHash:
    __Tabla = None
    __cant_datos = 0
    __pseudo = 0
    def __init__(self):
        self.__cant_datos = 1429 
        self.__Tabla = np.zeros(self.__cant_datos,dtype= int)
        self.__cont = 0
        self.__pseudo = random.randrange(0,5)

    
    def insertar(self,dato):
        posicion = self.transformar(dato)
        if(self.__Tabla[posicion] == 0):
            self.__Tabla[posicion] = dato
        else:
            orignal = posicion
            posicion = (posicion + self.__pseudo) % self.__cant_datos

            while(orignal != posicion and self.__Tabla[posicion] != 0 and dato != self.__Tabla[posicion]):
                posicion += self.__pseudo
                posicion = posicion % self.__cant_datos
            
            if(self.__Tabla[posicion] == dato):
                print('La posicion ya esta en la tabla')
            elif (orignal == posicion):
                print('La tabla esta llena')
            else:
                print('Elemento insertado')
                self.__Tabla[posicion] = dato
    
    def buscar(self,dato):
        posicion = self.transformar(dato)
        cont = 0
        band = 0
        original = posicion
        posicion = (posicion + self.__pseudo) % self.__cant_datos
        if(self.__Tabla[posicion] == 0):
            band = self.__Tabla[posicion] 
        else:    
            while(original != posicion and dato != self.__Tabla[posicion] and self.__Tabla[posicion] != 0):
                cont += 1
                posicion += self.__pseudo
                posicion = posicion % self.__cant_datos

        
        if original == posicion or self.__Tabla[posicion] == 0:

            band = -1
            print('La posicion no se encontro en la tabla')

        elif(self.__Tabla[posicion] == dato):

            if cont > self.__cont:
                self.__cont = cont

            band = self.__Tabla[posicion]
            print('posicion Encontrada')
        return band

    def transformar(self,dato):
        return dato % self.__cant_datos
    
    def mostrar_contador(self):

        print(self.__cont)


if __name__ == '__main__':
    random.seed(23)
    tabla = TablaHash()
    lista =[]
    for i in range(1000):
        valor = random.randrange(0,100000)
        lista.append(valor)
        tabla.insertar(valor)
    
    for elemento in lista:
        tabla.buscar(elemento)
    
    tabla.mostrar_contador()
        

