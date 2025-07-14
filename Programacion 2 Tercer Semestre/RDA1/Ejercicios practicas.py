#cada que se invoque una clase se debe invocar todas sun funciones tambien
#*************************************************************************************************************************
# class libro:
#     def __init__(self,titulo,autor,fecha):
#         self.titulo = titulo
#         self.autor = autor
#         self.fecha = fecha

#     def caracteristicas(self):
#         return f"El libro {self.titulo} fue escrito por {self.autor} en el año {self.fecha}"

#funciona con cualquiera de las dos
#libro1=libro("La mancha", "pepito", "2000")
#print(libro("La mancha", "pepito", "2000").caracteristicas())

#*************************************************************************************************************************
# class estudiante:
#     def __init__(self,nombre,carrera,nota):
#         self.nombre = nombre
#         self.carrera = carrera
#         self.nota = nota

#     def semestre (self):
#         return f"El estudiante {self.nombre} de la carrera {self.carrera} obtuvo la nota {self.nota}"

#     def verificacion(self):
#         if self.nota >= 7:
#             return f"El estudiante {self.nombre} de la carrera {self.carrera} a aprobado el curso"
#         else:
#             return f"El estudiante {self.nombre} de la carrera {self.carrera} a reprobado el curso"


# estudiante1 = estudiante("Juanito", "Gastronomia", 6)
# print(estudiante1.semestre())
# print(estudiante1.verificacion())

#*************************************************************************************************************************
# class Vehiculo:
#     def moverse(self):
#         return f"El vehiculo esta en movimiento"

# class Auto(Vehiculo):
#     def moverse(self):
#         return f"El auto se esta moviendo"

# vehiculo = Vehiculo()
# print(vehiculo.moverse())

# auto = Auto()
# print(auto.moverse())

#que estructura usaste, orientada a objetos o estructurada? y porque

#*************************************************************************************************************************
# class Pajaro:
#     def sonido(self):
#         print("El Pajaro canta")

# class Gato:
#     def sonido(self):
#         print("El Gato maulla")

# def ruido (animal):
#     animal.sonido()

# pajaro = Pajaro()
# gato = Gato()

# ruido(pajaro)
# ruido(gato)