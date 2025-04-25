class Paciente:
    def __init__(self,nombre,cedula,edad,sangre):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.sangre = sangre
        self.consulta = {}

    def consulta_medica(self, fecha, diagnostico, tratamiento):
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.datos_consulta = []
        
    def agregar_datos_consulta(self, fecha, diagnostico, tratamiento):
        self.datos_consulta.append(fecha)
        self.datos_consulta.append(diagnostico)
        self.datos_consulta.append(tratamiento)


    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Cedula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de sangre: {self.sangre}")
        print(f"Consultas: {self.consulta}")