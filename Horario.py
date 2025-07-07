
from FraccionCurso import FraccionCurso

###############################################
#           CREACION DE HORARIOS              #
###############################################

from typing import Optional

class Horario:
    def __init__(self,
                 lunes: Optional[list[FraccionCurso]] = None,
                 martes: Optional[list[FraccionCurso]] = None,
                 miercoles: Optional[list[FraccionCurso]] = None,
                 jueves: Optional[list[FraccionCurso]] = None,
                 viernes: Optional[list[FraccionCurso]] = None):
        self.lunes = lunes if lunes is not None else []
        self.martes = martes if martes is not None else []
        self.miercoles = miercoles if miercoles is not None else []
        self.jueves = jueves if jueves is not None else []
        self.viernes = viernes if viernes is not None else []

    def getHorario(self):
        return {
            'lunes': self.lunes,
            'martes':self.martes ,
            'miercoles':self.miercoles ,
            'jueves':self.jueves ,
            'viernes':self.viernes ,
        }