from Profesores import Profesor

###############################################
#           CREACION DE CURSOS               #
###############################################

class Curso:
    def __init__(self,nombre, profesor : Profesor):
        self.nombre = nombre 
        self.Profesor = profesor
    
    def getCurso(self):
        return {
            'Nombre' : self.nombre,
            'Profesor' : self.Profesor.getProfesor()
        }
