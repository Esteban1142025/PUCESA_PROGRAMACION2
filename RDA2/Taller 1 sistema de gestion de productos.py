#Busqueda Lineal: Es un algoritmo de busqueda el cual buscara el elemento en la lista de forma secuencial hasta encontrarlo
#Busqueda Binaria: Es un algoritmo de busqueda mas complejo el cual dividira la lista en mitades hasta encontrar el elemento, este tipo de lista debe estar ordenada para poder funcionar 
#La busqueda lineal es efectiva para listas pequeñas y desordenadas, mientras que la busqueda binaria es aplicada para listas mucho mas grandes en donde sus datos deben estar ordenados

tienda = ["Leche Entera","Leche Descremada","Huevos","Azucar","Sal","Aceite Vegetal","Galletas","Atun enlatado","Agua","Papel Higienico","Salsa de tomate","Mayonesa","Pasta Dental","Shampoo","Mantequilla","Queso","Jabon","Refresco","Cereal","Cepillo de dientes"]

comparacion_L = 0
encontrar_L = False

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

    buscar = input("Ingrese el nombre del producto que desea buscar: ").lower()
    
    if buscar == "5":
        break
    
    else:
        for i, producto in enumerate(tienda):
            comparacion_L += 1
        if producto.lower() == buscar:
            print(f"El producto se encontro en la posicion {i}.")
            encontrar_L = True
            break

        if not encontrar_L:
            print("El producto no se ha encontrado.")

        print(f"Comparaciones realizadas: {comparacion_L}")


