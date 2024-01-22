from enum import Enum


class TypeID(Enum): 
    cc = "Cédula de Ciudadanía (CC)"
    nit = "Número de Identificación Tributaria (NIT)"
    ti = "Tarjeta de Identidad (TI)"

class Domicilio(Enum):
    si = "Si"
    no = "No"
    none = "Sin información"

class Area(Enum):
    psicoligia = "psicologia"
    fonoaudiologia = "fonoaudiologia"
    terapia_fisica = "terapia fisica"
    terapiaocupacional = "terapia ocupacional"
    none = "Sin información"

class Convenio(Enum):
    ecopetrol = "ECOPETROL SA"
    sanitas = "SANITAS"
    colsanitas = "COMPANIA DE MEDICINA PREPAGADA COLSANITAS SA"
    allianz = "ALLIANZ"
    particulares = "PARTICULARES"
    sura = "SURA"
    servisalud = "UNION TEMPORAL SERVISALUD SAN JOSE"
    medplus_cereza = "MEDPLUS CEREZA"
    medisanitas = "MEDISANITAS SAS COMPANIA DE MEDICINA PREPAGADA"
    medplus_cafes = "MEDPLUS CAFES"
    seguro_bolivar = "SEGUROS BOLIVAR"
    fundacion_salvador = "FUNDACION SALVADOR DE SUENOS"
    medplus_celeste = "MEDPLUS CELESTE"
    famisanar = "FAMISANAR"
    medplus_turquesa = "MEDPLUS TURQUESA"
    medplus_selecto_joven = "MEDPLUS SELECTO JOVEN"
    medplus_medicina_prepagada = "MEDPLUS MEDICINA PREPAGADA SA"
    aliansalud_eps = "ALIANSA EPS"
    mapfre = "MAPFRE"
    none = "Sin información"

class RemitidoA(Enum):
    riie = "RIIE"

class Medicos(Enum):
    ALVARO_BURBANO = 'Alvaro Burbano'
    ANA_CAROLINA_MONTAFIEZ_JIMENEZ = 'Ana Carolina Montañez Jimenez'
    ANDREA_HELENO = 'Andrea Heleno'
    B_DUSSAN = 'B Dussán'
    CARLOS_ALDANA_PATIFIO = 'Carlos Aldana Patiño'
    CARMEN_ALICIA_ULLOA_PINTO = 'Carmen Alicia Ulloa Pinto’'
    CAROLINA_RAMIREZ = 'Carolina Ramirez'
    CATALINA_SALAZAR = 'Catalina Salazar'
    ELENA_ROSADO_ACOSTA = 'Elena Rosado Acosta'
    GUILLERMO_BONILLA = 'Guillermo Bonilla'
    HARRISON_BARON = 'Harrison Barón'
    JANNETT_INES_ACOSTA_ECHEVERRIA = 'Jannett Ines Acosta Echeverria'
    JAVIER_MAURICIO_GUTIERREZ_BLANCO = 'Javier Mauricio Gutierrez Blanco'
    JOHANNA_MARCELA_MARTINEZ_RAMIREZ = 'Johanna Marcela Martinez Ramirez'
    LILIANA_IVONNE_CAICEDO_RAMIREZ = 'Liliana Ivonne Caicedo Ramirez'
    LILIANA_MARIA_CORREA_OSPINA = 'Liliana Maria Correa Ospina'
    LUIS_ALFONSO_CASTELBLANCO_MEJIA = 'Luis Alfonso Castelblanco Mejia'
    MARGARITA_MARIA_VARGAS_DONOSO = 'Margarita María Vargas Donoso'
    MARIA_CLEMENCIA_RUIZ_DE_CIFUENTES = 'Maria Clemencia Ruiz de Cifuentes'
    MARIA_CRISTINA_ANGULO = 'Maria Cristina Angulo'
    MARIA_FERNANDA_LEON_PEREZ = 'Maria Fernanda Leon Perez'
    MARTHA_SANCHEZ_DE_FRISZ = 'Martha Sanchez de Frisz'
    MERCEDES_YAMILE_CABRERA_QUINTANA = 'Mercedes Yamile Cabrera Quintana'
    MILENA_OLMOS = 'Milena Olmos'
    NATALIA_PINZEN = 'Natalia Pinzón'
    NAYITA_ALARCON_BALLESTEROS = 'Nayita Alarcon Ballesteros'
    RICARDO_SALCEDO = 'Ricardo Salcedo'
    RUTH_ARMENTA_POLO = 'Ruth Armenta Polo'
    TERESITA_DE_JESUS_MEZA_CABALLERO = 'Teresita de Jesus Meza Caballero'
    TULIA_INES_GUERRA_PINEDA = 'Tulia Ines Guerra Pineda'
