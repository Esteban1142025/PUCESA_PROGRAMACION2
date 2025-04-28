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

def buscar_libro():
    ISBN = int(input("Ingrese el ISBN del libro a buscar: "))
    for libro in libros:
        if libro.ISBN == ISBN:
            print(libro.datos_libro())
            return book

def mostrar_biblioteca():
    for i in libros:
        print(f"{i}\n")