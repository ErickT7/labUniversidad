class Persona:
    def __init__(self, nombre , edad , sexo):
        # atributos de la clase persona
        self.nombre= nombre
        self.edad= edad
        self.sexo = sexo
    def __str__(self):
        # Representacion de la cadena de la persona
        return f"Nombre:{self.nombre}, Edad: {self.edad}, Sexo:{self.sexo}"
    
    