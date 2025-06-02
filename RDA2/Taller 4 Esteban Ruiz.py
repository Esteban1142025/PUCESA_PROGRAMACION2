import random
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time


notas = random.sample(range(0, 21), 15)
print("<<<Notas originales>>>", notas)

# Definimos la función bubble_sort_viz, que implementa Bubble Sort con estadísticas y opción de visualización
# Parámetros:
# - lista: la lista de números a ordenar
# - mostrar_pasos (bool): si es True, se guardarán los estados intermedios para animación
# - pausa (float): tiempo en segundos entre pasos, útil si se usa para animar (aunque aquí no se usa directamente)
def bubble_sort_viz(lista, mostrar_pasos=False):

    # Creamos una copia de la lista para no modificar la original
    lista = lista.copy()

    # Inicializamos contadores para registrar la cantidad de comparaciones e intercambios
    comparaciones = 0
    intercambios = 0

    # Guardamos la longitud de la lista
    n = len(lista)

    # Lista donde se almacenarán los pasos intermedios (solo si mostrar_pasos=True)
    pasos = []

    # Bucle externo que recorre toda la lista
    for i in range(n):
        # Bucle interno que compara elementos adyacentes
        for j in range(0, n - i - 1):
            # Cada vez que se comparan dos elementos, se incrementa el contador de comparaciones
            comparaciones += 1

            # Si el elemento actual es mayor que el siguiente, se deben intercambiar
            if lista[j] > lista[j + 1]:
                # Intercambio de los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

                # Incrementamos el contador de intercambios
                intercambios += 1

                # Si mostrar_pasos es True, guardamos el estado actual de la lista (después del intercambio)
                pasos.append(lista.copy())

    # Al finalizar, retornamos:
    # - La lista ordenada
    # - El número total de comparaciones
    # - El número total de intercambios
    # - La lista de pasos intermedios (puede estar vacía si mostrar_pasos=False)
    return lista, comparaciones, intercambios, pasos


# 🎥 Función para animar Bubble Sort paso a paso
def animar_bubble_sort(pasos):
    # Recorremos cada estado intermedio guardado del algoritmo
    for estado in pasos:
        # Limpiamos la salida anterior de la celda para simular una animación continua
        clear_output(wait=True)

        # Dibujamos una gráfica de barras representando el estado actual de la lista
        plt.bar(range(len(estado)), estado, color='green')

        # Agregamos título y etiquetas a la gráfica
        plt.title("Animación Bubble Sort")
        plt.xlabel("Índice")  # Eje X representa las posiciones de la lista
        plt.ylabel("Valor")   # Eje Y representa el valor de cada elemento

        # Pausamos por 0.3 segundos antes de pasar al siguiente paso para que se vea el movimiento
        plt.pause(0.1)

    # Al finalizar, mostramos la última imagen sin limpiar
    plt.show()

# Ejecutamos bubble_sort_viz con mostrar_pasos=True para capturar cada paso intermedio
_, _, _, pasos_animacion = bubble_sort_viz(notas, mostrar_pasos=True)

# Llamamos a la función de animación con los pasos registrados
animar_bubble_sort(pasos_animacion)

