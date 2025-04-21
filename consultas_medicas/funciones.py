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

def mostrar_todos():
    if not pacientes:
        print("No hay pacientes registrados.\n")
    for i in pacientes:
        i.mostrar_datos()