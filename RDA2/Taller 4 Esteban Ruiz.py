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



#******************************************************************************************************************************
# 🎞️ Función que anima y compara visualmente el proceso de ordenamiento de:
# - Bubble Sort (real, paso a paso)
# - sorted() (simulado, para efectos didácticos)
def animar_comparacion_sorted_bubble_simulada(lista_original, pausa=0.2):

    # Creamos una copia de la lista original para Bubble Sort
    lista_bubble = lista_original.copy()

    # Calculamos el resultado final de sorted() (lista ordenada) para simularlo paso a paso
    lista_sorted_final = sorted(lista_original)

    # Inicializamos la lista de pasos del algoritmo Bubble Sort (comenzamos con el estado original)
    pasos_bubble = [lista_bubble.copy()]

    # Lista de pasos para simular el comportamiento de sorted()
    pasos_sorted = []

    # 🔄 Generamos los pasos reales de Bubble Sort
    n = len(lista_bubble)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_bubble[j] > lista_bubble[j + 1]:
                # Intercambiamos los elementos si están fuera de orden
                lista_bubble[j], lista_bubble[j + 1] = lista_bubble[j + 1], lista_bubble[j]
                # Guardamos el estado actual después del intercambio
                pasos_bubble.append(lista_bubble.copy())

    # 🧪 Simulamos cómo se vería el progreso de sorted() paso a paso
    # Aunque sorted() es inmediato, aquí lo representamos como una transformación progresiva
    lista_simulada = lista_original.copy()
    for i in range(len(lista_sorted_final)):
        if lista_simulada[i] != lista_sorted_final[i]:
            # Sustituimos el valor por el que estaría en la lista ordenada
            lista_simulada[i] = lista_sorted_final[i]
        # Guardamos el paso simulado
        pasos_sorted.append(lista_simulada.copy())

    # Definimos el número total de pasos que tendrá la animación (el mayor entre ambos procesos)
    total_pasos = max(len(pasos_bubble), len(pasos_sorted))

    # 🖼️ Animación paso a paso
    for k in range(total_pasos):
        clear_output(wait=True)  # Limpiamos la salida anterior para crear efecto de movimiento

        # Creamos una figura con dos gráficos uno al lado del otro
        fig, axs = plt.subplots(1, 2, figsize=(12, 4))

        # 🎬 Animación de Bubble Sort (proceso real)
        if k < len(pasos_bubble):
            axs[0].bar(range(len(pasos_bubble[k])), pasos_bubble[k], color='skyblue')
            axs[0].set_title(f"Bubble Sort - Paso {k+1}")
            axs[0].set_ylim(0, max(lista_original) + 5)
        else:
            # Si se terminaron los pasos, mantenemos la vista final
            axs[0].bar(range(len(pasos_bubble[-1])), pasos_bubble[-1], color='skyblue')
            axs[0].set_title("Bubble Sort - Final")

        # 🎬 Simulación animada de sorted() (transformación progresiva)
        if k < len(pasos_sorted):
            axs[1].bar(range(len(pasos_sorted[k])), pasos_sorted[k], color='lightgreen')
            axs[1].set_title(f"sorted() - Paso {k+1}")
            axs[1].set_ylim(0, max(lista_original) + 5)
        else:
            axs[1].bar(range(len(lista_sorted_final)), lista_sorted_final, color='lightgreen')
            axs[1].set_title("sorted() - Final")

        # Acomoda ambos subgráficos para que no se encimen
        plt.tight_layout()

        # Pausa entre cada frame para que la animación sea visible
        plt.pause(pausa)

    # Muestra la última imagen estática al terminar
    plt.show()
    
animar_comparacion_sorted_bubble_simulada(notas)