import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Patch
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

# Interes en el sector banacario
interes_estudiates = []
interes_para_trabajar = []

# Adquisición de conocimientos
lenguajes_progra = []
conocimientos_tecnicos_generales = []
bases_de_datos = []
sistemas_operativos = []

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

# Centros de estudio
centros_de_estudio = []

# Bancos en los que ha trabajado
bancos_laborados = []
areas_de_desempenio = []

"""
# Habilidades tecnicas
lenguajes_de_programacion = []
uso_de_librerias = []
uso_de_frameworks = []
desa_app_web = []
desa_app_escritorio = []
desa_app_movil = []
desa_embebidos = []
metodologias_de_desarrollo = []
ataques_informaticos = []
buenas_practicas_de_seguridad = []
protocolos_de_redes = []
conocimientos_basico_redes = []
operaciones_en_bases = []
administracion_bases = []
"""

# Empleados con certificados
empleados_crt = []
certificados = []

# Bases de datos mas usdadas
bases_mas_usadas = []

# Sistemas operativos mas usados
so_mas_usados = []

# Lenguajes mas usados
lenguajes_mas_usados = []

#############################################################################

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

    #Interes en el sector bancario
    interes_estudiates.append(individuo["¿Qué tanto le interesa trabajar en el sector bancario?"])
    interes_para_trabajar.append(individuo["Al momento de buscar empleo ¿qué le interesa más?"])

    # Adquisición de conocimientos
    lenguajes_progra = lenguajes_progra + individuo["¿Cómo ha adquirido sus conocimientos en los lenguajes de programación preguntados anteriormente?\xa0\xa0\xa0(Puede escoger más de una opción)"].split(";")
    conocimientos_tecnicos_generales = conocimientos_tecnicos_generales + individuo["¿Cómo ha adquirido sus conocimientos sobre los conceptos de la pregunta anterior?\xa0(Puede escoger más de una opción)"].split(";")
    bases_de_datos = bases_de_datos + individuo["¿Cómo ha adquirido sus conocimientos en los gestores de base de datos preguntados anteriormente?\xa0\xa0(Puede escoger más de una opción)"].split(";")
    sistemas_operativos = sistemas_operativos + individuo["¿Cómo ha adquirido sus conocimientos en los sistemas operativos de la pregunta anterior?\xa0(Puede escoger más de una opción)"].split(";")


################ Datos de los empleados ################
for individuo in empleados_de_bancos:
    #print(individuo)
    #print()
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

    #Centros de estudio
    centros_de_estudio.append(individuo["Centro de estudio universitario en donde cursó la licenciatura en Ingeniería en Sistemas:"].upper())

    # Bancos en los que ha trabajados
    bancos_laborados = bancos_laborados + individuo["Entidad bancaria en la cual trabaja o ha trabajado:\xa0\xa0(Puede escoger más de una opción)"].split(";")

    if individuo["¿Se ha certificado en alguna área perteneciente a la carrera de Ingeniería en Sistemas?"] == "Sí":
        empleados_crt.append(individuo)
        certificados = certificados + individuo["Indique en cuáles áreas se ha certificado:\xa0(Puede escoger más de una opción)"].split(";")

    # Areas de desempeño
    areas_de_desempenio = areas_de_desempenio + individuo["¿En qué área se desempeña o desempeñó en el sector bancario?\xa0\xa0(Puede escoger más de una opción)"].split(";")


"""
    # Habilidades tecnicas
    lenguajes_de_programacion.append([""])
    uso_de_librerias.append([""])
    uso_de_frameworks.append([""])
    desa_app_web.append([""])
    desa_app_escritorio.append([""])
    desa_app_movil.append([""])
    desa_embebidos.append([""])
    metodologias_de_desarrollo.append([""])
    ataques_informaticos.append([""])
    buenas_practicas_de_seguridad.append([""])
    protocolos_de_redes.append([""])
    conocimientos_basico_redes.append([""])
    operaciones_en_bases.append([""])
    administracion_bases.append([""])
"""

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
fig, ax = plt.subplots()
ax.bar('Identificador', 'Promedios',data=habilidades_bc_df, color=colores)
plt.title("Importancia de Habilidades blandas requeridas en el sector bancario\n")
plt.xlabel("Habilidad")
plt.ylabel("Importancia")
plt.ylim([0,5])

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(nombre_habilidades, colores))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=nombre_habilidades, handles=patches, title='Habilidades', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

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


############ Interes de los estudiantes en el sector banacario ############
interes_estudiates = np.array(interes_estudiates)


############ Interes de los estudiantes para trabajar en el sector banacario ############
interes_para_trabajar = np.array(interes_para_trabajar)
interes_set, fre_interes = np.unique(interes_para_trabajar, return_counts=True) 

