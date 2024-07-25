from PilaSecuencial import pilaSecuencial

def factorial(numero):
    pila = pilaSecuencial(numero,str)
    fact = 1
    while numero > 0:
        pila.insertar(numero)
        numero -=1
    while pila.vacio() == False:
        fact =fact * int(pila.desapilar())
    return fact

if __name__ == '__main__':
    num = int(input('Ingrese numero para calcular factorial\n'))
    resultado = factorial(num)
    print('El factorial de {} es {}'.format(num,resultado))


