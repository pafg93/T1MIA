def mostrar_menu():
    print("Tarea 1 de MIA sección B")
    print("1. Ejemplo de asignación por Vector de Bits")
    print("2. Ejemplo de asignación por Listas Ligadas")
    print("3. Salir")

def ejemplo_vector_bits():
    print("Ejemplo de asignación por Vector de Bits")
    # Aquí puedes agregar el código correspondiente a la asignación por Vector de Bits
    print("")

def ejemplo_listas_ligadas():
    print("Ejemplo de asignación por Listas Ligadas")
    # Aquí puedes agregar el código correspondiente a la asignación por Listas Ligadas
    print("")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
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