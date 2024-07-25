from typing import Tuple,List
import numpy as np

class grafoSecuencial:
    __cantidad = 0
    __arreglo = None
    __dimension = 0

    def __init__(self,nodos, arcos:List[Tuple[int]]):
        self.__cantidad = len(nodos)
        self.__dimension = (self.__cantidad*(self.__cantidad+1))//2
        self.__arreglo = np.empty(self.__dimension, dtype= int)
        for i,j in arcos:
            self.set_arcos(i,j,1)

    def set_arcos(self,nodoO,nodoD,valor):
        if nodoO < nodoD:
            nodoO, nodoD = nodoD,nodoO
        self.__arreglo[((nodoO*(nodoO+1))//2)+nodoD] = valor
    
    def get_arco(self,nodoO,nodoD):
        if nodoO < nodoD:
            nodoO, nodoD = nodoD,nodoO
        return self.__arreglo[((nodoO*(nodoO+1))//2)+nodoD] 
    
    def adyacentes(self,nodo):
        lista = []
        for nodo_des in range(self.__cantidad):
            if self.get_arco(nodo,nodo_des) == 1:
                lista.append(nodo_des)
        print('El nodo {} es adyacente con los nodos {}'.format(nodo,lista))
        return lista
    
    def camino(self, nodo_origen:int, nodo_destino):
        d:np.ndarray = np.empty(self.__cantidad, int)
        d.fill(0)
        resultado = self.camino_aux(nodo_origen, nodo_destino, d)
        if isinstance(resultado,list):
            resultado.insert(0,nodo_origen)
        return resultado
         
    
    def camino_aux(self, nodo_origen:int, nodo_destino:int, d:np.ndarray):
        d[nodo_origen] = 1
        adys = self.adyacentes(nodo_origen)
        for un_nodo in adys:
            if un_nodo == nodo_destino:
                return [nodo_destino]
            if d[un_nodo] == 0:
                retorno = self.camino_aux(un_nodo, nodo_destino, d)
                if isinstance(retorno, list):
                    retorno.insert(0,un_nodo)
                    return retorno
        return 0
    
    def camino_minimo(self,nodo_origen,nodo_destino):
        distancias = np.empty(self.__cantidad, int)
        conocidos = np.empty(self.__cantidad, bool)
        caminos = np.empty(self.__cantidad, int)
        distancias.fill(-1)
        for i in range(self.__cantidad):
            conocidos[i] = False
        caminos.fill(-1)
        
        for i in range(self.__cantidad):
            v = self.get_minimo(distancias, conocidos)
            conocidos[v] = True
            adys = self.adyacentes(v)
            for w in adys:
                if conocidos[w] == False:
                    if distancias[v] + self.get_arco(v, w) < distancias[w] or distancias[w]==-1:
                        distancias[w] = distancias[v] + self.get_arco(v, w)
                        caminos[w] = v
    
    def get_minimo(self, distancias:np.ndarray, conocidos:np.ndarray):
        mas_corto = 0
        for i in range(self.__cantidad):
            if conocidos[i] == False and distancias[i] < distancias[mas_corto]:
                mas_corto = i
        return mas_corto

    def conexo(self):
        matriz = np.empty((self.__cantidad, self.__cantidad), int)
        matriz_conectividad = np.empty((self.__cantidad, self.__cantidad), int)
        for i in range(self.__cantidad):
            for j in range(self.__cantidad):
                matriz[i, j] = self.get_arco(i, j)
                matriz_conectividad[i, j] = self.get_arco(i, j)
        
        for i in range(self.__cantidad):
            matriz_conectividad = np.matmul(matriz, matriz_conectividad)
        
        i = 0
        j = 0

        while i < self.__cantidad and matriz_conectividad[i, j] != 0:
            i += 1
            j = 0
            while j < self.__cantidad and matriz_conectividad[i, j] != 0:
                j += 1
        
        return i == self.__cantidad
    
    def arbol_recubrimiento(self):
        if not self.conexo():
            raise Exception("El grafo no es conexo, por lo que no se puede encontrar su arbol de recubrimiento")
        
        distancias = np.empty(self.__cantidad, int)
        conocidos = np.empty(self.__cantidad, bool)
        caminos = np.empty(self.__cantidad, int)
        distancias.fill(-1)
        for i in range(self.__cantidad):
            conocidos[i] = False
        caminos.fill(-1)
        
        for i in range(self.__cant_nodos):
            v = self.get_corto_desconocido(distancias, conocidos)
            conocidos[v] = True
            adys = self.adyacentes(v)
            for w in adys:
                if conocidos[w] == False:
                    if self.get_arco(v, w) < distancias[w] or distancias[w]==-1:
                        distancias[w] = self.get_arco(v, w)
                        caminos[w] = v
        
        arcos = []
        for i in range(self.__cant_nodos):
            arcos.append((i, caminos[i], distancias[i, caminos[i]]))
        
        un_grafo = grafoSecuencial(self.__cant_nodos, arcos)

        return un_grafo
    