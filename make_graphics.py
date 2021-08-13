import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from instrumento import Instrumento

ins = Instrumento()
estudiantes, trabajadores_de_bancos = ins.getData()
poblacion = estudiantes + trabajadores_de_bancos

tamanio_de_poblacion = len(poblacion)

# Calcular promedio habilidades blandas
trabajo_en_equipo = []
liderazgo = []
manejo_de_estres = []
buena_comunicacion = []
puntualidad_y_responsabilidad = []
resolucion_de_problemas = []
proactividad = []
respeto_a_direcencias = []

for individuo in poblacion:
    trabajo_en_equipo.append(individuo["Trabajo en equipo"])
    liderazgo.append(individuo["Liderazgo"])
    manejo_de_estres.append(individuo["Manejo del estrés\xa0"])
    buena_comunicacion.append(individuo["Buena comunicación"])
    puntualidad_y_responsabilidad.append(individuo["Puntualidad y responsabilidad"])
    resolucion_de_problemas.append(individuo["Resolución de problemas"])
    proactividad.append(individuo["Proactividad"])
    respeto_a_direcencias.append(individuo["Respeto hacia las diferentes opiniones de los demás."])

trabajo_en_equipo = np.array(trabajo_en_equipo)
liderazgo = np.array(liderazgo)
manejo_de_estres = np.array(manejo_de_estres)
buena_comunicacion = np.array(buena_comunicacion)
puntualidad_y_responsabilidad = np.array(puntualidad_y_responsabilidad)
resolucion_de_problemas = np.array(resolucion_de_problemas)
proactividad = np.array(proactividad)
respeto_a_direcencias = np.array(respeto_a_direcencias)

nombre_habilidades = ["Trabajo en equipo","Liderazgo","Manejo del estrés","Buena comunicación","Puntualidad y responsabilidad","Resolución de problemas","Proactividad","Respeto hacia las diferentes opiniones de los demás."]
identificador_habilidades = ["H1","H2","H3","H4","H5","H6","H7","H8"]
promedios_habilidades = [np.mean(trabajo_en_equipo), np.mean(liderazgo), np.mean(manejo_de_estres), np.mean(buena_comunicacion), np.mean(puntualidad_y_responsabilidad), np.mean(resolucion_de_problemas), np.mean(proactividad), np.mean(respeto_a_direcencias)]

habilidades_df = pd.DataFrame({
    "Habilidades": nombre_habilidades,
    "Identificador": identificador_habilidades,
    "Promedios": promedios_habilidades
    })

habilidades_df_ordenadas = habilidades_df.sort_values('Promedios', ascending=False)

plt.bar('Identificador', 'Promedios',data=habilidades_df_ordenadas)
#plt.bar_label("Importancia de habilidades blandas.")
plt.title("Importancia de Habilidades blandas")
plt.xlabel("Habilidad")
plt.ylabel("Importancia")

#plt.xticks(np.arange(len(x)), x)

plt.savefig("./fig/habilidades_blandas.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        metadata=None)
plt.clf()

#print("Trabajadores de banco: ",len(trabajadores_de_bancos))
#print("Estudiantes: ",len(estudiantes))

