# Importamos la clase deque desde el módulo collections, que permite crear colas de manera eficiente.
from collections import deque

# Importamos el módulo time para simular pausas entre turnos (espera del viaje).
import time

# Importamos random para generar nombres aleatorios de personas y decidir si tienen prioridad.
import random

# Creamos una cola vacía para personas que hacen fila normalmente.
cola_general = deque()

# Creamos una cola separada para personas con prioridad (niños, discapacidad, fast pass).
cola_prioritaria = deque()

# Creamos una cola separada para personas con discapacidad
cola_discapacidad = deque()

cont_G = 0
cont_P = 0
cont_D = 0

# Esta función agrega personas a la cola correspondiente.
# Recibe un nombre (string) y una bandera de prioridad (True o False).
def agregar_visitante(nombre, discapacidad = False, prioridad=False):
    if discapacidad:
        # Si la persona tiene discapacidad, se agrega a la cola discapacidad.
        cola_discapacidad.append(nombre)
    elif prioridad:
        # Si la persona tiene prioridad, se agrega a la cola prioritaria.
        cola_prioritaria.append(nombre)
    else:
        # Si no tiene prioridad, se agrega a la cola general.
        cola_general.append(nombre)

# Esta función muestra el estado actual de ambas colas.
# Convierte las colas a listas para que se muestren bien por consola.
def mostrar_colas():
    print("\nCola Discapacidad:",list(cola_discapacidad))
    print("\nCola Prioritaria:", list(cola_prioritaria))
    print("Cola General:", list(cola_general))


# Definimos la capacidad máxima del vagón de la montaña rusa: solo pueden subir 4 personas por viaje.
CAPACIDAD_VAGON = 4

# Esta función simula el proceso de llenar el vagón antes del viaje.
def cargar_vagon():
    global cont_G, cont_P, cont_D
    pasajeros = []  # Lista vacía que irá guardando los nombres de quienes suben.

    # Mientras el vagón no esté lleno...
    while len(pasajeros) < CAPACIDAD_VAGON:
        if cola_discapacidad:
            # Si hay alguien en la cola discapacidad, sube primero.
            # Usamos .popleft() para sacar a la persona del principio de la cola.
            pasajeros.append(cola_discapacidad.popleft())
            cont_D += 1
        elif cola_prioritaria:
            # Si hay alguien en la cola prioritaria, sube despues del discapacitado.
            # Usamos .popleft() para sacar a la persona del principio de la cola.
            pasajeros.append(cola_prioritaria.popleft())
            cont_P += 1
        elif cola_general:
            # Si ya no hay nadie en la prioritaria, tomamos a alguien de la cola general.
            pasajeros.append(cola_general.popleft())
            cont_G += 1
        else:
            # Si ya no hay nadie esperando, se detiene el proceso.
            break

    # Retornamos la lista de pasajeros que subieron al vagón.
    return pasajeros


# Definimos la duración del viaje en turnos. Cada viaje tarda 3 "unidades de tiempo".
DURACION_VIAJE = 3

# Esta función simula el viaje de la montaña rusa.
# Recibe la lista de pasajeros y el número del viaje actual.
def simular_viaje(pasajeros, numero_viaje):
    # Imprimimos el inicio del viaje con los nombres de los pasajeros que subieron.
    print(f"\n Viaje #{numero_viaje} con: {pasajeros}")

    # Simulamos el viaje mediante un ciclo que dura la cantidad de turnos definida.
    for t in range(DURACION_VIAJE):
        # Imprime el turno actual dentro del viaje (por ejemplo: Turno 1/3)
        print(f"  Turno {t+1}/{DURACION_VIAJE}")
        # Pausa el programa 1 segundo para simular que el viaje está en progreso.
        time.sleep(1)

    # Al finalizar todos los turnos, mostramos un mensaje celebrando el fin del viaje.
    print("¡Viaje finalizado!")


# Esta función controla la simulación completa durante varios turnos.
# Recibe como parámetro la cantidad total de turnos a ejecutar.
def iniciar_simulacion(turnos_totales):
    viaje_num = 1  # Contador de viajes realizados

    # Recorremos cada turno uno por uno
    for turno in range(turnos_totales):
        print(f"--- Turno {turno+1}/{turnos_totales} ---")

        # Se generan entre 1 y 3 nuevos visitantes de forma aleatoria
        cantidad = random.randint(1, 3)
        for _ in range(cantidad):
            # Elegimos un nombre al azar de una lista
            nombre = random.choice(["Ana", "Luis", "Carlos", "Sofía", "Mateo", "Valentina","Martinez","John","Mejia","McDaniel","Kent","Whitney","Chelsey","Kelly"])

            # 50% de probabilidad de que tenga discapacidad
            es_discapacidad = random.random() < 0.5
            
            # 50% de probabilidad de que tenga prioridad (niño, discapacidad, fast pass)
            es_prioridad = random.random() < 0.5

            # Se agrega el visitante a la cola correspondiente
            agregar_visitante(nombre, es_discapacidad, es_prioridad)

        # Mostramos el estado actual de las colas
        mostrar_colas()

        # Si hay suficientes personas para llenar un vagón, iniciamos el viaje
        if len(cola_general) + len(cola_prioritaria) + len(cola_discapacidad) >= CAPACIDAD_VAGON:
            pasajeros = cargar_vagon()         # Seleccionamos a los pasajeros
            simular_viaje(pasajeros, viaje_num)  # Simulamos el viaje
            viaje_num += 1                     # Aumentamos el contador de viajes
        else:
            # Si aún no hay suficientes personas, se espera
            print("Aún no hay suficientes personas para el viaje.")


# Llamar a la función principal
iniciar_simulacion(turnos_totales=10)
Total_atendidos = cont_G + cont_P + cont_D

print("Total de personas atendidas: ",Total_atendidos)
print("<Tipos atendidos>")
print("General: ",cont_G)
print("Prioritarios: ",cont_P)
print("Discapacitados: ",cont_D)
print("Promedios: ")
print("Promedio General: ",((cont_G*100)/Total_atendidos))
print("Promedio Prioritarios: ",((cont_P*100)/Total_atendidos))
print("Promedio Discapacitados: ",((cont_D*100)/Total_atendidos))