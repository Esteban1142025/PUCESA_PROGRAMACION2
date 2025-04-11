# def funcion(nombre):
#     print("Estamos estuiando Python",nombre)
# funcion("Esteban")

# print("***Paso de argumentos a una funcion***")
# def datos (nombre,apellido):
#     print("Estamos estuiando Python",nombre,apellido)
# datos("Esteban","Ruiz")
# datos(nombre="Esteban",apellido="Ruiz")

# def area_triangulo(base,altura):
#     calc=base*altura/2
#     print(calc)
# #esta es una funcion posicional
# #la funcion nominal utiliza clave-valor
# area_triangulo(2,3)
# area_triangulo(4,5)

# #argumento con parametro por defecto
# def welcome (nombre,lenguaje='Python'):
#     print("Bienvenido a",lenguaje,nombre + '!')
# welcome("Esteban")
# welcome("Esteban","PHP")

# #pasar un número indeterminado de argumentos
# def menu (*platos):
#     print('Hoy tenemos: ',end='')
#     for plato in platos:
#         print(plato,end=', ')
# menu('pasta','pizza','ensalada')

# def contacto(**info):
#     print("Datos de contacto")
#     for clave,valor in info.items():
#         print(clave,":",valor)
# contacto(Nombre = "Esteban", Email = "nose@gmail.com" "\n")
# contacto(Nombre = "Esteban", Email = "nose@gmail.com", Direccion = "Enrique Segoviano")

# #las funciones son objetos
# def saludo(nombre):
#     print("Hola como estas",nombre)
#     return
# bienvenida = saludo
# bienvenida("Esteban")

# #funciones recursivas
# def cuenta_regresiva(numero):
#     numero -= 1
#     if numero > 0:
#         print(numero)
#         cuenta_regresiva(numero)
#     else:
#         print("Adios master!")
#     print("Fin de la función",numero)
# cuenta_regresiva(5)


# una clase en python es un plano para crear un objeto
# proporciona una estructura que define las propiedades y comportamientos de los objetos
# que se van a crear a partir de ella
# class Persona:
#     def __init__(self,nombre,edad,ocupacion):
#         self.nombre = nombre
#         self.edad = edad
#         self.ocupacion = ocupacion
#     def descripcion(self):
#         return f"Nombre: {self.nombre}, Edad:{self.edad}, Ocupacion:{self.ocupacion}"

# #creamos los objetos de tipo persona
# persona1 = Persona("Juan", 30, "Ingeniero")
# persona2 = Persona("Maria", 25, "Dcotora")

# #Mostramos la descripcion de cada persona
# print(persona1.descripcion())
# print(persona2.descripcion())


# class Persona:
#     def __init__(self,nombre,edad,ocupacion):
#         self.nombre = nombre
#         self.edad = edad
#         self.ocupacion = ocupacion
#     def descripcion(self):
#         return f"Nombre: {self.nombre}, Edad:{self.edad}, Ocupacion:{self.ocupacion}"

# #Pedimos al usuario que ingrese informacion para crear objetos Persona
# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))
# ocupacion = input("Ingrese su ocupacion: ")

# #creamos un objeto de tipo Persona con la informacion porporcionada por el usuario
# nueva_persona = Persona(nombre,edad,ocupacion)

# #Mostramos la descripcion de la persona creada
# print("\n Informacion de la persona creada")
# print(nueva_persona.descripcion())


class Persona:
    def __init__(self,nombre,edad,ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        
    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad:{self.edad}, Ocupacion:{self.ocupacion}"
def mostrar_menu():
    print("""
-- Gestión de Personas --
1. Agregar persona
2. Mostrar todas las personas
3. Buscar persona por nombre
4. Salir
""")

personas = []

while True:
    mostrar_menu()
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        ocupacion = input("Ingrese la ocupación de la persona: ")
        nueva_persona = Persona(nombre,edad,ocupacion)
        personas.append(nueva_persona)
        print(f"La persona '{nombre}' ha sido agregada")
    elif opcion == "2":
        if len(personas) > 0:
            print("\n--- Lista de Personas ---")
            for persona in personas:
                print(persona.descripcion())
        else:
            print("No hay personas en la lista")
    elif opcion == "3":
        if len(personas) > 0:
            nombre_buscar = input("Ingrese el nombre de la persona a buscar: ")
            encontrada = False
            for persona in personas:
                if persona.nombre.lower() == nombre_buscar.lower():
                    print("Personas encontrada")
                    print(persona.descripcion())
                    encontrada = True
                    break
            if not encontrada:
                print(f"No se encontró a '{nombre_buscar}' en la lista.")
        else:
            print("No hay personas en la lista")
    elif opcion == "4":
        print("Hasta luego!")
        break
    
    else:
        print("Opcion no válida. Por favor. seleccione una opción válida")