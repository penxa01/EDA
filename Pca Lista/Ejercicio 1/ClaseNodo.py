
class nodo:
    __objeto = None
    __siguiente = None

    def __init__(self,objeto,siguiente = 0):
        self.__objeto = objeto
        self.__siguiente = siguiente
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__objeto