
class Nodo:

    def __init__(self, M, D): # Constructor
        self.M = M  # Cantidad de hijos
        self.D = []  # Datos
        self.H = []  # Hijos

        for x in range(self.M - 1): # Inicializacion de datos
            self.D.append(-1)
            self.H.append(None)
        self.H.append(None)
        self.D[0] = D

    def getData(self, i): # Devuelve el dato en la posicion i
        return self.D[i]

    def setData(self, d, i): # Cambia el dato en la posicion i
        self.D[i] = d

    def getHijo(self, i): # Devuelve el hijo en la posicion i
        return self.H[i]

    def setHijo(self, p, i): # Cambia el hijo en la posicion i
        self.H[i] = p

    def existe(self, dato): # Devuelve True si el dato existe en el nodo
        for i in range(self.M - 1): # Busca el dato
            if self.D[i] == dato: # Si lo encuentra
                return True # Devuelve True
        return False # Si no lo encuentra devuelve False

    def esHoja(self): # Devuelve True si el nodo es hoja
        for i in range(self.M): # Busca el dato
            if self.H[i] is not None: # Si lo encuentra
                return False # Devuelve False
        return True # Si no lo encuentra devuelve True

    def cantDatos(self): # Devuelve la cantidad de datos en el nodo
        cant = 0 # Inicializa la cantidad de datos
        for i in range(self.M - 1):
            if self.D[i] != -1: # Si el dato no es -1
                cant = cant + 1 # Aumenta la cantidad de datos
        return cant # Devuelve la cantidad de datos

    def lleno(self): # Devuelve True si el nodo esta lleno
        if self.cantDatos() == self.M - 1: # Si la cantidad de datos es igual a la cantidad de hijos
            return True # Devuelve True
        return False # Si no devuelve False

    def getPosHijo(self, dato): # Devuelve la posicion del hijo que contiene el dato
        for i in range(self.M - 1):
            if self.D[i] > dato: # Si el dato es mayor que el dato en la posicion i
                return i # Devuelve la posicion i
        return self.M - 1 # Si no devuelve la posicion M - 1

    def getPosLibre(self): # Devuelve la posicion libre del nodo
        if self.lleno(): # Si el nodo esta lleno
            return -1 # Devuelve -1
        for i in range(self.M - 1): # Busca la posicion libre
            if self.D[i] == -1: # Si el dato en la posicion i es -1
                return i # Devuelve la posicion i

    def insertar(self, dato): # Inserta un dato en el nodo
        pos = self.getPosLibre() # Obtiene la posicion libre del nodo
        while (pos > 0) and (self.getData(pos - 1) > dato):  # Mientras la posicion sea mayor a 0 y el dato en la posicion menos 1 sea mayor al dato
            self.setData(self.getData(pos - 1), pos) # Mueve el dato en la posicion i a la posicion i - 1
            pos = pos - 1 # Decrementa la posicion
        self.setData(dato, pos) # Inserta el dato en la posicion i

