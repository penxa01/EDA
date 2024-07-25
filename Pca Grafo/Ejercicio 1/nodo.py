
class nodo:
    __sig = None
    __dato = None

    def __init__(self,dato):
        self.__dato = dato
        self.__sig = None
    
    def set_sig(self,sig):
        self.__sig = sig
    
    def set_dato(self,dato):
        self.__dato = dato
    
    def get_sig(self):
        return self.__sig
    
    def get_dato(self):
        return self.__dato

