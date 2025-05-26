#Explicacion de algoritmos:
#Bubble sort: Realiza comparaciones entre elementos y los ordena intercambiando sus posiciones repetidamente
#hasta que la lista quede ordenada
#Insertion sort: Crea la lista ordenanda tomando elemento por elemento e insertandolo en la posicion correcta dentro de los
#elementos ya ordenados
#Selection sort: Busca el elemento mas pequeño e intercambia su posicion con el elemento que ocupa la primera
#posicion de la lista en ese momento, luego va recorriendo la lista para encontrar el siguiente elemento mas pequeño y lo
#intercambia con la siguiente posicion.
#Metodo mas eficiente: La mejor opcion es selection sort
#Explicacion: es que mejor rendimiento presenta a comparacion de los otros 2 ya que realiza intercambio de posiciones buscando
#el valor minimo cada vez que recorre la lista


dollars = [1.3, 14.7, 19.8, 8.1, 18.9, 3.4, 15.6, 16.3, 9.4, 17.2]

comp_bs = 0
inter_bs = 0

comp_is = 0
inter_is = 0

comp_ss = 0
inter_ss = 0

def bubble_sort(dollars):
    n = len(dollars)
    global comp_bs, inter_bs

    for i in range(n):
        comp_bs += 1
        for j in range(0, n - i - 1):
            if dollars[j] > dollars[j + 1]:
                inter_bs += 1
                dollars[j], dollars[j + 1] = dollars[j + 1], dollars[j]
    return dollars

print("Original:", dollars)
print("Ordenado:", bubble_sort(dollars.copy()))
print("Numero de comparaciones realizadas: ",comp_bs)
print("Numero de intercambios realizados: ",inter_bs)
print("\n")

#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def insertion_sort(dollars):
    global comp_is, inter_is

    for i in range(0, len(dollars)):
        comp_is += 1
        actual = dollars[i]
        j = i - 1
        while j >= 0 and dollars[j] > actual:
            inter_is += 1
            dollars[j + 1] = dollars[j]
            j -= 1
        dollars[j + 1] = actual
    return dollars

print("Original:", dollars)
print("Ordenado:", insertion_sort(dollars.copy()))
print("Numero de comparaciones realizadas: ",comp_is)
print("Numero de intercambios realizados: ",inter_is)
print("\n")

#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def selection_sort(dollars):
    n = len(dollars)
    global comp_ss, inter_ss
    
    for i in range(n):
        comp_ss += 1
        minimo = i
        for j in range(i + 1, n):
            if dollars[j] < dollars[minimo]:
                inter_ss += 1
                minimo = j 
        if minimo != i:
            inter_ss += 1
            dollars[i], dollars[minimo] = dollars[minimo], dollars[i]

    return dollars

print("Original:", dollars)
print("Ordenado:", selection_sort(dollars.copy()))
print("Numero de comparaciones realizadas: ",comp_ss)
print("Numero de intercambios realizados: ",inter_ss)
