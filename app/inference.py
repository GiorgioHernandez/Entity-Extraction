from unstructured.partition.pdf import partition_pdf_or_image
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from langchain.output_parsers.json import SimpleJsonOutputParser

from fastapi import UploadFile
from app.schemas.fields import SchemaOut

import os
from io import BytesIO
from enum import Enum
from typing import get_args

class Process: 

    def __init__(self): 
        
        os.environ["OPENAI_API_KEY"] = "" #enter API Key
        self.model = ChatOpenAI(
            model = "gpt-3.5-turbo",
            temperature = 0
        )
    
    async def data_unstructured(self, file:UploadFile):

        if str(file.filename).endswith(('PDF','pdf')):
            is_image = False
        else: 
            is_image = True

        # Get elements
        contents = await file.read()
        raw_pdf_elements = partition_pdf_or_image(
            is_image=is_image,
            # filename=str(path_file),
            file= BytesIO(contents),
            languages=['spa'],
            infer_table_structure=True,
            strategy='hi_res',
        )

        text = ""
        for el in raw_pdf_elements:
            if el.category == "Table":
                text += el.metadata.text_as_html + "\n"
            elif el.category in ["Title","ListItem","NarrativeText","UncategorizedText", "Image", "FigureCaption"]:
                text += el.text + "\n"

        return text
        
    async def inference(self, text):
        schema = SchemaOut()
        schema_json = schema.model_json_schema()

        keys = ""
        for field_name, field_info in schema_json.get('properties', {}).items():
            
            field_type = schema.__annotations__.get(field_name)
            field_type = get_args(field_type)[0]

            default_value = field_info.get('default', 'No default value')
            description = field_info.get('description', 'No description available')
            
            if issubclass(field_type, Enum):
                enum_options = [e.value for e in field_type]
                default_value = field_info.get('default', 'No default value')
                keys += f"{field_name}; descripción: {description}; opciones de respuesta: {enum_options}. En caso de no encontrar la información en el texto, el valor por defecto es: {default_value}\n\n"
            else:
                keys += f"{field_name}; descripción: {description}. En caso de no encontrar la información en el texto, el valor por defecto es: {default_value}\n\n"


        template = """Nombre de las entidades a extraer, su respectiva descripción y en caso que aplique, las opciones de respuesta:
            {keys}
            Instrucciones: Extrae las entidades, en formato JSON, a partir del texto:
            {text}
            """

        prompt = PromptTemplate(
            template=template,
            input_variables=["keys","text"],
        )

        json_parser = SimpleJsonOutputParser()
        with get_openai_callback() as cb:
            chain = prompt | self.model | json_parser
            response = await chain.ainvoke({"keys":keys,"text": text})
            cost = cb.total_cost

        return response, cost
    


