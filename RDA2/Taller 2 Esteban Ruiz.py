#dollars = [1.3, 14.7, 19.8, 8.1, 18.9, 3.4, 15.6, 16.3, 9.4, 17.2]
dollars = [1.3, 3.4, 8.1, 9.4, 14.7, 15.6, 16.3, 17.2, 18.9, 19.8]

comp_bs = 0
inter_bs = 0

comp_is = 0
inter_is = 0

comp_ss = 0
inter_ss = 0

def bubble_sort(dollars):
    n = len(dollars)  # Guardamos la longitud de la lista
    global comp_bs, inter_bs
    
    # Recorremos toda la lista n veces
    for i in range(n):
        comp_bs += 1
        # En cada pasada, comparamos elementos adyacentes
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if dollars[j] > dollars[j + 1]:
                inter_bs += 1
                dollars[j], dollars[j + 1] = dollars[j + 1], dollars[j]
                # Intercambio usando desempaquetado de tuplas

    return dollars # Retornamos la lista ordenada

# Prueba
print("Original:", dollars)
print("Ordenado:", bubble_sort(dollars.copy()))
print("Numero de comparaciones realizadas: ",comp_bs)
print("Numero de intercambios realizados: ",inter_bs)
print("\n")

#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def insertion_sort(dollars):
    global comp_is, inter_is
    # Recorremos desde el segundo elemento hasta el final
    for i in range(0, len(dollars)):
        comp_is += 1
        actual = dollars[i]  # Elemento actual a insertar
        j = i - 1          # Posición anterior

        # Mientras haya elementos mayores que el actual, los movemos una posición a la derecha
        while j >= 0 and dollars[j] > actual:
            inter_is += 1
            dollars[j + 1] = dollars[j]
            j -= 1

        # Insertamos el elemento en su posición correcta
        dollars[j + 1] = actual

    return dollars  # Retornamos la lista ordenada

# Prueba
print("Original:", dollars)
print("Ordenado:", insertion_sort(dollars.copy()))
print("Numero de comparaciones realizadas: ",comp_is)
print("Numero de intercambios realizados: ",inter_is)
print("\n")

#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def selection_sort(dollars):
    n = len(dollars)
    global comp_ss, inter_ss
    
    # Recorremos todos los elementos
    for i in range(n):
        comp_ss += 1
        min_idx = i  # Suponemos que el mínimo está en la posición actual

        # Buscamos el menor elemento en el resto de la lista
        for j in range(i + 1, n):
            if dollars[j] < dollars[min_idx]:
                inter_ss += 1
                min_idx = j  # Actualizamos el índice del nuevo mínimo

        # Si encontramos un nuevo mínimo, lo intercambiamos con el actual
        if min_idx != i:
            inter_ss += 1
            dollars[i], dollars[min_idx] = dollars[min_idx], dollars[i]

    return dollars

# Prueba
print("Original:", dollars)
print("Ordenado:", selection_sort(dollars.copy()))
print("Numero de comparaciones realizadas: ",comp_ss)
print("Numero de intercambios realizados: ",inter_ss)
