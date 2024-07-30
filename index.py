from vectorBits import metodo_vector_bits
from pruebaLigada import pruebasLigadas
import os
import time

def mostrar_menu():
    print("Tarea 1 de MIA sección B")
    print("1. Ejemplo de asignación por Vector de Bits")
    print("2. Ejemplo de asignación por Listas Ligadas")
    print("3. Salir")


def mostrar_menu_vector_bits():
    print("Ejemplo de asignación por Vector de Bits")
    print("1. Guardar  Bloque")
    print("2. Eliminar Bloque")
    print("3. Imprimir Estado Actual")
    print("4. Salir")
    print("")

def ejemplo_vector_bits():
    memoria = metodo_vector_bits(32)
    while True:
        mostrar_menu_vector_bits()
        opcion = input("Seleccione una opción: ")        
        if opcion == "1":
            limpiar_consola()
            tamano = input("Tamaño del Bloque: ") 
            inicio_ejecucion = time.time()
            bloque_guardado = memoria.buscar_memoria(int(tamano))
            fin_ejecucion = time.time()
            if bloque_guardado:
                print("El tiempo de ejecucion para Guardar el bloque es de: ", fin_ejecucion - inicio_ejecucion)
            else:
                print("Error Al guardar datos")
        elif opcion == "2":
            limpiar_consola()
            bloque = input("Elinar Bloque: ")
            inicio_ejecucion = time.time()
            bloque_eliminado = memoria.eliminar_boque(int(bloque)) 
            fin_ejecucion = time.time()
            if bloque_eliminado:
                print("El tiempo de ejecucion para eliminar el bloque es de: ", fin_ejecucion - inicio_ejecucion)
            else:
                print("Error al borrar un bloque")
        elif opcion == "3":
            limpiar_consola()
            memoria.visualizar_memoria()
        elif opcion == "4":
            limpiar_consola()
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
    

def ejemplo_listas_ligadas():
    print("Ejemplo de asignación por Listas Ligadas")
    pruebasLigadas()
    print("")

def limpiar_consola():
    os.system("cls")  # Comando para Windows


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: \n")
        
        if opcion == "1":
            ejemplo_vector_bits()
        elif opcion == "2":
            ejemplo_listas_ligadas()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()