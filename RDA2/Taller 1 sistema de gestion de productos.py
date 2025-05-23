#Busqueda Lineal: Es un algoritmo de busqueda el cual buscara el elemento en la lista de forma secuencial hasta encontrarlo.

#Busqueda Binaria: Es un algoritmo de busqueda mas complejo el cual dividira la lista a la mitad varias veces hasta 
#encontrar el elemento buscado, este tipo de lista debe estar ordenada para poder funcionar de forma correcta.

#La busqueda lineal es efectiva para listas pequeñas y desordenadas donde se necesita un analisis rapido y simple, 
#mientras que la busqueda binaria es aplicada para listas mucho mas grandes ya que puede manejar con mayor facilidad 
#grandes cantidades de datos, ademas sus datos deben estar ordenados para poder funcionar de forma correcta.

tienda = ["Leche Entera","Limonada","Huevos","Azucar","Sal","Aceite Vegetal","Galletas","Atun","Agua",
        "Papel Higienico","Salsa de tomate","Mayonesa","Pasta Dental","Shampoo","Mantequilla","Queso","Jabon","Refresco",
        "Cereal","Cepillo de dientes"]

while True:
    print("""
        [&][&][&][&] Tiendita "Ahorros" [&][&][&][&]
        Catalogo:   
        Leche Entera     |   Salsa de tomate
        Limonada         |   Mayonesa
        Huevos           |   Pasta Dental
        Azucar           |   Shampoo
        Sal              |   Mantequilla
        Aceite Vegetal   |   Queso
        Galletas         |   Jabon
        Atun             |   Refresco
        Agua             |   Cereal
        Papel Higienico  |   Cepillo de dientes
        
        Ingrese 5 para salir del Catalogo
        """)

    buscar = input("Ingrese el nombre del producto que desea buscar: ").lower().strip()
    
    if buscar == "5":
        print('Gracias por visitar la Tiendita "Ahorros"')
        print("vuelva pronto!")
        break
    
    if buscar == "":
        print("Error!... No ha ingresado ningun producto")
        print("Intentelo nuevamente")
    
    else:
    #Busqueda Lineal
        comparacion_L = 0
        encontrar_L = False
    
        for i, producto in enumerate(tienda):
            comparacion_L += 1
            if producto.lower() == buscar:
                print(f"El producto se encontro usando BUSQUEDA LINEAL en la posicion {i}.")
                encontrar_L = True
                break
        if not encontrar_L:
            print("El producto no se ha encontrado.")

        print(f"Se realizaron {comparacion_L} comparaciones\n")

    #Busqueda Binaria
        tienda_ordenada = sorted(tienda, key=lambda x: x.lower())
        comparacion_B = 0
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

        print(f"Se realizaron {comparacion_B} comparaciones")
