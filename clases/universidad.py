from .curso import Curso

# clases universidad
class Universidad:
        def __init__(self, nombre):
            #atributos nombre de la universidad y listas de cursos
            self.nombre = nombre
            self.cursos= []
        def agregar_curso(self, curso):
            # Metodo para agregar cursos a la universidad
            self.cursos.append(curso)
        def __str__(self):
             #Representacion de la cadena de la universidad y sus cursos
             cursos_str = "\n".join([str(curso)for curso in self.cursos])
             return f"Universidad: {self.nombre}\nCursos:\n{cursos_str}"
         
         
         
         