# 1. ¿Por qué es necesario ordenar antes de realizar la búsqueda binaria?
# Porque en caso de no ordenar la lista, no es posible saber si el valor buscado está en la 
# mitad izquierda o derecha, lo que hace inservible el algoritmo.
#
# 2. ¿Qué pasaría si usamos búsqueda binaria sin ordenar primero?
# Si se aplica búsqueda binaria en una lista desordenada, el resultado será incorrecto o nulo. 
#
# 3. ¿Qué ventajas viste entre la búsqueda binaria y la búsqueda lineal?
# Busqueda binaria: Mucho más rápida para listas grandes
# Busqueda lineal: Recorre todos los elementos uno por uno
# 4. ¿Cuál de los dos ordenamientos te pareció más intuitivo de implementar y por qué?
# El ordenamiento lineal me parecio mas snecillo de implementar ya que no requiero de ordenar la lista
# para poder trabajar con ella

clientes = [
("Jorja",23.1),
("Federico",46.2),
("Rey",53.3),
("Potts",34.4),
("Farhan",56.5),
("Espinoza",26.6),
("Jean",76.7),
("Archie",67.8),
("Donovan",75.9),
("Mateo",92.1)]

print("Base de datos:")
for i in clientes:
    print(i,"\n")

def ordenar_nombres(lista):

    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j][0].lower() > actual[0].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

def ordenar_saldo(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j][1] < lista[min_idx][1]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def busqueda_nombre(lista_ordenada, objetivo):
    inicio = 0
    fin = len(lista_ordenada) - 1
    comp = 0

    while inicio <= fin:
        comp += 1
        medio = (inicio + fin) // 2
        nombre = lista_ordenada[medio][0].lower()

        if nombre == objetivo.lower():
            return medio, comp
        elif objetivo.lower() < nombre:
            fin = medio - 1
        else:
            inicio = medio + 1

    return -1, comp

def busqueda_lineal(lista_desorden, objetivo):
    for i in range(len(lista_desorden)):
        if lista_desorden[i][0].lower() == objetivo.lower():
            return i
    return -1

while True:
    print("""
        */\/\/\/\/\/\/\/\ Gestion de Clientes /\/\/\/\/\/\/\/\*
        Seleccione una de las siguientes opciones:
        
        1. Mostrar lista ordenada por nombre
        2. Mostrar lista ordenada por saldo
        3. Busqueda de clientes
        4. Ingresar un nuevo cliente
        5. Salir del programa
        """)
    
    opcion = input("Ingrese una opcion: ").strip()
    if opcion == "" or opcion not in ["1", "2", "3", "4", "5"]:
        print("Error!... No ha ingresado ninguna opcion o la opcion es incorrecta")
        print("Intentelo nuevamente")
    
    if opcion != "5":
        if opcion == "1":
            print("Lista de clientes ordenada por nombre:")
            base_ordenada_N = ordenar_nombres(clientes.copy())
            for i in base_ordenada_N:
                print(i)
                
        elif opcion == "2":
            print("Lista de clientes ordenada por saldo:")
            base_ordenada_S = ordenar_saldo(clientes.copy())
            for i in base_ordenada_S:
                print(i)
                
        elif opcion == "3":
            busqueda = input("Desea hacer la busqueda lineal (L) o binaria (B)?: ").lower().strip()
            if busqueda == "B".lower():
                base_ordenada_N = ordenar_nombres(clientes.copy())
                nombre = input("Ingrese el nombre del cliente a buscar: ").strip()
                pos, comp = busqueda_nombre(base_ordenada_N, nombre)
                if pos != -1:
                    print(f"El cliente fue encontrado: {base_ordenada_N[pos]} en la posición {pos}")
                else:
                    print("No se pudo encontrar al cliente")

                print(f"Se realizaron {comp} comparaciones")
            elif busqueda == "L".lower():
                nombre = input("Ingrese el nombre del cliente a buscar: ").strip()
                nombre_encontrado = busqueda_lineal(clientes, nombre)

                if nombre_encontrado != -1:
                    print(f"El cliente {nombre} se encuentra en la posicion: {nombre_encontrado}")
                else:
                    print("No se pudo encontrar al cliente")

        elif opcion == "4":
            print("<<<Agregando un nuevo cliente>>>")
            cliente = input("Ingrese el nombre del nuevo cliente: ").strip()
            saldo = float(input("Ingrese el saldo del nuevo cliente: "))
            clientes.append((cliente,saldo))
            print("Cliente agregado con exito!")
            for i in clientes:
                print(i)
    else:
        print("Gracias por usar el programa")
        print("Adios!")
        break
