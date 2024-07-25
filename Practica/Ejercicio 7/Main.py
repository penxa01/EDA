import os
import random
from ColaEncadenada import ColaEncadenada
from Cliente import cliente
from Cajero import cajero


def calculaMaximo(cliente,tiempomaximo):
    if(cliente.tiempoEspera()>tiempomaximo):
        tiempomaximo = cliente.tiempoEspera()
    return tiempomaximo

if __name__ == '__main__':
    caja1 = cajero()
    cola = ColaEncadenada()
    maximoEspera = 0

    tiempoSimulacion = int(input('Ingrese tiempo de simulacion en minutos\n'))
    os.system('cls')
    i = 0


    while i < tiempoSimulacion:
        if random.randrange(0,2) == 1:
            print('Ingresa cliente')
            Ncliente = cliente(i)
            cola.insertar(Ncliente)
        else:
            print('No ingresa cliente en el minuto {}'.format(i))
        
        if(not caja1.getOcupacion() and not cola.vacio()):
            clienteApasar = cola.obtenerPrimer()
            clienteApasar.saleCola(i)
            caja1.ocupar()
            maximoEspera =calculaMaximo(clienteApasar,maximoEspera)
        elif(caja1.getOcupacion()):
            caja1.actualizar()
        else:
            print('No hay nadie en cola')
            
        i +=1
    
    print('El maximo de espera es de {} minutos'.format(maximoEspera))

            

        

    