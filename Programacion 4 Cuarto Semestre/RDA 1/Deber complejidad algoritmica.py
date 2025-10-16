print("""
#############################
#      Programacion IV      #
#       Esteban Ruiz        #
#      Cuarto Semestre      #
#         15/10/2025        #
#############################
""")

print("Ejercicio 1: Sumador Selectivo")
print("Misión: Crea una función que reciba una lista de números y devuelva la suma de todos los números impares de la lista.")

def sumar_impares(numeros):
    suma = 0
    for n in numeros:
        if n % 2 != 0:
            suma += n
    return suma

# --- Prueba tu función ---
mi_lista = [2, 5, 8, 11, 14, 17, 20]
# El resultado debería ser 5 + 11 + 17 = 33
print("La suma de los numeros impares es: ",sumar_impares(mi_lista))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("\n")

print("Ejercicio 2: El Inversor de Listas")
print("""Misión: Escribe una función que tome una lista y devuelva `True` si la lista es un  
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda), y `False` en caso contrario.""")
def es_palindromo(lista):
    if lista == lista[::-1]:
        return True
    else:
        return False

# --- Prueba tu función ---
lista1 = [1, 2, 3, 2, 1] # Debería devolver True
lista2 = ["a", "n", "a"] # Debería devolver True
lista3 = [1, 2, 3, 4, 5] # Debería devolver False
print(es_palindromo(lista1))
print(es_palindromo(lista2))
print(es_palindromo(lista3))

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("\n")

print("Ejercicio 3: ¿Existen Duplicados?")

print("""Misión: Crea una función que reciba una lista y devuelva `True` si 
contiene al menos un elemento duplicado. Si todos los elementos son únicos, debe devolver `False`.""")
def hay_duplicados(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

# --- Prueba tu función ---
con_duplicados = [1, 2, 5, 2, 8] # Debería devolver True
sin_duplicados = ["gato", "perro", "pez"] # Debería devolver False
print(hay_duplicados(con_duplicados))
print(hay_duplicados(sin_duplicados))

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

