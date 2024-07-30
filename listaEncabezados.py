class NodoCabecera:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None
        self.referencia = None

class ListaEncabezados:
    def __init__(self):
        self.principio = None
        self.ultimo = None
    
    def ingresar(self, indice):
        nuevo = NodoCabecera(indice)
        if self.principio == None:
            self.principio = nuevo
        else:
            temp = self.principio
            while temp.siguiente is not None:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.anterior = temp
            self.ultimo = nuevo
    
    def getEncabezado(self, indice):
        temp = self.principio
        while temp is not None:
            if temp.valor == indice:
                return temp
            temp = temp.siguiente
        return None