class Paciente:
    def __init__(self,nombre,cedula,edad,sangre,fecha,diagnostico,tratamiento):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.sangre = sangre
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.consulta = {}

    def agregar_consulta (self, fecha, diagnostico, tratamiento):
        self.consulta = {
            "fecha": fecha,
            "diagnostico": diagnostico,
            "tratamiento":tratamiento}

    def agregar_fecha(self, fecha):
        self.fecha.append(fecha)

    def agregar_diagnostico(self,diagnostico):
        self.diagnostico.append(diagnostico)

    def agregar_tratamiento(self,tratamiento):
        self.tratamiento.append(tratamiento)

    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Cedula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de sangre: {self.sangre}")
        print(f"Consultas: {self.consulta}")