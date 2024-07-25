from PilaSecuencial import pilaSecuencial
import os

def convertir(numero):
    pila = pilaSecuencial(16,str)
    binario = ''
    while numero > 0:
        pila.insertar(str(numero % 2))
        numero = numero//2
    while pila.vacio() == False:
        binario += pila.desapilar()
    return binario

if __name__ == '__main__':
    terminar = True
    while terminar:
        print('[1] Para convertir un numero')
        print('[0] Para salir')
        op = int(input('Ingrese op\n'))
        os.system('cls')
        if op == 1:
            numero = int (input('Ingrese numero a convertir\n'))
            os.system('cls')
            binario = convertir(numero)
            print('{} en binario es: {}'.format(numero,binario))
            input('Enter para continuar')
            os.system('cls')
        elif(op == 0):
            terminar = not terminar
        else:
            print('Opcion inexistente')


