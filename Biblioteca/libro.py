class book:
    ISBN = int()
    prestamos = []
        
    def __init__(self,titulo,autor,ISBN,genero):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.genero = genero
        self.prestamos = []

    def datos_libro(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.ISBN}")
        print(f"Genero: {self.genero}")
        print(f"Listado de prestamos: {self.prestamos}")




#ISBN = codigo de 13 digitos
#prestamo = listado de personas