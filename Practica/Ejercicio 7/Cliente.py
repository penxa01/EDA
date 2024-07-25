
class cliente:
    __tiempoI  = 0
    __tiempoS = 0

    def __init__(self,entradaCola):
        self.__tiempoI = entradaCola
    
    def tiempoEspera(self):
        return self.__tiempoS - self.__tiempoI
    
    def saleCola(self,tiempoSalida):
        self.__tiempoS = tiempoSalida
    
    def getT_ingreso(self):
        return self.__tiempoI
    
    def getT_salida(self):
        return self.__tiempoS
