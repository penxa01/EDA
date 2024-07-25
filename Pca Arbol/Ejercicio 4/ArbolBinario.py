from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ArbolBinario import ArbolBinario

class ArbolBinario:
    __caracter = None
    __frecuencia = None
    __siguiente = None
    __izquierdo = None
    __derecho = None

    def __init__(self,caracter):
        self.__caracter = caracter
        self.__frecuencia = 0
        self.__siguiente = None
        self.__izquierdo = None
        self.__derecho = None

    
    def setElemento(self,caracter,frecuencia):
        self.__caracter = caracter
        self.__frecuencia = frecuencia
    
    def getCaracter(self):
        return self.__caracter
    
    def getSig(self) -> ArbolBinario:
        return self.__siguiente
    
    def setSig(self,siguiente):
        self.__siguiente = siguiente
    
    def setFrecuencia(self,Frecuencia):
        self.__frecuencia = Frecuencia  
    
    def getFrecuencia(self):
        return self.__frecuencia
    
    def incFrecuencia(self):
        self.__frecuencia += 1
    
    def vacio(self):
        return self.__caracter == None
   
    def getDerecho(self):
        return self.__derecho
    
    def getIzquierdo(self):
        return self.__izquierdo


    def setIzquierdo(self,referencia):
        self.__izquierdo = referencia

    def setDerecho(self,referencia):
        self.__derecho = referencia

    def getCodigo(self,caracter):
        if not caracter in self.__caracter:
            print('El caracter {} no se encuentra en el arbol'.format(caracter))
        if (len(self.__caracter) == 1):
            return ''
        elif(caracter in self.__izquierdo.getCaracter()):
            return '0' + self.__izquierdo.getCodigo(caracter)
        elif(caracter in self.__derecho.getCaracter()):
            return '1' + self.__derecho.getCodigo(caracter)
    
    def getCadena(self,byte):
        cadena = ''
        actual = self

        for bit in byte:
            if bit == '0':
                actual = actual.getIzquierdo()
            elif bit == '1':
                actual = actual.getDerecho()

            if len(actual.getCaracter()) == 1:
                cadena += actual.getCaracter()
                actual = self
        
        return cadena