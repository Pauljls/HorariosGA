
from Profesores import Profesor

from Cursos import Curso

from data import cursos
from data import horarioprof1

import pandas as pd

horas = list(range(7, 13))  # De 7:00 a 18:00

# Días de la semana
dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']

# Inicializamos la tabla vacía
tabla_horario = pd.DataFrame(index=[f"{h}:00 - {h+1}:00" for h in horas], columns=[d.capitalize() for d in dias])
tabla_horario[:] = ""  # Llenamos con cadenas vacías
# Llenar la tabla con los cursos según bloque horario
for dia, bloques in horarioprof1.getHorario().items():
    for bloque in bloques:
        curso = bloque['curso']['Nombre']
        prof = f"{bloque['curso']['Profesor']['Nombres']} {bloque['curso']['Profesor']['Apellidos']}"
        for h in range(bloque['horaiinicio'], bloque['horatermino']):
            fila = f"{h}:00 - {h+1}:00"
            tabla_horario.at[fila, dia.capitalize()] = curso  # o f"{curso}\n({prof})" si quieres incluir el profesor

print(tabla_horario)
#print(horarioprof1.getHorario().items())