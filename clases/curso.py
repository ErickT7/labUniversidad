
#from .profesor import Profesor
class Curso():
    def __init__(self, nombre, codigo, profesor):
        #atributos basicos de un  curso
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        
    def __str__(self):
        # return en cadena del curso, incluye el nombre del profesor
          return f"Curso:{self.nombre}, Codigo: {self.codigo}, {self.profesor}"
 