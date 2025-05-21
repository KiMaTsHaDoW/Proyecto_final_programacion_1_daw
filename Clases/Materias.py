class Materia:
    def __init__(self, num_materia:int, nombre:str):
        self.num_materia:int = num_materia
        self.nombre:str = nombre

    def __str__(self):
        return f"{self.nombre} - Numero de materia: {self.num_materia}"
