import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Patch
import pandas as pd
from instrumento import Instrumento

from make_bar import make_bar

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

# Interés en el sector banacario
interes_estudiates = []
interes_para_trabajar = []

# Adquisición de conocimientos
lenguajes_progra = []
conocimientos_tecnicos_generales = []
bases_de_datos = []
sistemas_operativos = []

# Area de interes
area_interes = []

# Lneguajes de programación que dominan
java = []
csharp = []
js = []
python = []
cpp = []
php = []

# Patrones de diseño
patrones = []

# Gestores de bases de datos
oracle = []
server = []
mysql = []
postgres = []
mongo = []
maria = []
db2 = []

# Diseño de bases
bases_disenio = []

# Sistemas Operativos que domina
sistema_domi = []

# Interés para trabajar en el sector bancario
interes_trabajar_en_el_sector = []

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

# Habilidades tecnicas necesarias
habilidades_necesarias = []


# Gestores de bases de datos
gestores_bd = []

# Empleados con certificados
empleados_crt = []
certificados = []

# Bases de datos mas usdadas
bases_mas_usadas = []

# Sistemas operativos mas usados
so_usados = []

# Lenguajes mas usados
lenguajes_usados = []
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

    #Interés en el sector bancario
    interes_estudiates.append(individuo["¿Qué tanto le interesa trabajar en el sector bancario?"])
    interes_para_trabajar.append(individuo["Al momento de buscar empleo ¿qué le interesa más?"])

    # Adquisición de conocimientos
    lenguajes_progra = lenguajes_progra + individuo["¿Cómo ha adquirido sus conocimientos en los lenguajes de programación preguntados anteriormente?\xa0\xa0\xa0(Puede escoger más de una opción)"].split(";")
    conocimientos_tecnicos_generales = conocimientos_tecnicos_generales + individuo["¿Cómo ha adquirido sus conocimientos sobre los conceptos de la pregunta anterior?\xa0(Puede escoger más de una opción)"].split(";")
    bases_de_datos = bases_de_datos + individuo["¿Cómo ha adquirido sus conocimientos en los gestores de base de datos preguntados anteriormente?\xa0\xa0(Puede escoger más de una opción)"].split(";")
    sistemas_operativos = sistemas_operativos + individuo["¿Cómo ha adquirido sus conocimientos en los sistemas operativos de la pregunta anterior?\xa0(Puede escoger más de una opción)"].split(";")

    # Area de interes
    area_interes = area_interes + individuo["¿En cuáles de las siguientes áreas de Ingeniería en Sistemas tiene mayor interés?\xa0\xa0(Puede escoger más de una opción)"].split(";")

    # lenguajes que domina
    java.append(individuo["Java"])
    csharp.append(individuo["C#"])
    js.append(individuo["JavaScript"])
    python.append(individuo["Python"])
    cpp.append(individuo["C++"])
    php.append(individuo["PHP"])

    # Patrones de diseño
    patrones = patrones + individuo["De los siguientes patrones de diseño de software seleccione cuáles conoce:\xa0\xa0(Puede escoger más de una opción)"].split(";")

    # Gestores 
    oracle.append(individuo["Oracle"])
    server.append(individuo["SQL Server"])
    mysql.append(individuo["MySQL"])
    postgres.append(individuo["PostgreSQL"])
    mongo.append(individuo["MongoDB"])
    maria.append(individuo["MariaDB"])
    db2.append(individuo["Db2"])

    # Diseño bd
    bases_disenio = bases_disenio + individuo["Al momento de diseñar una base de datos, ¿Cuáles de los siguientes principios utiliza?\xa0\xa0(Puede escoger más de una opción)"].split(";")

    # Sistemas operativos
    sistema_domi = sistema_domi + individuo["¿Cuáles de los siguientes sistemas operativos sabe usar?\xa0\xa0(Puede escoger más de una opción)"].split(";")

    # Interés para trabajar en el sector bancario
    interes_trabajar_en_el_sector.append(individuo["¿Qué tanto le interesa trabajar en el sector bancario?"])


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

    # Áreas de desempeño
    areas_de_desempenio = areas_de_desempenio + individuo["¿En qué área se desempeña o desempeñó en el sector bancario?\xa0\xa0(Puede escoger más de una opción)"].split(";")

    #Habilidades requeridas
    habilidades_necesarias = habilidades_necesarias + individuo["¿Qué habilidades o requisitos necesitó para comenzar a laborar en una entidad bancaria?\xa0(Puede escoger más de una opción)"].split(";")

    #Gestores de bases de datos
    gestores_bd = gestores_bd + individuo["Según su experiencia, ¿qué gestores de base de datos debe conocer un ingeniero en sistemas para laborar en una entidad bancaria? (Puede escoger más de una opción)"].split(";")

    #Sistemas Operativos
    so_usados = so_usados + individuo["Según su experiencia, ¿qué sistemas operativos debe saber utilizar un ingeniero en sistemas para poder laborar en una entidad bancaria?\xa0\xa0(Puede escoger más de una opción)"].split(";")

    #Lenguajes de programación
    lenguajes_usados = lenguajes_usados + individuo["Según su experiencia, ¿qué lenguajes de programación debe conocer un ingeniero en sistemas para poder laborar en una entidad bancaria?\xa0(Puede escoger más de una opción)"].split(";")


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

