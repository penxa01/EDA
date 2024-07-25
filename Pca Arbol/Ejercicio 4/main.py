import os
from ListaEnlazada import ListaEncadenada

if __name__ == "__main__":
    unaLista = ListaEncadenada()
    rutaAbsoluta = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
    Archivo = os.path.join(rutaAbsoluta, "prueba.txt")
    archivo = open(Archivo)
    diccionario = dict()
    for linea in archivo:
        for caracter in linea:
            unaLista.insertar(caracter)

    CodigoHuffman = unaLista.generarArbol()

    nuevoArchivo = open("comprimido.txt", "w")

    archivo.seek(0)

    for linea in archivo:
        for caracter in linea:
            codigo = CodigoHuffman.getCodigo(caracter)
            nuevoArchivo.write(codigo)
    
    nuevoArchivo.close()
    archivo.close()

    archivo = open("comprimido.txt")
    descomprimido = open("descomprimido.txt", "w")
    bytes = ""
    
    for linea in archivo:
        for bit in linea:
            bytes += bit
    
    nuevaCadena = CodigoHuffman.getCadena(bytes)
    
    descomprimido.write(nuevaCadena)