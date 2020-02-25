
"""
Esta clase crea funciones que  ordenarqan una matriz de matrices

"""

class MatrizCero(analisis): 
import numpy as npy
    
    matriz_sem = []
    lun = []
    mar = []
    mie = []
    jue = []
    vie = []
    sab = []
    dom = []
    matriz_mes = []


	def entrada ()
    	dia1 = ([80,120])
    	dia2 =
    	dia3 =
    	dia4 =
    	dia5 =
    	dia6 =
    	dia7 =
    	x=[["a", 5, 7], ["c", 3, 4], ["b", 1, 9]]
 
sortMatrix(x, 0)       # [['a', 5, 7], ['b', 1, 9], ['c', 3, 4]]
sortMatrix(x, 0, True) # [['c', 3, 4], ['b', 1, 9], ['a', 5, 7]]
sortMatrix(x, 1)       # [['b', 1, 9], ['c', 3, 4], ['a', 5, 7]]
sortMatrix(x, 1, True) # [['a', 5, 7], ['c', 3, 4], ['b', 1, 9]]
sortMatrix(x, 2)       # [['c', 3, 4], ['a', 5, 7], ['b', 1, 9]]
sortMatrix(x, 2, True) # [['b', 1, 9], ['a', 5, 7], ['c', 3, 4]]
1



1
2
def sortMatrix(matrix, field, reverse=False):
    return sorted(matrix, key=lambda x: x[field], reverse=reverse);

a = numpy.array([1, 2, 3])

newArray = numpy.append (a, [10, 11, 12])