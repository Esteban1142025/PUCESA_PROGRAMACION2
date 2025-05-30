from libro import book

prestamos = []
libros = []

def registrar_libro():
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    ISBN = int(input("Ingrese el ISBN del libro: "))
    genero = input("Ingrese el genero del libro: ")
    libro = book(titulo,autor,ISBN,genero)
    libros.append(libro)
    print("El libro se ha registrado!")

def registrar_prestamo():
    if not libros:
        print("No hay libros registrados")
    else:
        ISBN = int(input("Ingrese el codigo del libro a prestar: "))
        for libro in libros:
            if libro.ISBN == ISBN:
                persona = input("Ingrese el nombre del lector: ")
                prestamos.append(persona)
                print("El prestamo se ha registrado")

def buscar_libro():
    if not libros:
        print("No hay libros registrados")
    else:
        ISBN = int(input("Ingrese el ISBN del libro a buscar: "))
        for libro in libros:
            if libro.ISBN != ISBN:
                print("codigo invalido, intente nuevamente")
            else:
                print(libro.datos_libro())
                print(f"Listado de prestamos: {prestamos}")
                return book

def mostrar_biblioteca():
    if not libros:
        print("No hay libros registrados")
    else:
        for i in libros:
            i.datos_libro()
            print(f"Listado de prestamos: {prestamos}")
            print("\n")