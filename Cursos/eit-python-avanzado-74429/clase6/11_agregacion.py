class Libro:
    def __init__(self, titulo: str, autor: str, año: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.año = año


class Biblioteca:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.libros: list[Libro] = []
        # Agregación: una Biblioteca tiene varios Libros,
        # pero los libros pueden existir sin la biblioteca

    def agregar_libro(self, libro: Libro) -> None:
        self.libros.append(libro)

    def eliminar_libro(self, libro: Libro) -> None:
        if libro in self.libros:
            self.libros.remove(libro)
        else:
            print(f"⛔ El libro '{libro.titulo}' no está en la biblioteca.'")

    def listar_libros(self):
        print(f"Libros de '{self.nombre}'")
        for libro in self.libros:
            print(f"- {libro.titulo} de {libro.autor} ({libro.año})")


libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Órganon", "Aristóteles", -384)

biblioteca = Biblioteca("Biblioteca Central")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

biblioteca.listar_libros()

biblioteca.eliminar_libro(libro2)
biblioteca.eliminar_libro(libro2)

biblioteca.listar_libros()