# Grafica estudiantes
make_bar(
        data=nombre_habilidades,
        por=promedios_habilidades_es,
        title="Importancia de Habilidades blandas que poseen los estudiantes de Ingeniería en Sistemas\n",
        file_name="./fig/habilidades_blandas_es.png",
        range=True,
        name="Habilidades",
        ylabel="Nivel de importancia"
        )


# Grafica empleados
make_bar(
        data=nombre_habilidades,
        por=promedios_habilidades_bc,
        title="Importancia de Habilidades blandas requeridas en el sector bancario\n",
        file_name="./fig/habilidades_blandas_bc.png",
        range=True,
        name="Habilidades",
        ylabel="Nivel de importancia"
        )

############## Tecnologias y Frecuencia ##############

# Estudiantes
fre_actualizacion_tec_conocidas_es = np.array(fre_actualizacion_tec_conocidas_es)
fre_aprendizaje_nueva_tec_es = np.array(fre_aprendizaje_nueva_tec_es)

fre_act_set_es, frecuencia_act_es = np.unique(fre_actualizacion_tec_conocidas_es, return_counts=True)
fre_apr_set_es, frecuencia_apr_es = np.unique(fre_aprendizaje_nueva_tec_es, return_counts=True)

frecuencia_act_es = (frecuencia_act_es / len(estudiantes)) * 100
frecuencia_apr_es = (frecuencia_apr_es / len(estudiantes)) * 100

interes_trabajar_en_el_sector = np.array(interes_trabajar_en_el_sector)
interes_sec_set, interes_sec_por = np.unique(interes_trabajar_en_el_sector, return_counts=True)
interes_sec_por = (interes_sec_por / len(estudiantes)) * 100

