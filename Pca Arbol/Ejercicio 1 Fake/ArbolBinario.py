from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ArbolBinario import arbolbinario


class arbolbinario:
    __raiz:(arbolbinario|None)

    def __init__(self):
        self.__raiz = None

    def insertar(self,elemento):
        from ClaseNodo import nodo
        if self.__raiz == None:
            self.__raiz = nodo(elemento)
            print('Elemento ingresado con exito')

        elif(self.__raiz.getDato() == elemento):
            print('El elemento ya esta ingresado en el arbol')

        elif(self.__raiz.getDato() > elemento):
            subArbol = self.__raiz.getIzquierdo()
            subArbol.insertar(elemento)
        
        elif(self.__raiz.getDato() < elemento):
            subArbol = self.__raiz.getDerecho()
            subArbol.insertar(elemento)

    
    def Inorden(self):
        if self.__raiz != None:
            self.__raiz.getIzquierdo().Inorden()
            print(self.__raiz.getDato())
            self.__raiz.getDerecho().Inorden()
    
    def Preorden(self):
        if self.__raiz != None:
            print(self.__raiz.getDato())
            self.__raiz.getIzquierdo().Preorden()
            self.__raiz.getDerecho().Preorden()
    
    def posOrden(self):
        if self.__raiz != None:
            self.__raiz.getDerecho().Preorden()
            self.__raiz.getIzquierdo().Preorden()
            print(self.__raiz.getDato())

    

    
        
