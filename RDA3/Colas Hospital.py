class ColaPrioridadHospital:
    def __init__(self):
        # Lista vacía donde almacenaremos (prioridad, nombre)
        self.items = []

    def encolar(self, nombre, prioridad):
        # Agregar paciente como tupla (prioridad, nombre)
        self.items.append((prioridad, nombre))
        # Mostramos mensaje indicando qué elemento fue ingresado y su prioridad
        print(f"Ingresó: {nombre} con prioridad {prioridad}")


    def desencolar(self):
        # Atender paciente según prioridad
        if not self.esta_vacia():
            self.items.sort(key=lambda x: x[0])
            paciente_atendido = self.items.pop(0)
            print(f"Se atendió: {paciente_atendido[1]} (Prioridad {paciente_atendido[0]})")
            return paciente_atendido
        else:
            print("La cola está vacía")
            return None


    def esta_vacia(self):
        # Verificar si hay pacientes
        return len(self.items) == 0


    def tamaño(self):
        # Retornar cantidad de pacientes en espera
        return len(self.items)
    
    def mostrar_pendientes(self):
        # Mostrar lista ordenada de pacientes pendientes
        lista_ordenada = sorted(self.items)
        return lista_ordenada

#Simulacion del Hospital
hospital = ColaPrioridadHospital()

hospital.encolar("Zafiro", 3)
hospital.encolar("Tianna", 1)
hospital.encolar("Rafael", 1)
hospital.encolar("Yasin", 4)
hospital.encolar("Darío", 3)
hospital.encolar("Kayne", 2)
hospital.encolar("Evelyn", 2)
hospital.encolar("Alissa", 4)
print("\n")
print("----------------------------------------------------------------------------------------------------------------------")
print("Pacientes pendientes (Prioridad | Nombre): \n", hospital.mostrar_pendientes())
print("----------------------------------------------------------------------------------------------------------------------\n")

while not hospital.esta_vacia():
    print("\n")
    hospital.desencolar()
    print("Pacientes pendientes (Prioridad | Nombre): \n", hospital.mostrar_pendientes())
    print("\______________________________________________________________________________________________________/")
    if hospital.esta_vacia():
        print("<<<La cola está vacía>>>")
