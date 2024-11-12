from .persona import Persona

#Clase profesor que hereda de persona
class Profesor(Persona):
    def __init__(self, nombre, edad, sexo, codigo, especialidad):
        #Inializacion de atributos de persona y atributos adicionales
        super().__init__(nombre, edad, sexo)
        self.codigo = codigo
        self.especialidad = especialidad
    
    def __str__(self):
        #Representacion en cadena de profesor
         return f"{super().__str__()}, Codigo: {self.codigo}, Especialidad: {self.especialidad}"    