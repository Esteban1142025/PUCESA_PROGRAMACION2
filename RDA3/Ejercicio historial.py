# Clase NodoDoble
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

# Clase HistorialNavegador
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
        else:
            print("No hay página anterior.")

    def adelante(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
        else:
            print("No hay página siguiente.")

    def mostrar_historial(self):
        # Ir al inicio del historial
        nodo = self.actual
        while nodo and nodo.anterior:
            nodo = nodo.anterior
        # Imprimir desde el inicio hasta el final
        while nodo:
            if nodo == self.actual:
                print(f">>> {nodo.dato} (estas aqui!)")
            else:
                print(f"--- {nodo.dato}")
            nodo = nodo.siguiente

    def pagina_actual(self):
        if self.actual:
            print(f"Página actual: {self.actual.dato}")
        else:
            print("No se visito ninguna pagina.")



nav = HistorialNavegador()

nav.visitar_pagina("google.com")
nav.visitar_pagina("openai.com")
nav.visitar_pagina("github.com")

nav.atras()
nav.atras()

nav.visitar_pagina("stackoverflow.com")

nav.mostrar_historial()
nav.pagina_actual()