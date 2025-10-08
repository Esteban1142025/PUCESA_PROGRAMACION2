# class Persona:
#     def __init__(self,nombre, edad):
#         self.nombre = nombre
#         self.edad= edad
        

#     def saludar(self):
#         return f"Hola, me llamo {self.nombre} y tengo {self.edad} años"
    

# persona1 = Persona("Edison", 37)
# persona2 = Persona("Maria", 25)

# print(persona1.saludar())
# print(persona2.saludar())

class E_Ingenierias:
    def __init__(self,carrera,nombre):
        self.carrera = carrera
        self.nombre = nombre
        
    def presentacion(self):
        return f"Me llamo {self.nombre} y estudio la carrera de {self.carrera}"

# yo = E_Ingenierias("Ingenieria en sistemas", "Esteban")


# print(yo.presentacion())


class Datos(E_Ingenierias):
    def __init__(self, carrera, nombre, nivel, cedula):
        super().__init__(carrera, nombre)
        self.cedula = cedula
        self.nivel = nivel
    
    def presentacion_completa(self):
        return f"{self.presentacion()} estoy cursando {self.nivel}, mi cedula es: {self.cedula}"

# yo2 = Datos("Ingenieria en sistemas", "Esteban", "Cuarto Semestre", 1851025104)

# print(yo2.presentacion_completa())

class MasDatos (Datos):
    def __init__(self, carrera, nombre, nivel, cedula, materias):
        super().__init__(carrera, nombre, nivel, cedula)
        self.materias = materias
    
    def p_c_completa(self):
        return f"{self.presentacion_completa()}, mis materias favoritas son: {self.materias}"

yo3 = MasDatos("Ingenieria en sistemas", "Esteban", "Cuarto Semestre", 1851025104,"Programacion IV y Base de Datos I")

# print(yo3.p_c_completa())

class AunMasDatos(MasDatos):
    def __init__(self, carrera, nombre, nivel, cedula, materias, hora):
        super().__init__(carrera, nombre, nivel, cedula, materias)
        self.hora = hora
    
    def p_c_c_completa(self):
        return f"{self.p_c_completa()} y entro a las {self.hora}"

yo4 = AunMasDatos("Ingenieria en sistemas", "Esteban", "Cuarto Semestre", 1851025104,"Programacion IV y Base de Datos I", "7 AM de la manaña")

print(yo4.p_c_c_completa())