from Paciente import paciente
separador = "--------------------------------------------------------------------------------"
separador2 = "|| <----------------------------------------> ||"
# Lista global para guardar pacientes
pacientes = []

def registrado_de_paciente():
    while True:
        nombre = input("Nombre: ").lower()
        try:
            cedula = int(input("Cedula de ciudadanía: "))
            edad = int(input("Edad: "))
        except ValueError:
            print("Error: La cédula y la edad deben ser números.")
            continue
        tipo_de_sangre = input("Tipo de sangre: ")
        
        pa100te = paciente(nombre, cedula, edad, tipo_de_sangre)
        pacientes.append(pa100te)
        print("Paciente registrado con éxito.\n")
        break

def agregar_consulta_medica():

    cedula = int(input("Ingrese la cedula del paciente: "))
    for paciente in pacientes:
        if paciente.cedula == cedula:
            print("Paciente encontrado.\n")
            print("||---Datos de consulta médica---||")
    if paciente.cedula == cedula:
        fecha = input("Ingrese la fecha de la consulta: ")
        diagnostico = input("Ingrese el diagnóstico: ")
        tratamiento = input("Ingrese el tratamiento: ")
            
        adicional = paciente.R_CONSULTA_MEDICA(fecha, diagnostico, tratamiento)
        paciente.agregar_datos(fecha, diagnostico, tratamiento)
        pacientes.append(adicional)
        print("Consulta agregada con éxito ||c:)||.\n")

    else:
        print("Paciente no encontrado.\n")

def mostrar_paciente():
    cedula = input("Ingrese la cedula del paciente: ")
    for paciente in pacientes:
        if paciente.cedula == cedula:
            paciente.mostrar_datos()
            if paciente.cedula == cedula:
                print("||---Datos de consulta médica---||")
                print(f"\nFecha: {paciente.fecha}")
                print(f"Diagnóstico: {paciente.diagnostico}")
                print(f"Tratamiento: {paciente.tratamiento}")
            return
    print("Paciente no encontrado.\n")

def mostrar_todos():
    if not pacientes:
        print("No hay pacientes registrados.\n")
    for est in pacientes:
        est.mostrar_datos()

