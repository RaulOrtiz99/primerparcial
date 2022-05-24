

class Nodo:
    def __init__(self,M,D): #M es el valor del nodo, D es el dato que se le asigna al nodo
        self.M = M #Valor del nodo
        self.D = [] #Lista de datos
        self.H = [] #Lista de hijos

        for x in range(self.M-1): #Se agregan los datos
            self.D.append(-1) #Se agregan tantos datos como el valor del nodo
            self.H.append(None) #Se agregan tantos hijos como el valor del nodo
        self.H.append(None) #Se agrega un hijo por cada dato
        self.D[0] = D #Se asigna el dato al primer dato de la lista de datos

    def getData(self,i): #Devuelve el dato del nodo
        return self.D[i]

    def setDato(self,d,i): #Asigna un dato a una posicion
        self.D[i] = d

    def getHijo(self,i): #Devuelve el hijo del nodo
        return self.H[i]

    def setHijo(self,p,i): #Asigna un hijo a una posicion
        self.H[i] = p

    def existe(self,dato): #Devuelve la posicion del dato si existe, -1 si no existe
        for i in range(self.M-1):
            if self.D[i] == dato:
                return True
        return False

    def esHoja(self): #Devuelve True si el nodo es hoja
        for i in range(self.M):     #Si el nodo tiene un hijo
            if self.H[i] is not None: #Si el hijo no es nulo
                return False #El nodo no es hoja
        return True #El nodo es hoja

    def lleno(self): #Devuelve True si el nodo esta lleno
        if self.cantDatos() == self.M - 1: #Si la cantidad de datos es igual al maximo de datos
            return True #El nodo esta lleno
        return False #El nodo no esta lleno


    def getPosLibre(self): #Devuelve la posicion libre del nodo
        if self.lleno(): #Si el nodo esta lleno
            return -1 #No hay posicion libre
        for i in range(self.M-1):  #Si el nodo no esta lleno
            if self.D[i] == -1: #Si el dato es -1
                return i    #Devuelve la posicion libre


    def insertar(self,dato):
        pos = self.getPosLibre()
        while(pos>0) and (self.getData(pos-1)>dato):
            self.setDato(self.getData(pos-1),pos)
            pos = pos - 1
            self.setDato(dato,pos)




























