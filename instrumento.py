import pandas as pd

class Instrumento:

    def __init__(self):
        self.path = "./data/Intereses y oportunidades en el sector bancario de Honduras para Ingenieros en Sistemas (1-79).xlsx - Sheet1.tsv"

        data = pd.read_csv(self.path, sep="\t")
        df = pd.DataFrame(data)
        df = df.set_index("ID")

        dc = df.to_dict("records")

        self.estudiantes = []
        self.trabajadores_de_bancos = []

        for persona in dc:
            if persona["¿Actualmente se encuentra cursando la clase de Seminario de Investigación?"] == "Sí":
                self.estudiantes.append(persona)
            elif persona["¿Ha laborado o labora actualmente en una entidad bancaria?"] == "Sí":
                self.trabajadores_de_bancos.append(persona)

    def getData(self):
        return self.estudiantes, self.trabajadores_de_bancos




