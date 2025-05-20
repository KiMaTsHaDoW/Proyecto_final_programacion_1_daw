class Libro:
    def __init__(self, titulo:str, autor:str, isbn:str, numero_ejemplares:int):
        self.titulo:str = titulo
        self.autor:str = autor
        self.isbn:str = isbn
        self.numero_ejemplares:int = numero_ejemplares

    def __str__(self):
        return f"{self.titulo} by {self.autor} - ISBN: {self.isbn} - Ejemplares: {self.numero_ejemplares}"
