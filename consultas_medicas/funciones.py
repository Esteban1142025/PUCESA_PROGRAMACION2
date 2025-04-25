from paciente import Paciente

pacientes = []

def registrar_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    cedula = int(input("Ingrese la cédula del paciente: "))
    edad = int(input("Ingrese la edad del paciente:"))
    sangre = input("Ingrese el tipo de sangre del paciente: ")
    paciente = Paciente(nombre,cedula,edad,sangre)
    pacientes.append(paciente)
    print("El paciente se ha registrado!!!")

def buscar_paciente(cedula):
    for i in pacientes:
        if i.cedula == cedula:
            return i
    return None

def agregar_consulta():
    cedula = int(input("Ingrese la cédula del paciente: "))
    paciente = buscar_paciente(cedula)
    if paciente:
        try:
            fecha = input("Ingrese la fecha de la consulta: ")
            diagnostico = input("Ingrese el diagnóstico: ")
            tratamiento = input("Ingrese el tratamiento: ")
            paciente.agregar_fecha(fecha)
            paciente.agregar_diagnostico(diagnostico)
            paciente.agregar_tratamiento(tratamiento)
        except Exception:
            print("Parece que hubo un error!")
    else:
        print("Paciente no encontrado")

def mostrar_todos():
    if not pacientes:
        print("No hay pacientes registrados.\n")
    for i in pacientes:
        i.mostrar_datos()