import json
import os
import pandas as pd
from pathlib import Path

# Ruta de la carpeta que contiene los archivos JSON
directorio_json = './results/json'

path = [p for p in Path(directorio_json).glob('*') if p.suffix in ('.json')]

# Lista para almacenar los datos de los JSON
datos_json = []
for p in path:
    with open(p, "r", encoding='utf-8') as file:
        data = json.load(file)
        datos_json.append(data)


# Crear un DataFrame de pandas
df = pd.DataFrame(datos_json)
df = pd.concat([df.drop(['Fields'], axis=1), df['Fields'].apply(pd.Series)], axis=1)
df.to_csv(f'./results/report.csv', index=False, float_format='%.4f', decimal='.')