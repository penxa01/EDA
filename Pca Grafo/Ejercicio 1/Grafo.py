import re
from typing import List, Tuple

import numpy as np

class Grafo:
    __cant_nodos: int
    __dimension: int
    __arreglo: np.ndarray
    
    
    def __init__(self, nodos:int, arcos:List[Tuple[int]]) -> None:
        self.__cant_nodos = nodos
        self.__dimension = self.__cant_nodos*(self.__cant_nodos+1)//2
        self.__arreglo = np.empty(self.__dimension, int)
        for i, j in arcos:
            self.set_arco(i, j, 1)
        
    
    
    def set_arco(self,  nodo_origen:int, nodo_destino:int, valor:int):
        if nodo_origen < nodo_destino:
            nodo_origen, nodo_destino = nodo_destino, nodo_origen
        self.__arreglo[nodo_origen*(nodo_origen-1)//2+nodo_destino] = valor
    
    def get_arco(self, nodo_origen:int, nodo_destino:int):
        if nodo_origen < nodo_destino:
            nodo_origen, nodo_destino = nodo_destino, nodo_origen
        return self.__arreglo[nodo_origen*(nodo_origen-1)//2+nodo_destino]
    
    
    def adyacentes(self, un_nodo):
        nodos = []
        for i in range(self.__cant_nodos):
            if  self.get_arco(un_nodo, i):
                nodos.append(i)
        return nodos
    
    
    # def camino(self, nodo_origen:int, nodo_destino:int):
    #     d:np.ndarray = np.empty(self.__cant_nodos, int)
    #     d.fill(-1)
    #     cola = []
    #     cola.append(nodo_origen)
    #     band = False
    #     inicial = (nodo_origen, [])
    #     pila = []
    #     pila.append(inicial)
    #     i = 0
    #     while len(cola)>0 and not band:
    #         v = cola.pop(0)
    #         caminos = pila.pop()
    #         adys = self.adyacentes(v)
    #         i += 1
    #         for u in adys:
    #             if d[u] == -1:
    #                 d[u] = d[v] + 1
    #                 caminos[2].append((u, []))
    #                 cola.append(u)
    #             if u == nodo_destino:
    #                 band = True
    #         pila.append(caminos)
    

    def camino(self, nodo_origen:int, nodo_destino):
        d:np.ndarray = np.empty(self.__cant_nodos, int)
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