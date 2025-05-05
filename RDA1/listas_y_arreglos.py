import array
#remove solo elimina un UNICO elemento repetido
# lista = [1, 5, 5, 2]
# lista.remove(5)
# print(lista)

#con un bucle for se puede eliminar todos los elementos repetidos si los elementos se repiten mas de 2 veces
lista2 = [1, 2, 2, 2, 2, 4, 5]
for i in lista2:
    lista2.remove(2)
print(lista2)

#esta parte va comentada porque sino no funca
# lista3 = [1, 2, 2, 4, 5]
# for i in lista3:
#     lista2.remove(2)
# print(lista3)

#mismo ejercicio con try y except
lista3 = [1, 2, 2, 4, 5]
for i in lista3:
    try:
        lista3.remove(2)
    except ValueError:
        pass
print(lista3)

#suma acumulada
numeros = [5, 8, 2, 9, 1]
#se inicializa la variable suma
suma = 0
for num in numeros:
    suma+= num
print("Suma total: ",suma)

#encontrar el numero mayor en una lista
numeros2 = [12, 45, 3, 22, 89, 5]
mayor = numeros2[0]
for num in numeros2:
    if num > mayor:
        mayor = num
print("El numero mayor es: ", mayor)

#generar una lista con los cuadrados de sus elementos
cuadrados = []
for i in range(1,6):
    cuadrados.append(i ** 2)
print("Lista de cuadrados: ", cuadrados)

print("//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\")
#prueba de try y except con un input / se pueden agregar mas valores a evaluar
#pero deben ir todos dentro del mismo try
# try:
#     num1 = int(input("Ingrese un numero: "))
#     print(num1)
# except ValueError:
#     print("No es un número válido")

#busqueda lineal

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i #Devuelve el indice donde se encontro
    return -1 #Devuelve este valor en caso de no encontrarlo

print(busqueda_lineal([1, 2, 3, 4, 5], 3)) #Devuelve 2

lista = [5, 3, 8, 6, 2, 7, 4, 1]
for i in range(len(lista)-1):
    for j in range(len(lista)-1-i):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[+1], lista[j]
            print(lista[j], lista[j+1], end=" ")
print(lista)