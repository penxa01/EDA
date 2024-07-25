import numpy as np

class TablaHash:
    __Tabla = None
    __cant_datos = 0

    def __init__(self):
        self.__cant_datos = 1429 
        self.__Tabla = np.zeros(self.__cant_datos,dtype= int)
        self.__cont = 0 #calcula la frecuencia de busqueda
    
    def insertar(self,dato):
        clave = self.transformar(dato)
        if(self.__Tabla[clave] == 0):
            self.__Tabla[clave] = dato
        else:
            cont = 0
            while(cont < self.__Cant_datos and self.__Tabla[clave] != 0 and dato != self.__Tabla[clave]):
                cont += 1
                clave += 1
                clave = clave % self.__Cant_datos
            
            if cont == self.__cant_datos:
                print('La tabla esta llena')
            elif(self.__Tabla[clave] == dato):
                print('La clave ya esta en la tabla')
            else:
                print('Elemento insertado')
                self.__Tabla[clave] = dato
    
    def buscar(self,dato):
        clave = self.transformar(dato)
        cont = 0
        band = 0
        while(cont < self.__Cant_datos and dato != self.__Tabla[clave] and self.__Tabla[clave] != 0):
            cont += 1
            clave += 1
            clave = clave % self.__Cant_datos

        if cont > self.__cont:
            self.__cont = cont
        
        if cont == self.__cant_datos:
            band = -1
            print('La clave no se encontro en la tabla')
        elif(self.__Tabla[clave] == dato):
            band = self.__Tabla[clave]
            print('Clave Encontrada')
        return band

    def transformar(self,dato):
        return dato % self.__cant_datos


