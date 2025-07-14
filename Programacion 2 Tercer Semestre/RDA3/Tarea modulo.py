#<<<<Codigo para la cola de atencion>>>>

# NodoSimple representa un nodo en una lista enlazada simple
class NodoSimple:
    def __init__(self, persona):
        self.persona = persona  # Almacena el nombre de la persona
        self.siguiente = None   # Puntero al siguiente nodo en la lista

# ColaAtencion implementa una cola con una lista enlazada simple (FIFO)
class ColaAtencion:
    def __init__(self):
        self.inicio = None  # Primer elemento en la cola
        self.fin = None     # Último elemento en la cola

    # Inserta una nueva persona al final de la cola
    def insertar(self, persona):
        nuevo = NodoSimple(persona)
        if not self.inicio:  # Si la cola está vacia
            self.inicio = self.fin = nuevo
        else:  # Si ya hay elementos
            self.fin.siguiente = nuevo
            self.fin = nuevo

    # Atiende (o elimina) a la persona al frente de la cola
    def eliminar(self):
        if self.inicio:
            print(f"Atendiendo a: {self.inicio.persona}")
            self.inicio = self.inicio.siguiente  # Mueve el inicio al siguiente nodo
            if not self.inicio:
                self.fin = None  # Si ya no hay mas nodos, la cola queda vacia

    # Muestra todas las personas actualmente en la cola
    def mostrar(self):
        actual = self.inicio
        print("Cola de atención:")
        while actual:
            print(f"{actual.persona}")
            actual = actual.siguiente


#<<<<Codigo para el historial de navegacion>>>>>

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


# Simulacion para la cola de atencion
print("---------------------------------------------------------------------------------------------------------")

cola = ColaAtencion()
cola.insertar("Persona 1")  # Agrega a la cola
cola.insertar("Persona 2")
cola.insertar("Persona 3")
cola.insertar("Persona 4")
cola.insertar("Persona 5")

cola.mostrar()  # Muestra la cola completa
cola.eliminar() # Atiende a la primera persona (Persona 1)
cola.eliminar() # Atiende a la segunda persona (Persona 2)
cola.mostrar()  # Muestra la cola restante

print("---------------------------------------------------------------------------------------------------------")

# Simulacion para el historial de navegacion
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
print("---------------------------------------------------------------------------------------------------------")