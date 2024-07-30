import time
import uuid
from listaLigada import ListaLigada

class Archivo:
    def __init__(self, id, nombre, tamaño, segmento) -> None:
        self.id = id
        self.nombre = nombre
        self.tamaño = tamaño
        self.segmento = segmento

def pruebasLigadas():
    id = uuid.uuid4()
    id2 = uuid.uuid4()
    id3 = uuid.uuid4()
    print("Creación del Disco - 25MB (26214400 bytes)")
    lista_memoria = ListaLigada(26214400, 7, 4)
    bloque1 = Archivo(id, "lectura.txt", 1048576, 0)
    bloque2 = Archivo(id2, "pruebas.txt", 1398101.33, 0)
    bloque3 = Archivo(id2, "pruebas.txt", 1398101.34, 1)
    bloque4 = Archivo(id2, "pruebas.txt", 1398101.33, 2)
    bloque5 = Archivo(id3, "HarryPotter.txt", 1048576, 0)
    bloque6 = Archivo(id3, "HarryPotter.txt", 1048576, 1)
    lista_memoria.generarGraphviz("0")
    time.sleep(1)
    print("Cargar archivo lectura.txt 1MB")
    # Prueba 1: Asignar un bloque
    inicio_tiempo = time.time()
    print("Cargar bloque 1 de 1048576 bytes")
    lista_memoria.agregarBloque(id, bloque1)
    fin_tiempo = time.time()
    print(f"Tiempo de asignación: {fin_tiempo - inicio_tiempo} segundos")
    lista_memoria.generarGraphviz("1")
    time.sleep(1)
    print("Cargar archivo pruebas.txt 4MB")
    # Prueba 2: Asignar 3 bloques
    inicio_tiempo = time.time()
    print("Cargar bloque 1 de 1398101.33 bytes")
    lista_memoria.agregarBloque(id2, bloque2)
    print("Cargar bloque 2 de 1398101.34 bytes")
    lista_memoria.agregarBloque(id2, bloque3)
    print("Cargar bloque 3 de 1398101.33 bytes")
    lista_memoria.agregarBloque(id2, bloque4)
    fin_tiempo = time.time()
    print(f"Tiempo de asignación: {fin_tiempo - inicio_tiempo} segundos")
    lista_memoria.generarGraphviz("2")
    time.sleep(1)
    print("Liberar archivo lectura.txt 1MB")
    # Prueba 3: Liberar un bloque
    inicio_tiempo = time.time()
    print("Liberar bloque 1 de 1048576 bytes")
    lista_memoria.liberarBloque(id, 0)
    fin_tiempo = time.time()
    print(f"Tiempo de liberación: {fin_tiempo - inicio_tiempo} segundos")
    lista_memoria.generarGraphviz("3")
    time.sleep(1)
    print("Cargar archivo HarryPotter.txt 2MB")
    # Prueba 4: Asignar 2 bloques
    inicio_tiempo = time.time()
    print("Cargar bloque 1 de 1048576 bytes")
    lista_memoria.agregarBloque(id3, bloque5)
    print("Cargar bloque 2 de 1048576 bytes")
    lista_memoria.agregarBloque(id3, bloque6)
    fin_tiempo = time.time()
    print(f"Tiempo de asignación: {fin_tiempo - inicio_tiempo} segundos")
    lista_memoria.generarGraphviz("4")
    time.sleep(1)
    print("Liberar de pruebas.txt 4MB")
    inicio_tiempo = time.time()
    # Prueba 4: Liberar un bloque
    print("Liberar bloque 2 de 1398101.34 bytes")
    lista_memoria.liberarBloque(id2, 1)
    fin_tiempo = time.time()
    print(f"Tiempo de liberación: {fin_tiempo - inicio_tiempo} segundos")
    lista_memoria.generarGraphviz("5")
