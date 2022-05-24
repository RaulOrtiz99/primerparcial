
#TODO: Autor: Raul Alberto Ortiz M. 217174558

class Nodo:

    def __init__(self, M, d):
        self.M = M
        self.d = []
        self.h = []
        for i in range(self.M-1):
            self.d.append(-1)
            self.h.append(None)
        self.h.append(None)
        self.d[0] = d

    def getDato(self, i):
        return self.d[i]

    def setDato(self, d, i):
        self.d[i] = d

    def getHijo(self, i):
        return self.h[i]

    def setHijo(self, h, i):
        self.h[i] = h

    def esHoja(self):
        for i in range(self.M):
            if self.h[i] is not None:
                return False
        return True

    def cantidadDatos(self):
        cantidad = 0
        for i in range(self.M-1):
            if self.d[i] != -1:
                cantidad = cantidad+1
            return cantidad

    def lleno(self):
        if self.cantidadDatos() == self.M-1:
            return True
        return False
    
    def getPosHijo(self, dato):
        for i in range(self.M - 1):
            if self.D[i] > dato:
                return i
        return self.M-1
