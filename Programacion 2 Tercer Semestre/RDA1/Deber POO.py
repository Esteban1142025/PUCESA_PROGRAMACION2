#*************************************************************************************************************************
#Explicacion: Se define una clase libro en la cual le doy los atributos titulo, autor y fecha
#despues imprimo sus caracteristicas con un print.

#Resolucion: El ejercicio se resolvio usando una clase y definiendo sus atributos y metodos.

#Estructura: Se utilizo la estructura orientada a objetos porque se trabajo con una clase solamente.

class libro:
    def __init__(self,titulo,autor,fecha):
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha

    def caracteristicas(self):
        return f"El libro {self.titulo} fue escrito por {self.autor} en el año {self.fecha}"

print(libro("La mancha", "pepito", "2000").caracteristicas())

#*************************************************************************************************************************
#Explicacion: Se define una clase estudiante a la cual le otorgo los atributos nombre, carrera y nota
#despues se imprime su nota y se realiza una verificacion la cual define si pasa o reprueba el curso.

#Resolucion: La clase estudiante guarda 3 datos (nombre, carrera y nota), la nota tenia que ser mayor o igual a 7
#para aprobar el curso, se utiliza un if para realizar la verificacion, luego se imprime el resultado y los datos del estudiante.

#Estructura: Se utilizo en su mayoria la estructura orientada a objetos y solo en la verificacion
#se utilizo la estructura estructurada.

class estudiante:
    def __init__(self,nombre,carrera,nota):
        self.nombre = nombre
        self.carrera = carrera
        self.nota = nota

    def semestre (self):
        return f"El estudiante {self.nombre} de la carrera {self.carrera} obtuvo la nota {self.nota}"

    def verificacion(self):
        if self.nota >= 7:
            return f"El estudiante {self.nombre} de la carrera {self.carrera} a aprobado el curso"
        else:
            return f"El estudiante {self.nombre} de la carrera {self.carrera} a reprobado el curso"


estudiante1 = estudiante("Juanito", "Gastronomia", 7)
print(estudiante1.semestre())
print(estudiante1.verificacion())


#*************************************************************************************************************************
#Explicacion: Se define una clase vehiculo a la cual le doy un metodo "moverse", el mismo que sera
#heredado por mi segunda clase Auto y lo sobreescribira.

#Resolucion: La clase vehiculo hereda a la clase Auto el metodo "moverse", lo modifica y posteriormente se imprime el resultado.

#Estructura: Se utilizo la estructura orientada a objetos porque se hace uso de clases y herencia.

class Vehiculo:
    def moverse(self):
        return f"El vehiculo esta en movimiento"

class Auto(Vehiculo):
    def moverse(self):
        return f"El auto se esta moviendo"

vehiculo = Vehiculo()
print(vehiculo.moverse())

auto = Auto()
print(auto.moverse())

#*************************************************************************************************************************
#Explicacion: Se definen dos clases, Pajaro y Gato, con el metodo "sonido" que sera utilizado
#de forma polimorfica por ambas de forma diferente.

#Resolucion: Se utiliza el metodo "sonido" de forma polimorfica usando una funcion "ruido" que nos permitira
#utilizar dicho metodo en ambas clases de manera distinta.

#Estructura: Se utilizo la estructura otientada a objetos porque se hace uso de clases y polimorfismo.

class Pajaro:
    def sonido(self):
        print("El Pajaro canta")

class Gato:
    def sonido(self):
        print("El Gato maulla")

def ruido (animal):
    animal.sonido()

pajaro = Pajaro()
gato = Gato()

ruido(pajaro)
ruido(gato)