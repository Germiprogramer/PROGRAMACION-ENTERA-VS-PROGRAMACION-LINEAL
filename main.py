from combinar_restr import *
from modelo_basico import *
from modelo_general import *

if __name__ == "__main__":
    while True:
        # Mostrar el menú
        print("\nMenú:")
        print("1. Ejecutar Opción 1")
        print("2. Ejecutar Opción 2")
        print("3. Ejecutar Opción 3")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == '1':
            resolver_ejercito1()
        elif opcion == '2':
            resolver_ejercito2()
        elif opcion == '3':
            resolver_ejercito3()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")