fre_interes = (fre_interes / len(estudiantes)) * 100

fig, ax = plt.subplots()
ax.pie(fre_interes, labels=interes_set, colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red'], autopct='%.0f%%' )

plt.title("Interes de los estudiantes en un empleo")

plt.savefig("./fig/interes_estudiates_trabajo_banco.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()


############ Centros de estudio de los empleados de bancos ############
centros_de_estudio = np.array(centros_de_estudio)
centros_set, fre_centros = np.unique(centros_de_estudio, return_counts=True)

fre_centros = (fre_centros / len(empleados_de_bancos)) * 100

centros_df = pd.DataFrame({
    'Centros': centros_set,
    'Porcentaje': fre_centros
    })

centros_df = centros_df.sort_values('Porcentaje', ascending=True)

fig, ax = plt.subplots()

ax.barh('Centros', 'Porcentaje', data=centros_df)
plt.title("Universidades en las que estudiaron los empleados")
ax.xaxis.set_major_formatter(mtick.PercentFormatter())

plt.ylabel("Universidades")
plt.xlabel("Porcentaje de empleados que estudiaron en X universidad")

plt.savefig("./fig/centros_de_estudio.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()



############ Centros de estudio de los empleados de bancos ############
bancos_laborados = np.array(bancos_laborados)
bancos_set, fre_bancos = np.unique(bancos_laborados, return_counts=True)

fre_bancos = (fre_bancos / len(empleados_de_bancos)) * 100

bancos_df = pd.DataFrame({
    'Bancos': bancos_set,
    'Porcentaje': fre_bancos
    })

bancos_df.drop(labels=0, axis=0)

bancos_df = bancos_df.sort_values('Porcentaje', ascending=True)

fig, ax = plt.subplots()

ax.barh('Bancos', 'Porcentaje', data=bancos_df)
plt.title("Listado bancos")
ax.xaxis.set_major_formatter(mtick.PercentFormatter())

plt.ylabel("Bancos")
plt.xlabel("Porcentaje de empleados que trabajaron en X banco")

plt.savefig("./fig/bancos_laborados.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()

############ Adquisición de conocimientos ############
totales = []
totales = lenguajes_progra + conocimientos_tecnicos_generales + bases_de_datos + sistemas_operativos

lenguajes_progra = np.array(lenguajes_progra)
conocimientos_tecnicos_generales = np.array(conocimientos_tecnicos_generales)
bases_de_datos = np.array(bases_de_datos)
sistemas_operativos = np.array(sistemas_operativos)

totales = np.array(totales)

lenguajes_progra_set, lenguajes_progra_count = np.unique(lenguajes_progra, return_counts=True)
conocimientos_tecnicos_generales_set, conocimientos_tecnicos_generales_count = np.unique(conocimientos_tecnicos_generales, return_counts=True)
bases_de_datos_set, bases_de_datos_count = np.unique(bases_de_datos, return_counts=True)
sistemas_operativos_set, sistemas_operativos_count = np.unique(sistemas_operativos, return_counts=True)

totales_set, totales_count = np.unique(totales, return_counts=True)

lenguajes_por = (lenguajes_progra_count / len(estudiantes)) * 100
generales_por = (conocimientos_tecnicos_generales_count / len(estudiantes)) * 100
bases_por = (bases_de_datos_count / len(estudiantes)) * 100
sistemas_por = (sistemas_operativos_count / len(estudiantes)) * 100

totales_por = ((totales_count / 4) / len(estudiantes)) * 100

lenguajes_df = pd.DataFrame({
    "Lenguajes_adq": lenguajes_progra_set,
    "Porcentaje": lenguajes_por
    })
lenguajes_df = lenguajes_df.drop(labels=0, axis=0)

generales_df = pd.DataFrame({
    "Generales_adq": conocimientos_tecnicos_generales_set,
    "Porcentaje": generales_por
    })
generales_df = generales_df.drop(labels=0, axis=0)

bases_df = pd.DataFrame({
    "Bases_adq": bases_de_datos_set,
    "Porcentaje": bases_por
    })
bases_df = bases_df.drop(labels=0, axis=0)

sistemas_df = pd.DataFrame({
    "Sistemas_adq": sistemas_operativos_set,
    "Porcentaje": sistemas_por
    })
sistemas_df = sistemas_df.drop(labels=0, axis=0)


totales_df = pd.DataFrame({
    "Totales_adq": totales_set,
    "Porcentaje": totales_por
    })
totales_df = totales_df.drop(labels=0, axis=0)

### Lenguajes
fig, ax = plt.subplots()
ax.pie(lenguajes_df['Porcentaje'].tolist(), colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray'], autopct='%.0f%%' )

plt.title("Adquisición de conocimientos tecnicos de lenguajes de programación")

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(lenguajes_df['Lenguajes_adq'].tolist(), ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray']))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=lenguajes_df['Lenguajes_adq'].tolist(), handles=patches, title='Adquisición', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

plt.savefig("./fig/lenguajes_adq.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()

### Generales
fig, ax = plt.subplots()
ax.pie(generales_df['Porcentaje'].tolist(), colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray', 'tab:green'], autopct='%.0f%%' )

plt.title("Adquisición de conocimientos tecnicos de generales")

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(generales_df['Generales_adq'].tolist(), ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray', 'tab:green']))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=generales_df['Generales_adq'].tolist(), handles=patches, title='Adquisición', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

plt.savefig("./fig/generales_adq.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()

### Bases
fig, ax = plt.subplots()
ax.pie(bases_df['Porcentaje'].tolist(), colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray'], autopct='%.0f%%' )

plt.title("Adquisición de conocimientos tecnicos de bases de datos")

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(bases_df['Bases_adq'].tolist(), ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray']))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=bases_df['Bases_adq'].tolist(), handles=patches, title='Adquisición', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

plt.savefig("./fig/bases_adq.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()

### Sistemas
fig, ax = plt.subplots()
ax.pie(sistemas_df['Porcentaje'].tolist(), colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray', 'tab:green', 'tab:purple'], autopct='%.0f%%' )

plt.title("Adquisición de conocimientos tecnicos de Sistemas Operativos")

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(sistemas_df['Sistemas_adq'].tolist(), ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray', 'tab:green', 'tab:purple']))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=sistemas_df['Sistemas_adq'].tolist(), handles=patches, title='Adquisición', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

plt.savefig("./fig/sistemas_adq.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()


### Totales
fig, ax = plt.subplots()
ax.bar('Totales_adq', 'Porcentaje', data=totales_df, color=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray', 'tab:green', 'tab:purple', 'tab:pink', 'm'])

plt.tick_params(
    axis='x',        
    which='both',   
    bottom=False,  
    top=False,    
    labelbottom=False)

plt.title("Adquisición de conocimientos tecnicos totales")

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(totales_df['Totales_adq'].tolist(), ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray', 'tab:green', 'tab:purple', 'tab:pink', 'm']))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=totales_df['Totales_adq'].tolist(), handles=patches, title='Adquisición', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

plt.savefig("./fig/totales_adq.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()


############ Certificaciones de empleados ############
certificados = np.array(certificados)

certificados_set, certificados_count = np.unique(certificados, return_counts=True)

certificados_pro = (certificados_count / len(empleados_crt)) * 100

certificados_df = pd.DataFrame({
    'Certificados': certificados_set,
    'Porcentaje': certificados_pro
    })
certificados_df = certificados_df.drop(labels=0, axis=0)

fig, ax = plt.subplots()
ax.bar('Certificados', 'Porcentaje', data=certificados_df, color=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray', 'tab:green', 'tab:purple', 'tab:pink', 'm'])

plt.tick_params(
    axis='x',        
    which='both',   
    bottom=False,  
    top=False,    
    labelbottom=False)

plt.title("Adquisición de conocimientos tecnicos totales")

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(certificados_df['Certificados'].tolist(), ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray', 'tab:green', 'tab:purple', 'tab:pink', 'm']))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=certificados_df['Certificados'].tolist(), handles=patches, title='Certificados', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

plt.savefig("./fig/certificados.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()


############ Areas de trabajo de empleados ############
areas_de_desempenio = np.array(areas_de_desempenio)

areas_set, areas_count = np.unique(areas_de_desempenio, return_counts=True)

areas_pro = (areas_count / len(empleados_de_bancos)) * 100

areas_df = pd.DataFrame({
    'Areas': areas_set,
    'Porcentaje': areas_pro
    })
areas_df = areas_df.drop(labels=0, axis=0)

fig, ax = plt.subplots()
ax.bar('Areas', 'Porcentaje', data=areas_df, color=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray', 'tab:green', 'tab:purple', 'tab:pink', 'm'])

plt.tick_params(
    axis='x',        
    which='both',   
    bottom=False,  
    top=False,    
    labelbottom=False)

plt.title("Areas de desempeño de empleados")

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(areas_df['Areas'].tolist(), ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red', 'tab:gray', 'tab:green', 'tab:purple', 'tab:pink', 'm']))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=areas_df['Areas'].tolist(), handles=patches, title='Areas', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

plt.savefig("./fig/areas_de_desempenio.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()























