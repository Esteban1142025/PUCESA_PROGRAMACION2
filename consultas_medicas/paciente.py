class Paciente:
    def __init__(self,nombre,cedula,edad,sangre):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.sangre = sangre
        self.consulta = {}

    def agregar_consulta (self, fecha, diagnostico, tratamiento):
        self.consulta = {
            "fecha": fecha,
            "diagnostico": diagnostico,
            "tratamiento":tratamiento}

    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Cedula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de sangre: {self.sangre}")
        print(f"Consultas: {self.consulta}")