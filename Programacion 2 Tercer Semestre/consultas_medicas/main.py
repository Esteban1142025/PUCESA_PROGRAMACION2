from funciones import registrar_paciente, agregar_consulta, buscar_paciente, mostrar_todos

def menu_principal():
    while True:
        print("""
        1) Registrar paciente
        2) Buscar paciente
        3) Agregar consulta medica a un paciente
        4) Mostrar registro de pacientes
        5) Salir
        """)
    
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            registrar_paciente()
        elif opcion == 2:
            buscar_paciente()
        elif opcion == 3:
            agregar_consulta()
        elif opcion == 4:
            mostrar_todos()
        elif opcion == 5:
            print("Gracias por usar el programa")
            print("Adios!")
            break
        else:
            print("Seleccione una opcion valida!")

if __name__ == "__main__":
    menu_principal()