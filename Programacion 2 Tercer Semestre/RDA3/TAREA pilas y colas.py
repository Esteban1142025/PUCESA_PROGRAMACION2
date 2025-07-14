#Reflexion final
#su principal diferencia entre ambas es su orden de acceso, LIFO (Pila) y FIFO (Cola), ademas en colas con prioridades se
#requiere de un argumento mas para su ordenamiento y hacer uso de lambda para la comparacion de prioridades.

class PilaTareas:
    def __init__(self):
        self.items = []
        
    def agregar_tarea(self, tarea):
        self.items.append(tarea)
        
    def terminar_tarea(self):
        if TAR:
            completada = self.items.pop()
            print("La tarea",completada, "fue finalizada exitosamente")
        else:
            print("No hay tareas para completar.")

    def ver_ultima_tarea(self):
        if self.items:
            print("Tarea más reciente:", self.items[-1])
        else:
            print("No hay tareas pendientes.")
        
    def tamaño(self):
        print(f"Actualmente tiene {len(self.items)} tareas asignadas")

class ColaPrioridadClientes:
    def __init__(self):
        self.items = []
        
    def agregar_cliente(self, cliente, prioridad):
        self.items.append((prioridad,cliente))
        
    def atender_cliente(self):
        if not len(self.items) == 0:
            self.items.sort(key=lambda x: x[0])
            cliente_atendido = self.items.pop(0)
            print(f"Se atendió a: {cliente_atendido[1]} (Prioridad {cliente_atendido[0]})")
            return cliente_atendido
        else:
            print("No hay mas clientes por atender")
            return None

    def mostrar_pendientes(self):
        clientes_pendientes = sorted(self.items)
        return clientes_pendientes
        
    def tamaño(self):
        print(f"Actualmente tiene {len(self.items)} clientes pendientes")

pila = PilaTareas()
cola = ColaPrioridadClientes()

while True:
    print("""Seleccione un programa: 
        1. Gestor de Tareas
        2. Atencion de Clientes
        3. Salir
        """)
    opcion = int(input("Ingrese su opción: "))
    if opcion not in [1,2,3]:
        print("Error! Seleccione una opcion valida...")
    elif opcion == 1:
        while True:
            print("""
                <<<<<<<<BIENVENIDO AL GESTOR DE TAREAS>>>>>>>>
                1. Ingrese sus 10 tareas asignadas
                2. Finalizar una tarea
                3. Ver ultima tarea
                4. Total de tareas asignadas
                5. Salir
                """)
            
            opcion = int(input("Ingrese una opcion disponible: "))
            if opcion not in [1,2,3,4,5]:
                print("Error! Seleccione una opcion valida...")

            elif opcion == 1:
                cont = 0
                while True:
                    TAR = input("Ingrese la tarea asignada: ")
                    pila.agregar_tarea(TAR)
                    cont += 1
                    if cont == 10:
                        break

            elif opcion == 2:
                try:
                    pila.terminar_tarea()
                except IndexError:
                    print("Ya se han finalizado todas las tareas")

            elif opcion == 3:
                pila.ver_ultima_tarea()
            
            elif opcion == 4:
                pila.tamaño()

            elif opcion == 5:
                print("Finalizando programa...")
                break
    elif opcion == 2:
        while True:
            print("""
                <<<<<<<<BIENVENIDO A ATENCION DE CLIENTES>>>>>>>>
                1. Agregar nuevo cliente
                2. Atender un cliente
                3. clientes pendientes
                4. Total de clientes
                5. Salir
                """)
            opcion = int(input("Ingrese una opcion disponible: "))
            if opcion not in [1,2,3,4,5]:
                print("Error! Seleccione una opcion valida...")
            
            elif opcion == 1:
                cont = 0
                print("Debe ingresar 8 clientes:")
                while True:
                    cliente = input("Ingrese un nuevo cliente: ")
                    prioridad = int(input("""
                                    Prioridades:
                                    1 = Alta
                                    2 = Media
                                    3 = Baja
                                    Ingrese la prioridad del cliente: """))
                    cola.agregar_cliente(prioridad,cliente)
                    cont += 1
                    if cont == 8:
                        break
            
            elif opcion == 2:
                cola.atender_cliente()
            
            elif opcion == 3:
                print("Clientes pendientes (Nombre | Prioridad): \n", cola.mostrar_pendientes())
            
            elif opcion == 4:
                cola.tamaño()
            
            elif opcion == 5:
                print("Finalizando programa...")
                break
    elif opcion == 3:
        print("Saliendo del programa...")
        break