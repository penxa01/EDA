class nodo:
    __dato = None
    __izquierdo = None
    __derecho = None

    def __init__(self,dato):
        from ArbolBinario import arbolbinario
        self.__dato = dato
        self.__izquierdo = arbolbinario()
        self.__derecho = arbolbinario()
    
    def setIzquierdo(self,izquierdo):
        self.__izquierdo = izquierdo
    
    def getIzquierdo(self):
        return self.__izquierdo
    
    
    def setDerecho(self,derecho):
        self.__derecho = derecho
    
    def getDerecho(self):
        return self.__derecho

    def getDato(self):
        return self.__dato
    
    def setDato(self,dato):
        self.__dato = dato