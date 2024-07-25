from ArbolBinario import ArbolBinario

class ListaEncadenada:
    __cabeza : ArbolBinario
    __cantidad : int

    def __init__(self) -> None:
        self.__cabeza = None
        self.__cantidad = 0
    
    def insertar(self, caracter):
        actual = self.__cabeza
        while actual != None and actual.getCaracter() != caracter:
            actual = actual.getSig()
        if actual != None:
            actual.incFrecuencia()
        else:
            unNodo = ArbolBinario(caracter)
            unNodo.setSig(self.__cabeza)
            self.__cabeza = unNodo
    
    def vacia(self):
        return self.__cantidad == 0
  
    def ordenar(self):
        ultimo = None
        cota = None

        while ultimo != self.__cabeza:
            ultimo = self.__cabeza
            actual = self.__cabeza
            while actual.getSig() != cota:
                if (actual.getFrecuencia()) > (actual.getSig().getFrecuencia()):
                    aux = actual.getCaracter()
                    aux2 = actual.getFrecuencia()
                    actual.setElemento(actual.getSig().getCaracter(),actual.getSig().getFrecuencia())
                    actual.getSig().setElemento(aux,aux2)
                    ultimo = actual
                actual = actual.getSig()

            cota = ultimo.getSig()

    def generarArbol(self):
        self.ordenar()

        while self.__cabeza.getSig() != None:
            nuevoArbol = ArbolBinario(self.__cabeza.getCaracter()+self.__cabeza.getSig().getCaracter())
            nuevoArbol.setFrecuencia(self.__cabeza.getFrecuencia()+self.__cabeza.getSig().getFrecuencia())
            nuevoArbol.setIzquierdo(self.__cabeza)
            nuevoArbol.setDerecho(self.__cabeza.getSig())
            nuevoArbol.setSig(self.__cabeza.getSig().getSig())
            self.__cabeza = nuevoArbol
            
        
        return self.__cabeza