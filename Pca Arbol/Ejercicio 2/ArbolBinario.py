
class ArbolBinario:
    __raiz = None
    __izquierdo = None
    __derecho = None

    def __init__(self):
        self.__raiz = None
        self.__izquierdo = None
        self.__derecho = None

    def getRaiz(self):
        return self.__raiz
    
    def setElemento(self):
        self.__raiz = None
        self.__izquierdo = None
        self.__derecho = None
    
    def getDerecho(self):
        return self.__derecho
    
    def getIzquierdo(self):
        return self.__izquierdo

    def vacio(self):
        return self.__raiz == None

    def setIzquierdo(self,referencia):
        self.__izquierdo = referencia

    def setDerecho(self,referencia):
        self.__derecho = referencia

    
    def Inorden(self):
        if self.__raiz != None:
            self.__izquierdo.Inorden()
            print(self.__raiz)
            self.__derecho.Inorden()
    
    
    def frontera(self):
        if self.__raiz != None:
            self.__izquierdo.frontera()
            if self.__izquierdo.vacio() and self.__derecho.vacio():
                print(self.__raiz)
            self.__derecho.frontera()
    
    def Preorden(self):
        if self.__raiz != None:
            print(self.__raiz)
            self.__izquierdo.Preorden()
            self.__derecho.Preorden()
    
    def posOrden(self):
        if self.__raiz != None:
            self.__derecho.Preorden()
            self.__izquierdo.Preorden()
            print(self.__raiz)
    
    def cambiarHijo(self, antiguoHijo, nuevoHijo):
        if self.__izq is antiguoHijo:
            self.__izq = nuevoHijo
        elif self.__der is antiguoHijo:
            self.__der = nuevoHijo
        else:
            print("El arbol {0} no tiene como hijo al arbol {1}".format(self, antiguoHijo))
    
    def insertar(self,elemento):
        if self.__raiz == None:
            self.__raiz = elemento
            self.__derecho = ArbolBinario()
            self.__izquierdo = ArbolBinario()
            print('Elemento ingresado con exito')

        elif(self.__raiz == elemento):
            print('El elemento ya esta ingresado en el arbol')

        elif(self.__raiz > elemento):
            subArbol = self.__izquierdo
            subArbol.insertar(elemento)
        
        elif(self.__raiz < elemento):
            subArbol = self.__derecho
            subArbol.insertar(elemento)

    def buscar(self,elemento):
        if(self.__raiz == None):
            print('El elemento no se encuentra en el arbol')
        elif(self.__raiz == elemento):
            return self.__raiz
        elif(self.__raiz > elemento):
            return self.__izquierdo.buscar(elemento)
        elif(self.__raiz < elemento):
            return self.__derecho.buscar(elemento)

    def suprimir(self,elemento,padre =None):
        if self.__raiz == elemento:

            if self.__izquierdo.vacio() and self.__derecho.vacio():
                self.__raiz = None
                self.__izquierdo = None
                self.__derecho = None

            elif self.__izquierdo.vacio() and padre != None:
                padre.cambiarHijo(self, self.__derecho)

            elif self.__derecho.vacio() and padre != None:
                padre.cambiarHijo(self, self.__izquierdo)

            else:
                anterior = self
                infimo = self.__derecho

                while not infimo.getIzquierdo().vacio():
                    anterior = infimo
                    infimo = infimo.getIzquierdo()
                self.__raiz = infimo.getRaiz()
                anterior.cambiarHijo(infimo, infimo.getDerecho())


        elif elemento < self.__raiz:
            self.__izquierdo.suprimir(elemento, self)
        elif self.__raiz < elemento:
            self.__derecho.suprimir(elemento, self)   

    def nivel(self, elemento, nivelAnterior = 0):
        if self.__raiz == None:
            print("No existe el elemento {0} en el arbol".format(elemento))

        if self.__raiz == elemento:
            return nivelAnterior + 1

        elif elemento < self.__raiz:
            return self.__izquierdo.nivel(elemento, nivelAnterior+1)

        elif self.__raiz < elemento:
            return self.__derecho.nivel(elemento, nivelAnterior+1)



    def hoja(self, elemento):
        if self.__raiz == elemento:
            if self.__izquierdo.vacio() and self.__derecho.vacio():
                return True
            else:
                return False
        
        else:
            if elemento < self.__raiz:
                return self.__izquierdo.hoja(elemento)
            elif self.__raiz < elemento:
                return self.__derecho.hoja(elemento)
    


    def hijo(self, elementoHijo, elementoPadre):
        if self.__raiz == elementoPadre:
            if self.__izquierdo.getRaiz() == elementoHijo or self.__derecho.getRaiz() == elementoHijo:
                return True
            else:
                return False
        
        else:
            if elementoPadre < self.__raiz and not self.__izquierdo.vacio():
                return self.__izquierdo.hijo(elementoHijo, elementoPadre)

            elif self.__raiz < elementoPadre and not self.__derecho.vacio():
                return self.__derecho.hijo(elementoHijo, elementoPadre)
            
            else:
                return False



    def padre(self, elementoPadre, elementoHijo):
        return self.hijo(elementoHijo, elementoPadre)
    


    def altura(self):
        if self.__izq != None:
            alturaIzquierda = self.__izquierdo.altura() + 1
        else:
            alturaIzquierda = 0
        
        if self.__der != None:
            alturaDerecha = self.__derecho.altura() + 1
        else:
            alturaDerecha = 0
        
        return max(alturaIzquierda, alturaDerecha)             

if __name__ == "__main__":
    arbol = ArbolBinario()
    arbol.insertar(5)
    arbol.insertar(3)
    arbol.insertar(7)
    arbol.insertar(4)
    arbol.insertar(6)
    arbol.insertar(1)
    arbol.insertar(2)
    arbol.frontera()
    
