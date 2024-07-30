from listaEncabezados import ListaEncabezados
import graphviz

class Nodo:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.bloqueSiguiente = None
        self.bloqueAnterior = None
        self.siguiente = None
        self.atras = None
        self.arriba = None
        self.abajo = None

class ListaLigada:
    def __init__(self, tamaño, filas, columnas):
        self.tamaño = tamaño
        self.capacidad = tamaño
        self.datosFilas = ListaEncabezados()
        self.datosColumnas = ListaEncabezados()
        self.asignaciónEncabezados(filas, columnas)

    def asignaciónEncabezados(self, filas, columnas):
        for data in range(filas):
            if data < columnas:
                self.datosColumnas.ingresar(data)
            self.datosFilas.ingresar(data)
        for i in range(filas):
            for j in range(columnas):
                nuevo = Nodo(i, j, None)
                auxEncabezado = self.datosFilas.getEncabezado(i)
                if auxEncabezado.referencia is None:
                    auxEncabezado.referencia = nuevo
                else:
                    dataMatriz = auxEncabezado.referencia
                    while dataMatriz.siguiente is not None:
                        dataMatriz = dataMatriz.siguiente
                    dataMatriz.siguiente = nuevo
                    nuevo.atras = dataMatriz
                auxEncabezado = self.datosColumnas.getEncabezado(j)
                if auxEncabezado.referencia is None:
                    auxEncabezado.referencia = nuevo
                else:
                    dataMatriz = auxEncabezado.referencia
                    while dataMatriz.abajo is not None:
                        dataMatriz = dataMatriz.abajo
                    dataMatriz.abajo = nuevo
                    nuevo.arriba = dataMatriz

    def agregarBloque(self, id, valor):
        self.capacidad -= valor.tamaño
        temp = None
        aux = self.datosFilas.principio
        if aux.referencia.valor is None:
            aux.referencia.valor = valor
        else:
            bandera = False
            while aux is not None:
                temp = aux.referencia
                if temp.valor is None:
                    temp.valor = valor
                    bandera = True
                    break
                while temp.siguiente is not None and temp.siguiente.valor is not None:
                    temp = temp.siguiente
                if temp.siguiente is not None:
                    temp.siguiente.valor = valor
                    break
                aux = aux.siguiente
        if temp is not None:
            tempListaBloques = self.encontrarBloque(id)
            if temp.valor.id is id:
                while tempListaBloques.bloqueSiguiente is not None:
                    tempListaBloques = tempListaBloques.bloqueSiguiente
                if bandera:
                    tempListaBloques.bloqueSiguiente = temp
                    temp.bloqueAnterior = tempListaBloques
                else:
                    tempListaBloques.bloqueSiguiente = temp.siguiente
                    temp.siguiente.bloqueAnterior = tempListaBloques
     
    def encontrarBloque(self, id):
        actual = self.datosFilas.principio
        while actual is not None:
            temp = actual.referencia
            while temp is not None:
                if temp.valor.id == id:
                    return temp
                temp = temp.siguiente
            actual = actual.siguiente

    def recorrerFilas(self):
        grafo=""
        grafo2 = ""
        grafo3 = ""
        grafo4 = ""
        grafo5 = ""
        grafo6 = ""
        rFila = self.datosFilas.principio
        cont = 2
        auxRecorrido = None
        while rFila is not None:
            grafo5 += "{rank=same;"
            grafo += f'nodof{rFila.valor} [label=\" {rFila.valor} \" group=1]\n'
            grafo5 += f"nodof{rFila.valor};"
            if rFila.siguiente is not None:
                grafo2 += f"nodof{rFila.valor}->nodof{rFila.siguiente.valor} [arrowhead=none] \n"
            temp = rFila.referencia
            grafo3 += f"nodof{rFila.valor}->nodo{temp.fila}_{temp.columna} [arrowhead=none] \n"
            while temp is not None:
                grafo5 += f"nodo{temp.fila}_{temp.columna};"
                if temp.valor is None:
                    grafo3 += f"nodo{temp.fila}_{temp.columna}[label=\" \" group={cont}]\n"
                else:
                    grafo3 += f"nodo{temp.fila}_{temp.columna}[label=\"{temp.valor.nombre}\n{temp.valor.tamaño}\n{temp.valor.segmento}\" group={cont} fillcolor=\"green\"]\n"
                    if temp.valor.segmento == 0:
                        auxRecorrido = temp
                        while auxRecorrido is not None:
                            if auxRecorrido.bloqueSiguiente is not None:
                                grafo6 += f"nodo{auxRecorrido.fila}_{auxRecorrido.columna}->nodo{auxRecorrido.bloqueSiguiente.fila}_{auxRecorrido.bloqueSiguiente.columna} [dir=\"both\"]\n"
                            auxRecorrido = auxRecorrido.bloqueSiguiente
                if temp.siguiente is not None:
                    grafo4 += f"nodo{temp.fila}_{temp.columna}->nodo{temp.siguiente.fila}_{temp.siguiente.columna} [arrowhead=none]\n"
                temp = temp.siguiente
            grafo5+= "}\n"
            grafo4 += grafo5
            grafo5 = ""
            rFila = rFila.siguiente
            cont += cont
        grafo += grafo2
        grafo += grafo3
        grafo += grafo4
        grafo += grafo6
        return grafo
    
    def recorrerColumnas(self):
        grafo = ""
        grafo2 = ""
        grafo3 = ""
        grafo5 = "{rank=same;"
        rColumna = self.datosColumnas.principio
        while rColumna is not None:
            grafo += f"nodoc{rColumna.valor} [label=\"{rColumna.valor}\" group={rColumna.valor}]\n"
            grafo5 += f"nodoc{rColumna.valor};"
            if rColumna.siguiente is not None:
                grafo2 += f"nodoc{rColumna.valor}->nodoc{rColumna.siguiente.valor} [arrowhead=none] \n"
            temp = rColumna.referencia
            grafo3 += f"nodoc{rColumna.valor}->nodo{temp.fila}_{temp.columna} [arrowhead=none]\n"
            temp = rColumna.referencia
            while temp is not None:
                if temp.abajo is not None:
                    grafo3 += f"nodo{temp.fila}_{temp.columna}->nodo{temp.abajo.fila}_{temp.abajo.columna} [arrowhead=none]\n"                
                temp = temp.abajo
            rColumna = rColumna.siguiente
        grafo5 += "}\n"
        grafo += grafo2
        grafo += grafo5
        grafo += grafo3
        return grafo
            
    def liberarBloque(self, id, segmento):
        actual = self.datosFilas.principio
        while actual is not None:
            temp = actual.referencia
            while temp is not None:
                if temp.valor.id is id and temp.valor.segmento == segmento:
                    self.capacidad += temp.valor.tamaño
                    temp.valor = None
                    if temp.bloqueSiguiente is not None:
                        auxAnterior = temp.bloqueAnterior
                        auxSiguiente = temp.bloqueSiguiente
                        auxAnterior.bloqueSiguiente = auxSiguiente
                        auxSiguiente.bloqueAnterior = auxAnterior
                        temp.bloqueAnterior = None
                        temp.bloqueSiguiente = None
                    return
                temp = temp.siguiente
            actual = actual.siguiente
    
    def generarGraphviz(self, numImagen):
        nombreArchivo= f"lista_enlazada{numImagen}.dot"
        grafica = "digraph G{\nlabel=\" Disco 25MB\nCapacidad: "+str(self.capacidad)+"\";\n"
        grafica += "node[shape=box style=\"filled\" fontname=\"Arial\"]\n"
        grafica += self.recorrerFilas()
        grafica += self.recorrerColumnas()
        grafica += '}'
        grafMostrar = self.mostrarGrafo(grafica)
        grafMostrar.render(nombreArchivo, format='png', view=True)
    
    def mostrarGrafo(self, contenido_dot):
        # Crear el objeto Graph usando el contenido dot
        dot = graphviz.Source(contenido_dot)
        return dot
    
