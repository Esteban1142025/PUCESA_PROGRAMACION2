#Gestion de reportes medicos (Pilas)
# Clase ReporteMedico
class ReporteMedico:
    def __init__(self, tipo, observacion):
        self.tipo = tipo
        self.observacion = observacion
        self.anterior = None
        self.siguiente = None

# Clase PilaReportes
class PilaReportes:
    def __init__(self):
        self.actual = None

    def agregar_reporte(self, tipo, observacion):
        nuevo_reporte = ReporteMedico(tipo,observacion)
        if self.actual:
            self.actual.siguiente = None
            nuevo_reporte.anterior = self.actual
            self.actual.siguiente = nuevo_reporte
        self.actual = nuevo_reporte

    def eliminar_reporte(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior

    def mostrar_reportes(self):
        nodo = self.actual
        while nodo and nodo.anterior:
            nodo = nodo.anterior
        while nodo:
            if nodo == self.actual:
                print(f"--- {self.actual.tipo} | {self.actual.observacion}")
            else:
                print(f"--- {nodo.tipo} | {nodo.observacion}")
            nodo = nodo.siguiente
    def reporte_actual(self):
        if self.actual:
            print(f"Reporte actual: {self.actual.tipo} | {self.actual.observacion}")

Reporte = PilaReportes()



#Simulacion de Evacuacion Escolar (Colas)
# Clase EstudianteEvacuacion
class EstudianteEvacuacion:
    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula

# Clase ColaEvacuacion
class ColaEvacuacion:
    def __init__(self):
        pass  # Completa la implementación

    def agregar_estudiante(self, nombre, aula):
        pass

    def atender_estudiante(self):
        pass

    def mostrar_en_espera(self):
        pass

# Pruebas aquí

















while True:
    print("""
        <<<Sistema de Gestion Escolar de Emergencia>>>
        
        Bienvenido! Seleccione una opción para continuar:
        1) Gestion de Reportes Medicos
        2) Simulacion de Evacuacion Escolar
        3) Registro de visitas medicas
        4) Bitacora de Incidentes Escolares
        5) Salir
        """)
    opcion = int(input("Ingrese el numero de la funcionalidad que desea utilizar: "))
    if opcion not in [1,2,3,4,5]:
        print("Error! Seleccione una opcion valida...")
    elif opcion == 1:
        while True:
            print("""
                Gestion de Reportes Medicos
                1) Agregar reporte medico
                2) Eliminar reporte medico
                3) Mostrar reportes medicos
                4) Reporte actual
                5) Volver
                """)

            opcion = int(input("Ingrese el numero de la funcionalidad que desea utilizar: "))
            if opcion not in [1,2,3,4,5]:
                print("Error! Seleccione una opcion valida...")
            elif opcion == 1:
                print(f"Ingrese los datos del paciente:\n")
                if Reporte.actual:
                    Reporte.agregar_reporte(input("Ingrese el tipo de sintoma: "), input("Ingrese la observacion: "))
                else:
                    Reporte.agregar_reporte(input("Ingrese el nombre del paciente: "), input("Ingrese el apellido del paciente: "))
            elif opcion == 2:
                Reporte.eliminar_reporte()
                print("Reporte eliminado!")
                print("Se actualizara la lista de reportes medicos en el siguiente ingreso de datos...")
            elif opcion == 3:
                Reporte.mostrar_reportes()
            elif opcion == 4:
                Reporte.reporte_actual()
            elif opcion == 5:
                break

    elif opcion == 2:
        while True:
            print("""
                
                """)
    elif opcion == 3:
        while True:
            print("""
                
                """)
    elif opcion == 4:
        while True:
            print("""
                
                """)
    elif opcion == 5:
        print("Saliendo del programa...")
        break