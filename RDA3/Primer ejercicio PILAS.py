historial = []
print("Historial vacio:", historial, "\n")

print("<><><><><><> HISTORIAL <><><><><><>")
print("<<<Ingrese 5 si desea salir del programa>>>")

while True:
    print("""
        Opciones disponibles:
        1) Visitar nuevas paginas
        2) Mostrar Historial completo
        3) Volver a la pagina anterior
        4) Verificar si el historial esta vacio
        5) Salir
        """)
    
    
    opcion = int(input("Ingrese una opcion disponible: "))
    if opcion not in [1,2,3,4,5]:
        print("Error! Seleccione una opcion valida...")

    elif opcion == 1:
        print('Ingrese "salir" para regresar al menu principal \n')
        while True:
            pagina = input("Ingrese la url de la pagina que va a visitar: ")
            historial.append(pagina)
            if pagina == "salir":
                historial.pop()
                break

    elif opcion == 2:
        print("Historial completo:", historial)
    
    elif opcion == 3:
        if historial:
            try:
                eliminada = historial.pop()
                print("Volviste desde:", eliminada)
                print("Página actual:", historial[-1])
            except IndexError:
                print("No puedes volver, historial vacío.")
        else:
            print("No puedes volver, historial vacío.")

    elif opcion == 4:
        if len(historial) == 0:
            print("El historial está vacío.")
        else:
            print("Páginas restantes:", historial)
    elif opcion == 5:
        print("Finalizando programa...")
        break
