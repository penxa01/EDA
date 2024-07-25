from ClaseNodo import nodo

class PilaEncadenada:
    __comienzo = None

    def __init__(self):
        self.__comienzo = None
        self.__tope = 0
    
    def agregarObjeto(self,objeto):
        NuevoNodo = nodo(objeto)
        NuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo = NuevoNodo
        self.__tope += 1
    
    def eliminarYretornar(self):
        aux = None
        if self.vacio() == False:
            aux = self.__comienzo.getDato()
            self.__comienzo = self.__comienzo.getSiguiente()
            self.__tope -=1
        else:
            print('La pila esta vacia')
        return aux
    
    def getLongitud(self):
        return self.__tope
    
    def vacio(self):
        return (self.__tope == 0)

        
           
        
        


