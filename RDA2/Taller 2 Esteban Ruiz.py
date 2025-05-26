dollars = [1.3, 14.7, 19.8, 8.1, 18.9, 3.4, 15.6, 16.3, 9.4, 17.2]

comp = 0
inter = 0

def bubble_sort(dollars):
    n = len(dollars)  # Guardamos la longitud de la lista
    global comp, inter
    # Recorremos toda la lista n veces
    for i in range(n):
        comp += 1
        # En cada pasada, comparamos elementos adyacentes
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if dollars[j] > dollars[j + 1]:
                inter += 1
                dollars[j], dollars[j + 1] = dollars[j + 1], dollars[j]
                # Intercambio usando desempaquetado de tuplas

    return dollars, comp, inter  # Retornamos la lista ordenada

# Prueba
print("Original:", dollars)
print("Ordenado:", bubble_sort(dollars.copy()))
print("Numero de comparaciones realizadas: ",comp)
print("Numero de intercambios realizados: ",inter)
print("\n")

#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def insertion_sort(dollars):
    # Recorremos desde el segundo elemento hasta el final
    for i in range(1, len(dollars)):
        actual = dollars[i]  # Elemento actual a insertar
        j = i - 1          # Posición anterior

        # Mientras haya elementos mayores que el actual, los movemos una posición a la derecha
        while j >= 0 and dollars[j] > actual:
            dollars[j + 1] = dollars[j]
            j -= 1

        # Insertamos el elemento en su posición correcta
        dollars[j + 1] = actual

    return dollars  # Retornamos la lista ordenada

# Prueba
print("Original:", dollars)
print("Ordenado:", insertion_sort(dollars.copy()))
print("\n")

#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def selection_sort(dollars):
    n = len(dollars)

    # Recorremos todos los elementos
    for i in range(n):
        min_idx = i  # Suponemos que el mínimo está en la posición actual

        # Buscamos el menor elemento en el resto de la lista
        for j in range(i + 1, n):
            if dollars[j] < dollars[min_idx]:
                min_idx = j  # Actualizamos el índice del nuevo mínimo

        # Si encontramos un nuevo mínimo, lo intercambiamos con el actual
        if min_idx != i:
            dollars[i], dollars[min_idx] = dollars[min_idx], dollars[i]

    return dollars

# Prueba
print("Original:", dollars)
print("Ordenado:", selection_sort(dollars.copy()))
