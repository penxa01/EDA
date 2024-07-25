from xml.dom import ValidationErr
from nodo import nodo

class lista:
    __cabeza = None

    def __init__(self):
        self.__cabeza = None

    def insertar(self,valor):
        nuevoNodo = nodo(valor)
        nuevoNodo.set_sig(self.__cabeza)
        self.__cabeza = nuevoNodo