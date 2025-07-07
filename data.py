from Cursos import Curso
from Profesores import Profesor
from FraccionCurso import FraccionCurso
from Horario import Horario

proferos1 =  Profesor(
    'Carlos',
    'Ramirez'
)
proferos2 =  Profesor(
    'Brenda',
    'Ramirez'
)

proferos3 =  Profesor(
    'Pedro',
    'Ramirez'
)
proferos4 =  Profesor(
    'Juan',
    'Ramirez'
)
########################################################################

matematicas = Curso(
    'Matematicas',
    proferos1
)

lenguaje = Curso(
    'Lenguaje',
    proferos2
)

fisica = Curso(
    'Fisica',
    proferos3
)

biologia = Curso(
    'Biologia',
    proferos1
)

razMatematico = Curso(
    'Raz Matematico',
    proferos1
)

############################################################################

fra01 = FraccionCurso(
    7,10,fisica,
)

fra02 = FraccionCurso(
    10,12,razMatematico
)

fra03 = FraccionCurso(
    12,13,biologia
)


horarioprof1 = Horario([fra01,fra02,fra03])

cursos = [matematicas, lenguaje, fisica, biologia]

