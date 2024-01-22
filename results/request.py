import requests
import json
import os
from pathlib import Path

src = "./data" # configurar ruta donde están los archivos.
path = [p for p in Path(src).glob('*/*') if p.suffix in ('.pdf','.PDF','.JPEG', '.jpeg', '.jpg','.png')]

print(f'Cantidad de muestras: {len(path)}\n\n')

# se crea directorio donde se guardarán las respuestas. 
directorio = "./results/json"
if not os.path.exists(directorio):
    os.mkdir(directorio)
else:
    print(f"El directorio '{directorio}' ya existe.")

for i, p in enumerate(path): 
    print(f'Processing ... {str(p)} - {i}')

    response = requests.post(
        'http://0.0.0.0:80/api/extraction', 
        headers={'accept': 'application/json'}, 
        files={'file': (str(p), open(str(p), 'rb'), 'application/pdf')}
        )
    if response.status_code == 200:
        filename = p.name[:-4]
        response = json.loads(response.text)
        
        with open(f'{directorio}/{filename}.json', 'w', encoding='utf-8') as f:
            json.dump(response, f, ensure_ascii=False, indent=4)
        print('Successfully processed.\n\n')
    else: 
        print(f'No procesable {str(p)} - {i}\n\n')