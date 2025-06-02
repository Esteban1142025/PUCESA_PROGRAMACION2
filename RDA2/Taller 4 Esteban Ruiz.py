#*****************************************************************************************************************************
#CONCLUSION PERSONAL#
#*****************************************************************************************************************************
# ¿Qué método te pareció más eficiente o claro para ordenar?
#El mas eficiente de ambos es sin duda alguna sorted() ya que es una función que ordena los valores de manera automatica 
#de forma casi instantanea sin modificar la lista original, mientras que bubble sort es mas facil de comprender ya que podemos
#visualizar el proceso de ordenamiento paso a paso, pero es mucho mas lento que sorted()

# ¿Crees que es útil visualizar el proceso de ordenamiento?
#Si, ya que de esa manera el programador puede observar el proceso de ordenamiento paso a paso y entender mejor
#su funcionamiento y poder corregir errores o cambiar los parametros de ordenamiento si lo desea

import random
import matplotlib.pyplot as plt
from IPython.display import clear_output
import bisect

notas = random.sample(range(0, 21), 15)
print("<<<Notas originales>>>", notas)

nueva_nota = int(input("Ingrese una nueva nota: "))
bisect.insort(notas, nueva_nota)
print("<<<Lista después de insertar la nueva nota>>>", notas)

nota_buscar = int(input("Ingrese la nota a buscar: "))
posicion = bisect.bisect_left(notas, nota_buscar)
if posicion < len(notas) and notas[posicion] == nota_buscar:
    print(f"La nota solicitada: {nota_buscar}, se encuentra en la posición {posicion}")
else:
    print(f"La nota solicitada: {nota_buscar}, no está en la lista.")

def bubble_sort_viz(lista, mostrar_pasos=False):

    lista = lista.copy()
    comparaciones = 0
    intercambios = 0
    n = len(lista)

    pasos = []

    for i in range(n):

        for j in range(0, n - i - 1):
            comparaciones += 1
            
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
                pasos.append(lista.copy())
    return lista, comparaciones, intercambios, pasos


def animar_bubble_sort(pasos):
    for estado in pasos:
        clear_output(wait=True)

        plt.bar(range(len(estado)), estado, color='green')

        plt.title("Animación Bubble Sort")
        plt.xlabel("Índice")
        plt.ylabel("Valor")
        plt.pause(0.1)

    plt.show()

_, _, _, pasos_animacion = bubble_sort_viz(notas, mostrar_pasos=True)

animar_bubble_sort(pasos_animacion)



#******************************************************************************************************************************
def animar_comparacion_sorted_bubble_simulada(lista_original, pausa=0.2):
    lista_bubble = lista_original.copy()
    lista_sorted_final = sorted(lista_original)
    pasos_bubble = [lista_bubble.copy()]
    pasos_sorted = []

    n = len(lista_bubble)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_bubble[j] > lista_bubble[j + 1]:
                lista_bubble[j], lista_bubble[j + 1] = lista_bubble[j + 1], lista_bubble[j]
                pasos_bubble.append(lista_bubble.copy())


    lista_simulada = lista_original.copy()
    for i in range(len(lista_sorted_final)):
        if lista_simulada[i] != lista_sorted_final[i]:
            lista_simulada[i] = lista_sorted_final[i]

        pasos_sorted.append(lista_simulada.copy())

    total_pasos = max(len(pasos_bubble), len(pasos_sorted))

    for k in range(total_pasos):
        clear_output(wait=True)

        fig, axs = plt.subplots(1, 2, figsize=(12, 4))
        if k < len(pasos_bubble):
            axs[0].bar(range(len(pasos_bubble[k])), pasos_bubble[k], color='skyblue')
            axs[0].set_title(f"Bubble Sort - Paso {k+1}")
            axs[0].set_ylim(0, max(lista_original) + 5)
        else:
            axs[0].bar(range(len(pasos_bubble[-1])), pasos_bubble[-1], color='skyblue')
            axs[0].set_title("Bubble Sort - Final")

        if k < len(pasos_sorted):
            axs[1].bar(range(len(pasos_sorted[k])), pasos_sorted[k], color='lightgreen')
            axs[1].set_title(f"sorted() - Paso {k+1}")
            axs[1].set_ylim(0, max(lista_original) + 5)
        else:
            axs[1].bar(range(len(lista_sorted_final)), lista_sorted_final, color='lightgreen')
            axs[1].set_title("sorted() - Final")

        plt.tight_layout()
        plt.pause(pausa)
    plt.show()
    
animar_comparacion_sorted_bubble_simulada(notas)
