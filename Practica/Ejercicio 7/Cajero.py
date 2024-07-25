
class cajero:
    __ocupada = None
    __tiempoAtencion =  0

    def __init__(self,tiempoAtencion = 0):
        self.__tiempoAtencion = tiempoAtencion
        self.__ocupada = False

    def ocupar(self):
        self.__ocupada = True
        self.__tiempoAtencion = 5
    
    def actualizar(self):
        if (self.__tiempoAtencion == 0):
            self.__ocupada = False
            print("Sale cliente")
        else:
            self.__tiempoAtencion -=1
    
    def getOcupacion(self):
        return self.__ocupada
    
    def getTiempo_atencion(self):
        return self.__tiempoAtencion
