#Actividad Practica 2
#Busqueda de Numeros usando busqueda binaria


def busqueda_numeros(lista,objetivo):
    inicio = 0              #posicion inicial de la busqueda
    fin = len(lista) - 1    #posicion final de la busqueda
    cont = 0                #contador de las divisiones de la lista

    #Bucle que se ejecuta mientras exista un rango válido en la búsqueda
    while inicio <= fin:
        cont += 1                       #se cuenta cada division de la lista
        medio = (inicio + fin) // 2     #se calcula la posicion de la mitad de la lista
        if lista[medio] == objetivo:
            return medio, cont          #retorna posicion y el numero de divisiones
        elif lista[medio] < objetivo:
            inicio = medio + 1          #Si es numero es mayor empezara a buscar hacia la derecha
        else:
            fin = medio - 1             #Si el numero es menor empezara a buscar hacia la izquierda
    return -1, cont                     #Si no se encuentra retorna -1 y la cantidad de divisiones hechas

#Lista de números ordenados
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#Bucle while "infinito" que permite al usuario realizar múltiples búsquedas hasta que decida salir
while True:

    print("""
        Numeros enlistados:
        
        [10]    [20]    [30]    [40]    [50]
        
        [60]    [70]    [80]    [90]    [100]
        
        Ingrese 5 para salir del programa
        """)
    
    #Se pide al usuario que escriba un numero para empezar la busqueda
    busqueda_usuario = int(input("Ingrese el numero que desea buscar: "))
    
    #Se invoca a la funcion y se realiza la busqueda binaria
    posicion, cont = busqueda_numeros(numeros, busqueda_usuario)
    
    #Si el usuario ingresa el numero 5 el programa termina
    if busqueda_usuario == 5:
        break
    
    #Si el número fue encontrado muestra su posición y las divisiones realizadas
    elif posicion != -1:
        print(f"El numero {busqueda_usuario} existe en la lista y se encuentra en la posicion {posicion}.")
        print(f"Se realizaron {cont} divisiones para encontrar el numero.")
    
    #Si el valor ingresado no está en la lista se mostrara un mensaje de error
    else:
        print("El termino ingresado no se encuentra en la lista.")