# Interés para trabajar en el sector bancario
fig, ax = plt.subplots()
ax.pie(interes_sec_por, colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red'], autopct='%.0f%%')
plt.title("Interés que tienen los estudiantes para trabajar en el sector bancario")

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(interes_sec_set, ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red']))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=interes_sec_set.tolist(), handles=patches, title='Interés', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)


plt.savefig("./fig/interes_trabajar_en_sector.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()

# Frecuencia actualización
fig, ax = plt.subplots()

ax.pie(frecuencia_act_es, colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red'], autopct='%.0f%%')
plt.title("Frecuencia de actualización de conocimientos técnicos \n de estudiantes por egresar de Ingeniería en Sistemas \n en la UNAH")

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(fre_act_set_es, ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red']))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=fre_act_set_es.tolist(), handles=patches, title='Frecuencia', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)


plt.savefig("./fig/actualizacion_de_conocimientos_es.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()

# Frecuencia aprendizaje
fig, ax = plt.subplots()

ax.pie(frecuencia_apr_es, colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red'], autopct='%.0f%%')
plt.title("Frecuencia de aprendizaje de nuevos conocimientos técnicos \n de estudiantes por egresar de Ingeniería en Sistemas \n en la UNAH")

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(fre_apr_set_es, ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red']))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=fre_apr_set_es.tolist(), handles=patches, title='Frecuencia', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)


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

ax.pie(frecuencia_act_bc, colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red'], autopct='%.0f%%')
plt.title("Frecuencia de actualización de conocimientos técnicos \n de empleados del sector bancario")

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(fre_act_set_bc, ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red']))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=fre_act_set_bc.tolist(), handles=patches, title='Frecuencia', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

plt.savefig("./fig/actualizacion_de_conocimientos_bc.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()

# Frecuencia aprendizaje
fig, ax = plt.subplots()

ax.pie(frecuencia_apr_bc, colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red'], autopct='%.0f%%')
plt.title("Frecuencia de aprendizaje de nuevos conocimientos técnicos \n de empleados del sector bancario")

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(fre_apr_set_bc, ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red']))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=fre_apr_set_bc.tolist(), handles=patches, title='Frecuencia', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)


plt.savefig("./fig/aprendizaje_de_conocimientos_bc.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
plt.clf()


############ Interés de los estudiantes en el sector banacario ############
interes_estudiates = np.array(interes_estudiates)


############ Interés de los estudiantes para trabajar en el sector banacario ############
interes_para_trabajar = np.array(interes_para_trabajar)
interes_set, fre_interes = np.unique(interes_para_trabajar, return_counts=True) 

fre_interes = (fre_interes / len(estudiantes)) * 100

fig, ax = plt.subplots()
ax.pie(fre_interes, colors=['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red'], autopct='%.0f%%' )

plt.title("Interés de los estudiantes en un empleo")

fontP = FontProperties()
fontP.set_size('small')

cmap = dict(zip(interes_set, ['tab:blue', 'tab:cyan', 'tab:orange', 'tab:red']))

patches = [Patch(color=v, label=k) for k, v in cmap.items()]

plt.legend(labels=interes_set.tolist(), handles=patches, title='Interés', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)

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

centros_df = centros_df.sort_values('Porcentaje', ascending=False)

make_bar(
        data=centros_df['Centros'].tolist(),
        por=centros_df['Porcentaje'].tolist(),
        title="Universidades en las que estudiaron los empleados",
        name="Universidades",
        file_name="./fig/centros_de_estudio.png",
        ylabel="Porcentaje de población"
        )

############ Centros de trabajo de los empleados de bancos ############
bancos_laborados = np.array(bancos_laborados)
bancos_set, fre_bancos = np.unique(bancos_laborados, return_counts=True)

fre_bancos = (fre_bancos / len(empleados_de_bancos)) * 100

bancos_df = pd.DataFrame({
    'Bancos': bancos_set,
    'Porcentaje': fre_bancos
    })

bancos_df = bancos_df.drop(labels=0, axis=0)

bancos_df = bancos_df.sort_values('Porcentaje', ascending=False)

make_bar(
        data=bancos_df['Bancos'].tolist(),
        por=bancos_df['Porcentaje'].tolist(),
        title="Bancos en los que han trabajado los empleados",
        name="Bancos",
        file_name="./fig/bancos_laborados.png",
        ylabel="Porcentaje de población"
        )

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
make_bar(
        data=totales_df['Totales_adq'].tolist(),
        por=totales_df['Porcentaje'].tolist(),
        title="Adquisición de conocimientos tecnicos totales",
        name="Adquisición",
        file_name="./fig/totales_adq.png",
        ylabel="Porcentaje de población"
        )

############ Certificaciones de empleados ############
certificados = np.array(certificados)

certificados_set, certificados_count = np.unique(certificados, return_counts=True)

certificados_pro = (certificados_count / len(empleados_crt)) * 100

make_bar(
        data=certificados_set,
        por=certificados_pro,
        title="Certificaciones de los empleados",
        name="Certificados",
        file_name="./fig/certificados.png",
        drop_df=True,
        ylabel="Porcentaje de población"
        )

############ Áreas de trabajo de empleados ############
areas_de_desempenio = np.array(areas_de_desempenio)

areas_set, areas_count = np.unique(areas_de_desempenio, return_counts=True)

areas_pro = (areas_count / len(empleados_de_bancos)) * 100

make_bar(
        data=areas_set,
        por=areas_pro,
        title="Áreas de desempeño de empleados",
        name="Áreas",
        file_name="./fig/areas_de_desempenio.png",
        drop_df=True,
        ylabel="Porcentaje de población"
        )

############ Habilidades necesarias ############
habilidades_necesarias = np.array(habilidades_necesarias)

habilidades_set, habilidades_count = np.unique(habilidades_necesarias, return_counts=True)

hab_pro = (habilidades_count / len(empleados_de_bancos)) * 100

make_bar(
        data=habilidades_set,
        por=hab_pro,
        title="Habilidades necesarias para trabajar en el sector",
        name="Habilidades",
        file_name="./fig/habilidades_necesarias.png",
        drop_df=True,
        ylabel="Porcentaje de población"
        )

############ Gestores de bases de datos usados ############
gestores_bd = np.array(gestores_bd)

gestores_set, gestores_count = np.unique(gestores_bd, return_counts=True)

gestores_pro = (gestores_count / len(empleados_de_bancos)) * 100

make_bar(
        data=gestores_set,
        por=gestores_pro,
        title="Gestores necesarios",
        name="Gestores",
        file_name="./fig/gestores_bd.png",
        drop_df=True,
        ylabel="Porcentaje de población"
        )


############ Sistemas operativos que saben usar los empleados ############

so_usados = np.array(so_usados)

so_set, so_count = np.unique(so_usados, return_counts=True)

so_pro = (so_count / len(empleados_de_bancos)) * 100

make_bar(
        data=so_set,
        por=so_pro,
        title="Sistemas operativos",
        name="SO",
        file_name="./fig/so_usados.png",
        drop_df=True,
        ylabel="Porcentaje de población"
        )
############ Lenguajes de programación que saben usar los empleados ############

lenguajes_usados = np.array(lenguajes_usados)

so_set, so_count = np.unique(lenguajes_usados, return_counts=True)

so_pro = (so_count / len(empleados_de_bancos)) * 100

make_bar(
        data=so_set,
        por=so_pro,
        title="Lenguajes de programación usados",
        name="Lenguajes",
        file_name="./fig/lenguajes_usados.png",
        drop_df=True,
        ylabel="Porcentaje de población"
        )

############ Áreas de interes para los estudiantes ############

area_interes = np.array(area_interes)

so_set, so_count = np.unique(area_interes, return_counts=True)

so_pro = (so_count / len(estudiantes)) * 100

make_bar(
        data=so_set,
        por=so_pro,
        title="Áreas de interés para los estudiantes",
        name="Áreas",
        file_name="./fig/areas_interes.png",
        drop_df=True,
        ylabel="Porcentaje de población"
        )

############ Lenguajes de programación que dominan los estudiantes ############

java = np.array(java)
csharp = np.array(csharp)
js = np.array(js)
python = np.array(python)
cpp = np.array(cpp)
php = np.array(php)

### Lenguajes obtenidos "a mano" de la opción de otros
typescript = [0]*len(estudiantes)
go = [0]*len(estudiantes)
r = [0]*len(estudiantes)
sh = [0]*len(estudiantes)

typescript[0] = 4

go[0] = 2
go[1] = 3
go[2] = 4

r[0] = 3

sh[0] = 2

typescript = np.array(typescript)
go = np.array(go)
r = np.array(r)
sh = np.array(sh)

lenguajes = ["Java","C#","JavaScript","Python","C++", "PHP", "TypeScript", "GO", "R", "SH"]
lenguajes_pro = [np.mean(java), np.mean(csharp), np.mean(js), np.mean(python), np.mean(cpp), np.mean(php), np.mean(typescript), np.mean(go), np.mean(r), np.mean(sh)]

make_bar(
        data=lenguajes,
        por=lenguajes_pro,
        title="Lenguaes de Programación que los estudiantes dominan",
        name="Lenguajes",
        file_name="./fig/lenguajes_domi.png",
        range=True,
        ylabel="Nivel de dominio"
        )

############ Patrones de diseño ############

area_interes = np.array(patrones)

so_set, so_count = np.unique(area_interes, return_counts=True)

so_pro = (so_count / len(estudiantes)) * 100

make_bar(
        data=so_set,
        por=so_pro,
        title="Patrones de diseño que conocen los estudiantes",
        name="Patrones",
        file_name="./fig/patrones_disenio.png",
        drop_df=True,
        ylabel="Porcentaje de población"
        )

############ Gestores de bases de datos que dominan los estudiantes ############

oracle = np.array(oracle)
server = np.array(server)
mysql = np.array(mysql)
postgres = np.array(postgres)
mongo = np.array(mongo)
maria = np.array(maria)
db2 = np.array(db2)

lenguajes = ["Oracle","SQL Server","MySQL","PostgreSQL","MongoDB", "MariaDB", "DB2"]
lenguajes_pro = [np.mean(oracle), np.mean(server), np.mean(mysql), np.mean(postgres), np.mean(mongo), np.mean(maria), np.mean(db2)]

make_bar(
        data=lenguajes,
        por=lenguajes_pro,
        title="Gestores de bases de datos que dominan los estudiantes\n",
        name="Gestores",
        file_name="./fig/gestores_domi.png",
        range=True,
        ylabel="Nivel de dominio"
        )

############ Diseño de bases de datos ############

area_interes = np.array(bases_disenio)

so_set, so_count = np.unique(area_interes, return_counts=True)

so_pro = (so_count / len(estudiantes)) * 100

make_bar(
        data=so_set,
        por=so_pro,
        title="Diseño de bases de datos",
        name="Diseño",
        file_name="./fig/bases_disenio.png",
        drop_df=True,
        ylabel="Porcentaje de población"
        )

############ Diseño de bases de datos ############

area_interes = np.array(sistema_domi)

so_set, so_count = np.unique(area_interes, return_counts=True)

so_pro = (so_count / len(estudiantes)) * 100

make_bar(
        data=so_set,
        por=so_pro,
        title="Sistemas operativos que dominan los estudiantes",
        name="Sistemas Operativos",
        file_name="./fig/sistema_domi.png",
        drop_df=True,
        ylabel="Porcentaje de población"
        )













