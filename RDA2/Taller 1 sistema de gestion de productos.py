#Busqueda Lineal: Es un algoritmo de busqueda el cual buscara el elemento en la lista de forma secuencial hasta encontrarlo
#Busqueda Binaria: Es un algoritmo de busqueda mas complejo el cual dividira la lista en mitades hasta encontrar el elemento, este tipo de lista debe estar ordenada para poder funcionar 
#La busqueda lineal es efectiva para listas pequeñas y desordenadas, mientras que la busqueda binaria es aplicada para listas mucho mas grandes en donde sus datos deben estar ordenados

tienda = ["Leche Entera","Leche Descremada","Huevos","Azucar","Sal","Aceite Vegetal","Galletas","Atun enlatado","Agua","Papel Higienico","Salsa de tomate","Mayonesa","Pasta Dental","Shampoo","Mantequilla","Queso","Jabon","Refresco","Cereal","Cepillo de dientes"]
comparacion_L = 0
encontrar_L = False
comparacion_B = 0
while True:
    print("""
        [&][&][&][&] Tiendita "Ahorros" [&][&][&][&]
        Catalogo:   
        Leche Entera     |   Salsa de tomate
        Leche Descremada |   Mayonesa
        Huevos           |   Pasta Dental
        Azucar           |   Shampoo
        Sal              |   Mantequilla
        Aceite Vegetal   |   Queso
        Galletas         |   Jabón
        Atún enlatado    |   Refresco
        Agua             |   Cereal
        Papel Higiénico  |   Cepillo de dientes
        
        Ingrese 5 para salir del Catalogo
        """)

    buscar = input("Ingrese el nombre del producto que desea buscar: ").lower().strip()
    
    
    
    if buscar == "5":
        break
    
    else:
    #Busqueda Lineal
        for i, producto in enumerate(tienda):
            comparacion_L += 1
            if producto.lower() == buscar:
                print(f"El producto se encontro usando BUSQUEDA LINEAL en la posicion {i}.")
                encontrar_L = True

        if not encontrar_L:
            print("El producto no se ha encontrado.")

        print(f"Se realizaron {comparacion_L} comparaciones")

    #Busqueda Binaria
        tienda_ordenada = sorted(tienda, key=lambda x: x.lower())
        
        inicio = 0
        fin = len(tienda_ordenada) - 1
        encontrar_B = False

        while inicio <= fin:
            comparacion_B += 1
            medio = (inicio + fin) // 2
            producto_medio = tienda_ordenada[medio].lower()
            
            if producto_medio == buscar:
                print(f"El producto se encontro usando BUSQUEDA BINARIA en la posicion: {medio}")
                encontrar_B = True
                break
            elif buscar < producto_medio:
                fin = medio - 1
            else:
                inicio = medio + 1

        if not encontrar_B:
            print("El producto no se ha encontrado.")

        print(f"Se realizaron {comparacion_L} comparaciones")
