print("*******************************************************************************")
print("Nombre: Dilón Lagua")
print("Fecha: 19/05/2025")
print("RDA 2")
print("*******************************************************************************")
 #Explicación conceptual (teórica)

 # ¿Qué es la búsqueda lineal? ¿Cómo funciona?
#La busqueda lineal es un algoritmo diciendo asi simple que recorre una lista creada con elementos  y recorre elemento por elemento hasta el valor
#buscado o llegar al final, todo comienza desde el primer elemento y compara uno por uno con el objetivo de encontrarlo y si lo encuentra lo devuelve
#a la posición y si no se encuentra nos indicara que no se encontro. Y de esta busqueda no se necesita ser ordena puede ser desordenada.

# ¿Qué es la búsqueda binaria? ¿Qué condición especial debe cumplir la lista?
#La busqueda binaria es un algoritmo que busca de ingual forma un valor dividiendo repetidamente una lista ordena partiendole a ala mitad, compara el valor
#buscado con el del medio si es igual lo encontro, pero si es menor va a buscar en la mitad izquierda, pero si es menor estara en la derecha.

# ¿En qué casos conviene usar cada una?
#La busqueda lienal se usa  cuando la lista es corta o desordenada o cuando se puede ordenar facilmente.
#la busqueda binaria se usa cuando la lista ordenada y se nesecita una busqueda en una lista grande.

print("*******************************************************************************")
productos = [
    "Laptop", "Teclado", "Mouse", "Monitor", "Impresora", "Tablet", "Celular",
    "Cargador", "Auriculares", "Camara", "Proyector", "Microfono", "Altavoz",
    "Smartwatch", "Router", "Disco duro", "Memoria USB", "Bateria externa",
    "Webcam", "Tarjeta grafica"
]

busquedas = []

def buscar_lineal(lista, nombre):
    comp = 0
    for i in range(len(lista)):
        comp += 1
        if lista[i].lower() == nombre:
            return True, i, comp
    return False, -1, comp

def buscar_binaria(lista, nombre):
    lista = sorted(lista, key=str.lower)
    ini = 0
    fin = len(lista) - 1
    comp = 0

    while ini <= fin:
        comp += 1
        medio = (ini + fin) // 2
        if lista[medio].lower() == nombre:
            return True, medio, comp
        elif nombre < lista[medio].lower():
            fin = medio - 1
        else:
            ini = medio + 1
    return False, -1, comp

while True:
    buscar = input("Escribe el producto que quieres buscar (o 'salir' para terminar): ").strip().lower()

    if buscar == "salir":
        break

    if buscar == "":
        print("No escribiste nada. Intenta otra vez.")
        continue

    l_encontrado, l_pos, l_comp = buscar_lineal(productos, buscar)
    b_encontrado, b_pos, b_comp = buscar_binaria(productos, buscar)

    if l_encontrado:
        print(f"[Lineal] Producto encontrado en la posicion {l_pos}. Comparaciones: {l_comp}")
    else:
        print(f"[Lineal] Producto no encontrado. Comparaciones: {l_comp}")

    if b_encontrado:
        print(f"[Binaria] Producto encontrado en la lista ordenada en la posicion {b_pos}. Comparaciones: {b_comp}")
    else:
        print(f"[Binaria] Producto no encontrado. Comparaciones: {b_comp}")

    busquedas.append((buscar, l_encontrado, l_pos, l_comp, b_encontrado, b_pos, b_comp))

print("\nResumen de busquedas:")
for i, b in enumerate(busquedas):
    print(f"{i+1}. Producto: {b[0]}")
    print(f"   Lineal - Encontrado: {b[1]}, Posicion: {b[2]}, Comparaciones: {b[3]}")
    print(f"   Binaria - Encontrado: {b[4]}, Posicion: {b[5]}, Comparaciones: {b[6]}")
