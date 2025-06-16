class PilaTareas:
    def __init__(self):
        self.items = []
        
    def agregar_tarea(self, tarea):
        self.items.append(tarea)
        
    def terminar_tarea(self):
        if TAR:
            completada = self.items.pop()
            print("Tarea completada:", completada)
        else:
            print("No hay tareas para completar.")
            print("La tarea",completada, "fue finalizada con exitosamente")
        
    def ver_ultima_tarea(self):
        if self.items:
            print("Tarea más reciente:", self.items[-1])
        else:
            print("No hay tareas pendientes.")
        
    def tamaño(self):
        if len(self.items) == 0:
            print("Todas las tareas han sido completadas.")
        else:
            print("Tareas restantes:", self.items)

pila = PilaTareas()
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
                1. Ingresar una nueva tarea
                2. Finalizar una tarea
                3. Ver ultima tarea
                4. Comprobar tareas pendientes
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
                pila.terminar_tarea()
                
            elif opcion == 3:
                pila.ver_ultima_tarea()

            elif opcion == 4:
                pila.tamaño()

            elif opcion == 5:
                print("Finalizando programa...")
                break