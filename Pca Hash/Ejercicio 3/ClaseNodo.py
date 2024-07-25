class nodo:
    __dato = None
    __siguiente = None

    def __init__(self,dato):
        self.__dato = dato
    
    def set_sig(self,siguiente):
        self.__siguiente = siguiente
    
    def get_sig(self):
        return self.__siguiente
    
    def get_dato(self):
        return self.__dato
    
    def set_dato(self,dato):
        self.__dato = dato
        

