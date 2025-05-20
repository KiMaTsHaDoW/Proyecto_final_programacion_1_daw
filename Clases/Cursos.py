class Curso:
    def __init__(self, anio:str, nivel:str):
        self.anio:str = anio
        self.nivel:str = nivel

    def __str__(self):
        return f"Año: {self.anio} - Nivel: {self.nivel}"
