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
turnos_totales=10
viaje_num = 1
nombres = ["Ana", "Luis", "Carlos", "Sofía", "Mateo", "Valentina","Martinez","John","Mejia","McDaniel","Kent","Whitney","Chelsey","Kelly"]

# Bucle infinito que solo se rompe si el usuario ingresa un valor válido
while True:
    try:
        # Solicita al usuario la duración de cada turno y lo convierte a número decimal
        tiempo_espera = float(input("Ingrese la duración de cada turno: "))
        
        # Verifica si el número ingresado es mayor a 0
        if tiempo_espera <= 0:
            print("Ingrese un numero mayor a 0.") # Mensaje si el número no es válido
        else:
            break # Sale del bucle si el valor es correcto
    except ValueError:
        # Captura el error si el usuario ingresa algo que no se puede convertir a float
        print("Error... Por favor ingrese un numero positivo")


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
def mostrar_colas(turno):
    print(f"\n--- Turno {turno}/{turnos_totales} ---")
    print("\nCola Discapacidad:",list(cola_discapacidad))
    print("\nCola Prioritaria:", list(cola_prioritaria))
    print("Cola General:", list(cola_general))

def agregar_aleatorios():
    cantidad = random.randint(1, 3)
    for _ in range(cantidad):
        nombre = random.choice(nombres)
        es_discapacidad = random.random() < 0.5
        es_prioridad = not es_discapacidad and random.random() < 0.5
        agregar_visitante(nombre, prioridad=es_prioridad, discapacidad=es_discapacidad)
    print(f"{cantidad} personas fueron añadidas al carro de forma aleatoria.")

# Definimos la capacidad máxima del vagón de la montaña rusa: solo pueden subir 4 personas por viaje.
CAPACIDAD_VAGON = 4

# Esta función simula el proceso de llenar el vagón antes del viaje.
def cargar_vagon(viaje_num):
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
        time.sleep(tiempo_espera)

    # Al finalizar todos los turnos, mostramos un mensaje celebrando el fin del viaje.
    print("¡Viaje finalizado!")

# Bucle principal que muestra el panel de control y recibe la opción del usuario
while True:
    print("""
        <<<<Panel de control del parque K BOOM>>>>
        1. Agregar nuevo pasajero
        2. Ver estado de las colas
        3. Simular turnos
        4. Salir del sistema
        """)

    # Solicita al usuario una opción del menú
    opcion = int(input("Ingrese su opción: "))

    # Valida si la opción es válida
    if opcion not in [1,2,3,4]:
        print("Error! Seleccione una opcion valida...")

    # Opción 1: Agregar pasajero
    elif opcion == 1:
        nombre = input("Ingrese el nombre del pasajero: ")
        tipo = input("Ingrese el tipo de cola al que pertenece, General(G), Prioritaria(P) o Discapacidad(D): ").lower()
        
        # Agrega al pasajero a la cola correspondiente
        if tipo == "g":
            print(f"El pasajero {nombre} fue agregado a la cola general.")
            agregar_visitante(nombre)
        elif tipo == "p":
            print(f"El pasajero {nombre} fue agregado a la cola prioritaria.")
            agregar_visitante(nombre, prioridad=True)
        elif tipo == "d":
            print(f"El pasajero {nombre} fue agregado a la cola discapacidad.")
            agregar_visitante(nombre, discapacidad=True)

    # Opción 2: Ver estado de las colas
    elif opcion == 2:
        mostrar_colas(0)

    # Opción 3: Simular turnos del parque
    elif opcion == 3:
        for turno in range(1, turnos_totales + 1):
            mostrar_colas(turno)  # Muestra el estado de las colas en cada turno
            
            # Si hay suficientes personas, se simula el viaje
            if len(cola_general) + len(cola_prioritaria) + len(cola_discapacidad) >= CAPACIDAD_VAGON:
                pasajeros = cargar_vagon(viaje_num)
                simular_viaje(pasajeros, viaje_num)
                viaje_num += 1
            else:
                print("Aun no hay suficientes personas para el viaje.")
            
            agregar_aleatorios()  # Se agregan pasajeros aleatorios a las colas
            time.sleep(tiempo_espera)  # Espera para simular el paso del tiempo

        print("Simulacion de turnos finalizada.")
        
        # Reporte final de estadísticas de pasajeros
        Total_atendidos = cont_G + cont_P + cont_D
        print("Total de personas atendidas: ",Total_atendidos)
        print("<Tipos atendidos>")
        print("General: ",cont_G)
        print("Prioritarios: ",cont_P)
        print("Discapacitados: ",cont_D)
        print("Promedios: ")
        print("Promedio General: ","%",((cont_G*100)/Total_atendidos))
        print("Promedio Prioritarios: ","%",((cont_P*100)/Total_atendidos))
        print("Promedio Discapacitados: ","%",((cont_D*100)/Total_atendidos))

    # Opción 4: Salir del sistema
    elif opcion == 4:
        print("\nGracias por usar el sistema del parque K BOOM.!")
        break  # Sale del bucle principal y termina el programa