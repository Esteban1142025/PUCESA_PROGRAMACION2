#<<<<Codigo para la cola de atencion>>>>

class NodoSimple:
    def __init__(self, persona):
        self.persona = persona
        self.siguiente = None

class ColaAtencion:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def insertar(self, persona):
        nuevo = NodoSimple(persona)
        if not self.inicio:
            self.inicio = self.fin = nuevo
        else:
            self.fin.siguiente = nuevo
            self.fin = nuevo

    def eliminar(self):
        if self.inicio:
            print(f"Atendiendo a: {self.inicio.persona}")
            self.inicio = self.inicio.siguiente
            if not self.inicio:
                self.fin = None


    def mostrar(self):
        actual = self.inicio
        print("Cola de atención:")
        while actual:
            print(f"{actual.persona}")
            actual = actual.siguiente


#<<<<Codigo para el historial de navegacion>>>>>

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class HistorialNavegador:
    def __init__(self):
        self.actual = None  # Nodo donde se encuentra el usuario

    def visitar_pagina(self, url):
        nuevo_nodo = NodoDoble(url)
        if self.actual:
            # Eliminar páginas futuras
            self.actual.siguiente = None
            nuevo_nodo.anterior = self.actual
            self.actual.siguiente = nuevo_nodo
        self.actual = nuevo_nodo

    def atras(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior

    def adelante(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente

    def mostrar_historial(self):
        # aqui iremos al inicio del historial
        nodo = self.actual
        while nodo and nodo.anterior:
            nodo = nodo.anterior
        # aqui se imprime desde el inicio hasta el final
        while nodo:
            if nodo == self.actual:
                print(f">>> {nodo.dato} (estas aqui!)")
            else:
                print(f"--- {nodo.dato}")
            nodo = nodo.siguiente

    def pagina_actual(self):
        if self.actual:
            print(f"Página actual: {self.actual.dato}")


# Simulacion para la cola de atencion
print("---------------------------------------------------------------------------------------------------------")

cola = ColaAtencion()
cola.insertar("Persona 1")
cola.insertar("Persona 2")
cola.insertar("Persona 3")
cola.insertar("Persona 4")
cola.insertar("Persona 5")

cola.mostrar()
cola.eliminar()
cola.eliminar()
cola.mostrar()

print("---------------------------------------------------------------------------------------------------------")

# Simulacion para el historial de navegacion
print("Historial de navegacion:")

nav = HistorialNavegador()

nav.visitar_pagina("google.com")
nav.visitar_pagina("openai.com")
nav.visitar_pagina("github.com")

nav.atras()
nav.atras()

nav.visitar_pagina("stackoverflow.com")
nav.visitar_pagina("Facebook.com")

nav.mostrar_historial()
nav.pagina_actual()
print("---------------------------------------------------------------------------------------------------------")