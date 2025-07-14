from paciente import Paciente

pacientes = []

def registrar_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    cedula = int(input("Ingrese la cédula del paciente: "))
    edad = int(input("Ingrese la edad del paciente: "))
    sangre = input("Ingrese el tipo de sangre del paciente: ")
    paciente = Paciente(nombre,cedula,edad,sangre)
    pacientes.append(paciente)
    print("El paciente se ha registrado!!!")

def buscar_paciente():
    cedula = int(input("Ingrese la cédula del paciente: "))
    for paciente in pacientes:
        if paciente.cedula == cedula:
            print(paciente.mostrar_datos())
            return paciente
    return None

def agregar_consulta():
    paciente = buscar_paciente()
    if paciente:
            fecha = input("Ingrese la fecha de la consulta: ")
            diagnostico = input("Ingrese el diagnóstico: ")
            tratamiento = input("Ingrese el tratamiento: ")
            paciente.agregar_datos_consulta(fecha,diagnostico,tratamiento)

            datos = paciente.consulta_medica(fecha, diagnostico, tratamiento)
            paciente.agregar_datos_consulta(fecha, diagnostico, tratamiento)
            pacientes.append(datos)
            print("Consulta agendada")
    else:
        print("Paciente no encontrado")

def mostrar_todos():
    if not pacientes:
        print("No hay pacientes registrados.\n")
    for paciente in pacientes:
        paciente.mostrar_datos()