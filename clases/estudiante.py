from .persona import Persona

# Clase estudiante hereda de persona
class Estudiante (Persona):
    def __init__ (self, nombre, edad, sexo, carnet, carrera):
        # Inicializacion de atributos de persona y atributos adicionales
        super().__init__(nombre, edad, sexo)   
        self.carnet = carnet
        self.carrera = carrera
    
    def __str__(self):
        # Representacion en cadena de estudiante
        return  f"{super().__str__()}, Carnet: {self.carnet}, Carrera: {self.carrera}"
    
    