import numpy as np
import matplotlib as plt
from instrumento import Instrumento

ins = Instrumento()
estudiantes, trabajadores_de_bancos = ins.getData()

print("Trabajadores de banco: ",len(trabajadores_de_bancos))
print("Estudiantes: ",len(estudiantes))

