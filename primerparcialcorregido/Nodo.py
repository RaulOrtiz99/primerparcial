class Nodo:
    def __init__(self,M,D):
        self.M = M #Cantidad de hijos
        self.D = D #Dato del nodo
        self.P= 0 #Posicion del hijo
        self.H = [] #Lista de hijos

        for x in range(self.M):
            self.H.append(None) #Se inicializa la lista de hijos con Nones para que no se caiga al recorrerla

    def getData(self): #Devuelve el dato del nodo
        return self.D

    def setData(self,D): #Setea el dato del nodo
        self.D = D

    def getHijos(self,i): #Devuelve el hijo en la posicion i
        return self.H[i]

    def setHijos(self,p,i): #setea un hijo en la posicion i
        self.H[i] = p

    def agregarHijo(self,p): #Agrega un hijo al nodo
        self.H[self.P] = p #Se agrega el hijo en la posicion P
        self.P += 1

    def esHoja(self): #Verifica si el nodo es hoja
        for i in range(self.M): #Recorre la lista de hijos
            if self.H[i] is not None: #Si encuentra un hijo que no sea None, es que no es hoja
                return False #Devuelve False
            return True #Si no encuentra un hijo que no sea None, es que es hoja

    def cantidadHijos(self): #Devuelve la cantidad de hijos
        cantidad = 0
        for i in range(self.M): #Recorre la lista de hijos
            if self.H[i] is not None:   #Si encuentra un hijo que no sea None, suma 1
                cantidad += 1 #Suma 1
        return cantidad #Devuelve la cantidad de hijos