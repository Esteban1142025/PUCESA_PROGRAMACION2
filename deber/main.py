from Funciones2 import registrado_de_paciente, agregar_consulta_medica, mostrar_paciente, mostrar_todos

print("Hecho por: Alejandro Sutherland\n")
print("Fecha: 25/04/25\n")


def menu():
    while True:
        print("----- SISTEMA DE REGISTRO DE PACIENTES -----")
        print("1. Registrar nuevo paciente")
        print("2. Buscar paciente")
        print("3. Agregar consulta médica a un paciente")
        print("4. Mostrar todos los pacientes")
        print("5. Salir")
        
#Menu completado
#registrar nuevo paciente completado
#buscar paciente completado
#mostrar todos los pacientes completado
#agregar consulta médica a un paciente completado

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrado_de_paciente()
        elif opcion == "2":
            mostrar_paciente()    
            
        elif opcion == "3":
            agregar_consulta_medica()
        
        elif opcion == "4":
            mostrar_todos()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

# Ejecutar menú
if __name__ == "__main__":
    menu()
