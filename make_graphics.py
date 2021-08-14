import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from instrumento import Instrumento

ins = Instrumento()
estudiantes, empleados_de_bancos = ins.getData()
poblacion = estudiantes + empleados_de_bancos

tamanio_de_poblacion = len(poblacion)

# Variables de habilidades blandas poblacion

############## Variables Estudiantes ##############

# Variables habilidades blandas estudiantes

trabajo_en_equipo_es = []
liderazgo_es = []
manejo_de_estres_es = []
buena_comunicacion_es = []
puntualidad_y_responsabilidad_es = []
resolucion_de_problemas_es = []
proactividad_es = []
respeto_a_direcencias_es = []

# Frecuencias
fre_actualizacion_tec_conocidas_es = []
fre_aprendizaje_nueva_tec_es = []

############## Variables Bancos ##############

# Variables habilidades blandas bancos

trabajo_en_equipo_bc = []
liderazgo_bc = []
manejo_de_estres_bc = []
buena_comunicacion_bc = []
puntualidad_y_responsabilidad_bc = []
resolucion_de_problemas_bc = []
proactividad_bc = []
respeto_a_direcencias_bc = []

# Frecuencias
fre_actualizacion_tec_conocidas_bc = []
fre_aprendizaje_nueva_tec_bc = []

# Colores
colores = ["#f0325b","#3268f0","#f0cd32","#58f032","#32f0ea", "#9432f0", "#f032e0", "#f09432"]

################ Datos de la población ################



################ Datos de los estudiantes ################

for individuo in estudiantes:
    trabajo_en_equipo_es.append(individuo["Trabajo en equipo"])
    liderazgo_es.append(individuo["Liderazgo"])
    manejo_de_estres_es.append(individuo["Manejo del estrés\xa0"])
    buena_comunicacion_es.append(individuo["Buena comunicación"])
    puntualidad_y_responsabilidad_es.append(individuo["Puntualidad y responsabilidad"])
    resolucion_de_problemas_es.append(individuo["Resolución de problemas"])
    proactividad_es.append(individuo["Proactividad"])
    respeto_a_direcencias_es.append(individuo["Respeto hacia las diferentes opiniones de los demás."])

    #Tecnologias y Frecuencia de actualizacion
    fre_actualizacion_tec_conocidas_es.append(individuo["De las tecnologías que usted domina ¿qué tan frecuente actualiza su conocimiento sobre estas?"])
    fre_aprendizaje_nueva_tec_es.append(individuo["¿Qué tan frecuente aprende nuevas tecnologías?"])

################ Datos de los empleados ################

for individuo in empleados_de_bancos:
    trabajo_en_equipo_bc.append(individuo["Trabajo en equipo"])
    liderazgo_bc.append(individuo["Liderazgo"])
    manejo_de_estres_bc.append(individuo["Manejo del estrés\xa0"])
    buena_comunicacion_bc.append(individuo["Buena comunicación"])
    puntualidad_y_responsabilidad_bc.append(individuo["Puntualidad y responsabilidad"])
    resolucion_de_problemas_bc.append(individuo["Resolución de problemas"])
    proactividad_bc.append(individuo["Proactividad"])
    respeto_a_direcencias_bc.append(individuo["Respeto hacia las diferentes opiniones de los demás."])

    #Tecnologias y Frecuencia de actualizacion
    fre_actualizacion_tec_conocidas_bc.append(individuo["De las tecnologías que usted domina ¿qué tan frecuente actualiza su conocimiento sobre estas?"])
    fre_aprendizaje_nueva_tec_bc.append(individuo["¿Qué tan frecuente aprende nuevas tecnologías?"])

################ Habilidades Blandas ################

# Estudiantes
trabajo_en_equipo_es = np.array(trabajo_en_equipo_es)
liderazgo_es = np.array(liderazgo_es)
manejo_de_estres_es = np.array(manejo_de_estres_es)
buena_comunicacion_es = np.array(buena_comunicacion_es)
puntualidad_y_responsabilidad_es = np.array(puntualidad_y_responsabilidad_es)
resolucion_de_problemas_es = np.array(resolucion_de_problemas_es)
proactividad_es = np.array(proactividad_es)
respeto_a_direcencias_es = np.array(respeto_a_direcencias_es)

#empleados
trabajo_en_equipo_bc = np.array(trabajo_en_equipo_bc)
liderazgo_bc = np.array(liderazgo_bc)
manejo_de_estres_bc = np.array(manejo_de_estres_bc)
buena_comunicacion_bc = np.array(buena_comunicacion_bc)
puntualidad_y_responsabilidad_bc = np.array(puntualidad_y_responsabilidad_bc)
resolucion_de_problemas_bc = np.array(resolucion_de_problemas_bc)
proactividad_bc = np.array(proactividad_bc)
respeto_a_direcencias_bc = np.array(respeto_a_direcencias_bc)

nombre_habilidades = ["Trabajo en equipo","Liderazgo","Manejo del estrés","Buena comunicación","Puntualidad y responsabilidad","Resolución de problemas","Proactividad","Respeto hacia las diferentes opiniones de los demás."]
identificador_habilidades = ["H1","H2","H3","H4","H5","H6","H7","H8"]

