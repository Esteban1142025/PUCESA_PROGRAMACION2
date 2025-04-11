# a = 5
# b = 0

# if b == 0:
#     print("Error: Division por cero")
# else:
#     print(a/b)
# #------------------------------------------
# if b != 0:
#     print(a/b)
# else:
#     print("Error: Division por cero")
# #------------------------------------------
# if b == 0: print("Error: Division por cero")
# else: print(a/b)

#------------------------------------------
#Meu de opciones
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#------------------------------------------
#5. select opciones
#6. Ingresar por teclado 2 números verifique el tipo de dato
#7. validar que el segundo numero no sea cero
#8. realizar la operación seleccionada
#9. mostrar el resultado
#10. validar que la opcion seleccionada sea correcta
#11. mostrar mensaje de error si la opcion seleccionada no es correcta

print("""
MENU:
1. Suma
2. Resta
3. Multiplicación
4. División
""")
seleccion = int(input("Seleccione alguna de las operaciones indicadas -> "))
if seleccion < 1 or seleccion > 4:
    print("Error: Seleccione una opcion valida...")
else:
    if seleccion == 1:
        print("Ha seleccionado la opcion SUMA, es correcto? (S/N)")
        validacion = input("")
        if validacion.upper() == "S":
            a = float(input("Ingrese el primer numero -> "))
            b = float(input("Ingrese el segundo numero -> "))
            print("El resultado de la suma es: ", a + b)
        else:
            print("Error: La opcion seleccionada no es correcta...")
    elif seleccion == 2:
        print("Ha seleccionado la opcion RESTA, es correcto? (S/N)")
        validacion = input("")
        if validacion.upper() == "S":
            a = float(input("Ingrese el primer numero -> "))
            b = float(input("Ingrese el segundo numero -> "))
            print("El resultado de la resta es: ", a - b)
        else:
            print("Error: La opcion seleccionada no es correcta...")
    elif seleccion == 3:
        print("Ha seleccionado la opcion MULTIPLICACIÓN, es correcto? (S/N)")
        validacion = input("")
        if validacion.upper() == "S":
            a = float(input("Ingrese el primer numero -> "))
            b = float(input("Ingrese el segundo numero -> "))
            print("El resultado de la multiplicacion es: ", a * b)
        else:
            print("Error: La opcion seleccionada no es correcta...")
    elif seleccion == 4:
        print("Ha seleccionado la opcion DIVISIÓN, es correcto? (S/N)")
        validacion = input("")
        if validacion.upper() == "S":
            a = float(input("Ingrese el primer numero -> "))
            b = float(input("Ingrese el segundo numero -> "))
            if b == 0:
                print("Error: Division por cero")
            else:
                print("El resultado de la division es: ", a / b)
        else:
                print("Error: La opcion seleccionada no es correcta...")
