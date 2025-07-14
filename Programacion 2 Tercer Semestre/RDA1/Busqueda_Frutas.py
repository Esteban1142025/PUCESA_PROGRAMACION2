#Actividad Practica 1
#Busqueda de Frutas usando busqueda lineal

#Lista con nombres de frutas disponibles
frutas = ["manzana", "platano", "naranja", "pera", "uva", "sandia", "melon", "piña", "fresa", "cereza"]

#Bucle while "infinito" que permite al usuario realizar múltiples búsquedas hasta que decida salir
while True:
    comparaciones = 0 #Contador para saber cuántas comparaciones se realizan
    print("""
        Lista de frutas disponibles:
        - manzana
        - platano
        - naranja
        - pera
        - uva
        - sandia
        - melon
        - piña
        - fresa
        - cereza
        
        Ingrese 5 para salir del programa
        """)
    
    #Se pide al usuario que escriba el nombre de una fruta
    buscar = input("Ingrese el nombre de la fruta que desea buscar: ").lower()
    
    #Si el usuario ingresa "5", se termina el programa
    if buscar == "5":
        break
    
    #Si la fruta está en la lista recorrera dicha lista comparando sus elementos uno por uno
    elif buscar in frutas:
        for i in range(len(frutas)):
            comparaciones += 1
            if frutas[i] == buscar:
                print(f"La fruta {buscar} se encuentra en la lista y esta en posición {i+1}")
                print(f"Se realizo {comparaciones} comparaciones para llegar al resultado")
    
    #Si la fruta no está en la lista se mostrara un mensaje de error
    else:
        print("El termino ingresado no se encuentra en la lista, intentelo nuevamente")
