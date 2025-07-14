from funciones import registrar_libro, registrar_prestamo, buscar_libro, mostrar_biblioteca

def menu_principal():
    while True:
        print("""
        1) Registrar un nuevo libro
        2) Registrar un prestamo
        3) Mostrar informacion de un libro
        4) Mostrar todos los libros
        5) Salir
        """)
        
        opcion = int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            registrar_libro()
        elif opcion == 2:
            registrar_prestamo()
        elif opcion == 3:
            buscar_libro()
        elif opcion == 4:
            mostrar_biblioteca()
        elif opcion == 5:
            print("Gracias por utilizar el programa")
            print("Adios!")
            break
        else:
            print("Seleccione una opcion valida!!!")

if __name__ == "__main__":
    menu_principal()