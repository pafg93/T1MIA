from listaEncabezados import ListaEncabezados

class Nodo:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.siguiente = None
        self.atras = None
        self.arriba = None
        self.abajo = None

class ListaLigada:
    def __init__(self, tamaño, filas, columnas):
        self.tamaño = tamaño
        self.filas = filas
        self.columnas = columnas
        self.datosFilas = ListaEncabezados()
        self.datosColumnas = ListaEncabezados()
        self.siguiente = None

    def agregarBloque(self, valor, fila, columna):
        if self.tamaño == 0 or self.tamaño - valor.tamaño < 0:
            print("El tamaño del archivo excede de los limites o ya no hay espacio en el disco.")
            return
        self.tamaño -= valor.tamaño
        nuevo = Nodo(fila, columna, valor)
        #insertar en filas
        datoFila = self.datosFilas.getEncabezado(fila)
        if datoFila == None:
            self.datosFilas.ingresar(fila)
            datoFila = self.datosFilas.getEncabezado(fila)
            datoFila.referencia = nuevo
        else:
            if nuevo.columna < datoFila.referencia.columna:
                nuevo.siguiente = datoFila.referencia
                datoFila.referencia.atras = nuevo
                datoFila.referencia = nuevo
            else:
                temp = datoFila.referencia
                while temp.siguiente is not None:
                    if nuevo.columna < temp.siguiente.columna:
                        nuevo.siguiente = temp.siguiente
                        temp.siguiente.atras = nuevo
                        temp.siguiente = nuevo
                        break
                    temp = temp.siguiente
                if temp.siguiente == None:
                    temp.siguiente = nuevo
                    nuevo.atras = temp
        #insertar columnas
        datoColumna = self.datosColumnas.getEncabezado(columna)
        if datoColumna == None:
            self.datosColumnas.ingresar(columna)
            datoColumna = self.datosColumnas.getEncabezado(columna)
            datoColumna.referencia = nuevo
        else:
            if nuevo.fila < datoColumna.referencia.fila:
                nuevo.abajo = datoColumna.referencia
                datoColumna.referencia.arriba = nuevo
                datoColumna.referencia = nuevo
            else:
                temp = datoColumna.referencia
                while temp.abajo is not None:
                    if nuevo.fila < temp.abajo.fila:
                        nuevo.abajo = temp.abajo
                        temp.abajo.arriba = nuevo
                        temp.abajo = nuevo
                        break
                    temp = temp.abajo
                if temp.abajo == None:
                    temp.abajo = nuevo
                    nuevo.arriba = temp

    def encontrar_bloque_libre(self, tamaño):
        actual = self.cabeza
        while actual:
            if actual.tamaño >= tamaño:
                return actual
            actual = actual.siguiente
        return None

    def asignar_bloque(self, tamaño):
        bloque_libre = self.encontrar_bloque_libre(tamaño)
        if bloque_libre:
            if bloque_libre.tamaño == tamaño:
                # Bloque exacto, eliminar de la lista
                self.eliminar_bloque(bloque_libre.inicio)
            else:
                # Reducción del bloque
                bloque_libre.inicio += tamaño
                bloque_libre.tamaño -= tamaño
            print(f"Bloque de {tamaño} asignado en la dirección {bloque_libre.inicio - tamaño}")
        else:
            print("No hay bloques libres disponibles de tamaño suficiente")

    def recorrerFilas(self):
        datoFila = self.datosFilas.principio
        while datoFila != None:
            print("Recorrer fila "+str(datoFila.valor))
            dato = datoFila.referencia
            while dato != None:
                print("Dato "+dato.valor+" x "+str(dato.fila)+" y "+str(dato.columna))
                dato = dato.siguiente
            datoFila = datoFila.siguiente

    def recorrerColumnas(self):
        datoColumna = self.datosColumnas.principio
        while datoColumna != None:
            print("Recorrer Columna "+str(datoColumna.valor))
            dato = datoColumna.referencia
            while dato != None:
                print("Dato "+dato.valor+" x "+str(dato.fila)+" y "+str(dato.columna))
                dato = dato.abajo
            datoColumna = datoColumna.siguiente
            
    def liberar_bloque(self, inicio, tamaño):
        self.agregar_bloque(inicio, tamaño)
        print(f"Bloque de {tamaño} liberado en la dirección {inicio}")
    
    def generar_graphviz(self, nombre_archivo="lista_enlazada.dot"):
        with open(nombre_archivo, "w") as file:
            file.write("digraph G {\n")
            file.write("rankdir=LR;\n")
            actual = self.cabeza
            while actual:
                file.write(f'nodo{actual.indice} [label="{actual.indice}", shape=box];\n')
                if actual.siguiente:
                    file.write(f'nodo{actual.indice} -> nodo{actual.siguiente.indice};\n')
                actual = actual.siguiente
            file.write("}\n")