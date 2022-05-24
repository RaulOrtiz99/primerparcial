
#TODO: Autor: Raul Alberto Ortiz M. 217174558
from Nodo import Nodo


class Arbol:

    def __init__(self, M):
        self.__M = M
        self.__raiz = None

    def __existe(self, dato, x):
        if x == None:
            return False
        else:
            if x.existe(dato):
                return True

    def insertar(self, dato):
        if not self.__existe(dato, self.__raiz):
            self.__raiz = self.__insertarI(dato, self.__raiz)

    def __insertarI(self, dato, x):

        if x == None:
            return Nodo(self.__M, dato)
        else:
            if not x.lleno():
                x.insertar(dato)
                return x
            else:
                xh = x.getPosHijo(dato)
                x.setHijo(self.__insertarI(dato, x.getHijo(xh)), xh)
            return x

    def inOrden(self):
        self.__inOrden1(self.__raiz)

    def __inOrden1(self, p):
        if p != None:
            for i in range(p.cantDatos()):
                self.__inOrden1(p.getHijo(i))
                print(' - ', p.getData(i))
            self.__inOrden1(p.getHijo(p.cantDatos()))
    
    def cantNodos(self):
            return self.__cantNodos1(self.__raiz)
    
    def __cantNodos1(self, x):
        if x is None:
            return 0
        if x.esHoja():
            return 1
        cantidanodos = 0
        for i in range(self.__M):
            cantidanodos= cantidanodos + self.__cantNodos1( p.getHijo(i) )
        return cantidanodos+1