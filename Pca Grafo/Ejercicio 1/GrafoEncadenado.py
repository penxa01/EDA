from typing import List,Tuple
import numpy as np
from nodo import nodo
from lista import lista

class grafoEncadenado:
    __arreglo = None
    __dimension = 0

    def __init__(self,dimension,arcos:List[Tuple[int]]):
        self.__arreglo = np.empty(dimension,lista)
        self.__dimension = dimension
    
