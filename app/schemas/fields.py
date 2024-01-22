from pydantic import BaseModel, Field, field_validator
from typing import Optional
from fastapi.encoders import jsonable_encoder
from app.schemas.enums import *


class SchemaOut(BaseModel):
    fecha_orden: Optional[str] = Field(
        description="Fecha en la que fue radicada la orden", 
        default="Sin información"
        )
    
    nombre_paciente: Optional[str] = Field(
        description="Nombre del paciente", 
        default="Sin información"
        )

    id_paciente: Optional[str] = Field(
        description="Número de identificación del paciente", 
        default="Sin información"
        )
    
    tipo_identidad: Optional[TypeID] = Field(
        description="Tipo de identificación del paciente", 
        default="CC"
        )    
    
    area: Optional[Area] = Field(
        description="El tipo de servicio médico", 
        default="Sin información"
        )
    
    cantidad_sesiones: Optional[int] = Field(
        description="Cantidad de sesiones o servicios médicos que se le realizan al paciente", 
        default=0
        )
    
    bool_domicilio : Optional[Domicilio] = Field(
        description="Indica si el servicio médico es a domicilio", 
        default="Si"
        )
    
    nombre_medico: Optional[Medicos] = Field(
        description="Nombre del médico o profesional de la salud. Puede a aparecer como 'Remitido por:'", 
        default="Sin información"
        )
    
    convenio: Optional[Convenio]= Field(
        description="Entidad que remite la orden", 
        default="ECOPETROL SA"
        )
    
    remitida_a: Optional[RemitidoA] = Field(
        description="A quién es dirigida la orden", 
        default="RIIE"
        )


    # @field_validator('fecha_orden', mode='before')
    # @classmethod
    # def normalize_tipo_identificacion(cls, value):
    #     value = value.replace(".", "")
    #     value = value.replace("/","")
    #     value = value.replace("-","")
    #     return value.strip()
        
    # def to_dict(self):
    #     return {
    #         'fecha_orden': self.fecha_orden,
    #         'paciente':jsonable_encoder(self.paciente),
    #         'area':jsonable_encoder(self.area),
    #         'sesiones':jsonable_encoder(self.sesiones),
    #         'nombre_medico':self.nombre_medico,
    #         'convenio':self.convenio,
    #         'remitida_a':self.remitida_a
    #     }
