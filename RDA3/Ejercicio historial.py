# NodoDoble representa un nodo en una lista doblemente enlazada
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato         # URL o nombre de la pagina
        self.anterior = None     # Puntero al nodo anterior
        self.siguiente = None    # Puntero al nodo siguiente

# HistorialNavegador permite simular un historial de navegación con retroceso y avance
class HistorialNavegador:
    def __init__(self):
        self.actual = None  # Nodo donde se encuentra el usuario actualmente

    # Visita una nueva pagina
    def visitar_pagina(self, url):
        nuevo_nodo = NodoDoble(url)
        if self.actual:
            # Eliminar páginas futuras (como lo hace un navegador real)
            self.actual.siguiente = None
            nuevo_nodo.anterior = self.actual
            self.actual.siguiente = nuevo_nodo
        self.actual = nuevo_nodo  # Actualizamos la posición actual

    # Retrocede a la pagina anterior
    def atras(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior

    # Avanza a la pagina siguiente
    def adelante(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente

    # Muestra todo el historial desde el inicio hasta la pagina actual
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

    # Muestra la pagina actual
    def pagina_actual(self):
        if self.actual:
            print(f"Página actual: {self.actual.dato}")

print("Historial de navegacion:")

nav = HistorialNavegador()

nav.visitar_pagina("google.com")       # Visita la pagina 1
nav.visitar_pagina("openai.com")       # Visita la pagina 2
nav.visitar_pagina("github.com")       # Visita la pagina 3

nav.atras()                            # Retrocede a openai.com
nav.atras()                            # Retrocede a google.com

nav.visitar_pagina("stackoverflow.com")  # Visita nueva pagina ("borra" las otras dos paginas)
nav.visitar_pagina("Facebook.com")       # Visita otra pagina

nav.mostrar_historial()  # Muestra todo el historial
nav.pagina_actual()      # Muestra la pagina actual