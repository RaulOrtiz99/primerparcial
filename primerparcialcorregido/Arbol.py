
from Nodo import Nodo


class Arbol:

    def __init__(self, M):
        self.__M = M
        self.__raiz = None

    def __existe(self, dato, p):
        if p == None:
            return False
        else:
            if p.existe(dato):
                return True

        ph = p.getPosHijo(dato)
        return self.__existe(dato, p.getHijo(ph))

    def insertar(self, dato):
        if not self.__existe(dato, self.__raiz):
            self.__raiz = self.__insertar1(dato, self.__raiz)
        else:
            print('El dato ya existe')

    def __insertar1(self, dato, p):
        if p == None:
            return Nodo(self.__M, dato)
        else:
            if not p.lleno():
                p.insertar(dato)
                return p
            else:
                ph = p.getPosHijo(dato)
                p.setHijo(self.__insertar1(dato, p.getHijo(ph)), ph)
            return p

    def inOrden(self):
        self.__inOrden1(self.__raiz)

    def __inOrden1(self, p):
        if p != None:
            for i in range(p.cantDatos()):
                self.__inOrden1(p.getHijo(i))
                print(' - ', p.getData(i))
            self.__inOrden1(p.getHijo(p.cantDatos()))

