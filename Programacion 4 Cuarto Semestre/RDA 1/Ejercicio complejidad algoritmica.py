# #Ejercicio 1
# def es_primero_par(numeros):
#     if not numeros:
#         return "Lista Vacia"
#     primer_numero = numeros[0] # Acceso directo
    
#     if primer_numero % 2 == 0:
#         return "El primero numero es Par"
#     else:
#         return "El primer numero es Impar"

# # --- Pruebas ---
# lista_corta = [10, 2, 5, 8]
# lista_larga = list(range(1, 1000001)) # Lista de 1 millon de numeros

# print(es_primero_par(lista_corta))
# print(es_primero_par(lista_larga))

# # Ejercicio 2
def encontrar_aguja(pajar,aguja):
    for elemento in pajar:
        if elemento == aguja:
            return True # !La encontramos!
    return False # No estaba en la lista

# --- Pruebas ---
mi_lista = [15, 23, 4, 88, 9, 42, 101]
print(f"¿Está el 42?{encontrar_aguja(mi_lista, 42)}")
print(f"¿Está el 99?{encontrar_aguja(mi_lista, 99)}")

# #Ejercicio 3
# def generar_pares(nombres):
#     for nombre1 in nombres:
#         for nombre2 in nombres:
#             if nombre1 != nombre2:
#                 print(f"{nombre1} = {nombre2}")

# # --- Pruebas ---
# equipo = ["Ana","Luis","Juan","Sara"]
# generar_pares(equipo)

# #Ejercicio 4
import time
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# --- Pruebas (!!!CUIDADO!!!) ---
# Prueba con un numero pequeño
start_time = time.time()
fib_30 = fibonacci_recursivo(30)
end_time = time.time()
print(f"Fibonacci(30) = {fib_30}. Tiempo: {end_time - start_time:.4f}segundos.")

# #Intenta con un numero un poco mas grande
# start_time = time.time()
# fib_35 = fibonacci_recursivo(35)
# end_time = time.time()
# print(f"Fibonacci(30) = {fib_35}. Tiempo: {end_time - start_time:.4f}segundos.")
