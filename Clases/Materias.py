class Materia:
    def __init__(self, nombre:str, departamento:str):
        self.nombre:str = nombre
        self.departamento:str = departamento

    def __str__(self):
        return f"{self.nombre} - Departamento: {self.departamento}"
