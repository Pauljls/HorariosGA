
###############################################
#           CREACION DE PROFESORES            #
###############################################

class Profesor:
    def __init__(self, nombres, apellidos):
        self.nombres = nombres
        self.apellidos = apellidos

    def getProfesor(self):
        return {
            'Nombres': self.nombres,
            'Apellidos' : self.apellidos
        }
