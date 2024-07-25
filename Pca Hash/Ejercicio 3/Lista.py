from ClaseNodo import nodo

class lista:
    __cabeza = None

    def __init__(self):
        self.__cabeza = None
    
    def buscar(self,dato):
        actual = self.__cabeza
        band = True
        while(actual != None and actual.get_dato() != dato):
            actual = actual.get_sig()
        
        if actual == None:
            band = False
        elif(actual.get_dato() == dato):
            print('Elemento encontrado')
        
        return band
    
    def longitud(self):
        cont = 0 
        actual = self.__cabeza
        while actual != None:
            cont += 1
            actual = actual.get_sig()
        return cont
    
    def insertar(self,dato):
        if (self.buscar(dato)):
            print('La clave ya se encuentra en la tabla')
        else:
            nuevoNodo = nodo(dato)
            nuevoNodo.set_sig(self.__cabeza)
            self.__cabeza = nuevoNodo

        
