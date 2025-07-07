from Cursos import Curso

###############################################
#           CREACION DE FRACCION CURSO        #
###############################################

class FraccionCurso():
    def __init__(self, horainicio :int , horatermino : int, curso :  Curso):
        self.curso = curso
        self.horainicio = horainicio
        self.horatermino = horatermino
    
    def getFraccionCurso(self):
        return {
            'curso' : self.curso.getCurso(),
            'horaiinicio' : self.horainicio,
            'horatermino' : self.horatermino
        }