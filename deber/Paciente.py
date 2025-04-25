class paciente:
    def __init__(self,nombre, cedula, edad,tipo_de_sangre):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tipo_de_sangre = tipo_de_sangre
        self.Datos1 = []

    def agregar_datos(self, nombre, cedula, edad,tipo_de_sangre):
        self.Datos1.append(nombre)
        self.Datos1.append(cedula)
        self.Datos1.append(edad)
        self.Datos1.append(tipo_de_sangre)



    def R_CONSULTA_MEDICA(self, fecha, diagnostico, tratamiento):
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.Datos2 = []
        
    def agregar_datos(self, fecha, diagnostico, tratamiento):
        self.Datos2.append(fecha)
        self.Datos2.append(diagnostico)
        self.Datos2.append(tratamiento)

    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de sangre: {self.tipo_de_sangre}")
