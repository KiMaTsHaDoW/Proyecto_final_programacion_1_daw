class Alumno:
    def __init__(self, nombre:str, apellidos:str, tramo_concedido:str, seccion:str):
        self.nombre:str = nombre
        self.apellidos:str = apellidos
        self.tramo_concedido:str = tramo_concedido
        self.seccion:str = seccion

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - Tramo: {self.tramo_concedido} - Sección: {self.seccion}"