promedios_habilidades_es = [np.mean(trabajo_en_equipo_es), np.mean(liderazgo_es), np.mean(manejo_de_estres_es), np.mean(buena_comunicacion_es), np.mean(puntualidad_y_responsabilidad_es), np.mean(resolucion_de_problemas_es), np.mean(proactividad_es), np.mean(resolucion_de_problemas_es)]
promedios_habilidades_bc = [np.mean(trabajo_en_equipo_bc), np.mean(liderazgo_bc), np.mean(manejo_de_estres_bc), np.mean(buena_comunicacion_bc), np.mean(puntualidad_y_responsabilidad_bc), np.mean(resolucion_de_problemas_bc), np.mean(proactividad_bc), np.mean(resolucion_de_problemas_bc)]

habilidades_es_df = pd.DataFrame({
    "Habilidades": [x.replace(" ", "\n") for x in nombre_habilidades],
    "Identificador": identificador_habilidades,
    "Promedios": promedios_habilidades_es
    })

habilidades_bc_df = pd.DataFrame({
    "Habilidades": nombre_habilidades,
    "Identificador": identificador_habilidades,
    "Promedios": promedios_habilidades_bc
    })


# Grafica estudiantes
plt.bar('Identificador', 'Promedios',data=habilidades_es_df, color=colores)
plt.title("Importancia de Habilidades blandas que poseen los estudiantes de Ingeniería en Sistemas\n")
plt.xlabel("Habilidad")
plt.ylabel("Importancia")
plt.ylim([0,5])

plt.savefig("./fig/habilidades_blandas_es.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()

# Grafica empleados
plt.bar('Identificador', 'Promedios',data=habilidades_bc_df, color=colores)
plt.title("Importancia de Habilidades blandas requeridas en el sector bancario\n")
plt.xlabel("Habilidad")
plt.ylabel("Importancia")
plt.ylim([0,5])

plt.savefig("./fig/habilidades_blandas_bc.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()

############## Tecnologias y Frecuencia ##############

# Estudiantes
fre_actualizacion_tec_conocidas_es = np.array(fre_actualizacion_tec_conocidas_es)
fre_aprendizaje_nueva_tec_es = np.array(fre_aprendizaje_nueva_tec_es)

fre_act_set_es, frecuencia_act_es = np.unique(fre_actualizacion_tec_conocidas_es, return_counts=True)
fre_apr_set_es, frecuencia_apr_es = np.unique(fre_aprendizaje_nueva_tec_es, return_counts=True)

frecuencia_act_es = (frecuencia_act_es / len(estudiantes)) * 100
frecuencia_apr_es = (frecuencia_apr_es / len(estudiantes)) * 100

# Frecuencia actualización
fig, ax = plt.subplots()

ax.pie(frecuencia_act_es, labels=fre_act_set_es, colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red'], autopct='%.0f%%')
plt.title("Frecuencia de actualización de conocimientos técnicos \n de estudiantes por egresar de Ingeniería en Sistemas \n en la UNAH")

plt.savefig("./fig/actualizacion_de_conocimientos_es.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()

# Frecuencia aprendizaje
fig, ax = plt.subplots()

ax.pie(frecuencia_apr_es, labels=fre_apr_set_es, colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red'], autopct='%.0f%%')
plt.title("Frecuencia de aprendizaje de nuevos conocimientos técnicos \n de estudiantes por egresar de Ingeniería en Sistemas \n en la UNAH")

plt.savefig("./fig/aprendizaje_de_conocimientos_es.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()


# Bancos
fre_actualizacion_tec_conocidas_bc = np.array(fre_actualizacion_tec_conocidas_bc)
fre_aprendizaje_nueva_tec_bc = np.array(fre_aprendizaje_nueva_tec_bc)

fre_act_set_bc, frecuencia_act_bc = np.unique(fre_actualizacion_tec_conocidas_bc, return_counts=True)
fre_apr_set_bc, frecuencia_apr_bc = np.unique(fre_aprendizaje_nueva_tec_bc, return_counts=True)

frecuencia_act_bc = (frecuencia_act_bc / len(empleados_de_bancos)) * 100
frecuencia_apr_bc = (frecuencia_apr_bc / len(empleados_de_bancos)) * 100

# Frecuencia actualización
fig, ax = plt.subplots()

ax.pie(frecuencia_act_bc, labels=fre_act_set_bc, colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red'], autopct='%.0f%%')
plt.title("Frecuencia de actualización de conocimientos técnicos \n de empleados del sector bancario")

plt.savefig("./fig/actualizacion_de_conocimientos_bc.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        metadata=None)
plt.clf()

# Frecuencia aprendizaje
fig, ax = plt.subplots()

ax.pie(frecuencia_apr_bc, labels=fre_apr_set_bc, colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red'], autopct='%.0f%%')
plt.title("Frecuencia de aprendizaje de nuevos conocimientos técnicos \n de empleados del sector bancario")

plt.savefig("./fig/aprendizaje_de_conocimientos_bc.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        metadata=None)
plt.clf()














