from clases.universidad import Universidad
from clases.profesor import Profesor
from clases.curso import Curso
from clases.estudiante import Estudiante

# Crea la universidad
universidad =Universidad("Universidad de El Salvador")

#crear profesor
profesor_juan = Profesor("Juan Perez", 30, "Masculino", 20240810, "Matematicas")
profesor_maria = Profesor("Maria Lopez", 35, "Femenino", 21241254, "Fisica")
profesor_pedro = Profesor("Pedro Ramirez", 40, "Masculino", 21251412, "Quimica") 

# crear los cursos con los profesores respectivos
curso_matematicas= Curso("Matematicas","MAT0102", profesor_juan)
curso_fisica= Curso("Fisica","FIS0102", profesor_maria)
curso_quimica= Curso("Quimica","QUI0102", profesor_pedro)

#agregar los cursos a la universidad
universidad.agregar_curso(curso_matematicas)
universidad.agregar_curso(curso_fisica)
universidad.agregar_curso(curso_quimica)

#crear un estudiante
estudiante_carlos= Estudiante("Carlos Perez", 20, "Masculino", 20211412, "Ingenieria en sistemas")

#imprimir la informacion de la universidad del estudiante, profesor y curso

print(universidad)
print("---------------------------")
print(estudiante_carlos)
print("---------------------------")
print(profesor_juan)
print("---------------------------")
print(curso_fisica)

curso_nuevo_fisica= Curso ("Fisica", "FIS0232", profesor_maria)
universidad.agregar_curso(curso_nuevo_fisica)

#imprimir la uiversida con el nuevo curso
print("---------------------------")
print(universidad)


