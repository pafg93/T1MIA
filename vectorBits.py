class metodo_vector_bits:

    def __init__(self, size):
        # Inicializa el vector de bits con todos los bloques libres (0)
        self.memoria = [0] * size
        self.ubicacion = []

    def buscar_memoria(self, tamano):
        for i in range(len(self.memoria)):
            if self.memoria[i] == 0:
                dis = 0
                for j in range(i, len(self.memoria)):
                    if self.memoria[j] == 0:
                        dis += 1
                        if dis == tamano:
                            self.asignar_memoria(i, tamano)
                            return True
                    else:
                        dis = 0
                        break
        return False  # Si no se encuentra un bloque libre


    def asignar_memoria(self, pos, tamano):
        for i in range(tamano):
            self.memoria[pos + i] = 1
        self.guardar_ubicacion(pos, tamano)


    def guardar_ubicacion(self, pos, tamano):
        ubi = [pos, tamano]
        self.ubicacion.append(ubi)

    def eliminar_boque(self, no_bloque):

        if len(self.ubicacion) <= no_bloque:
            return False

        bloque = self.ubicacion[no_bloque]

        pos = bloque[0]
        tamano = bloque[1]

        for i in range(tamano):
            self.memoria[pos + i] = 0

        self.ubicacion.pop(no_bloque)
        return True


    def visualizar_memoria(self):
        # Muestra el estado actual de la memoria
        print("****************************")
        print("Estado de la memoria:", self.memoria)
        print("Ubicacion:", self.ubicacion)
        print("****************************")
