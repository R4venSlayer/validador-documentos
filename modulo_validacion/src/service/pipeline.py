
from PIL import Image
from pathlib import Path
from django.conf import settings
from django.core.files.uploadedfile import UploadedFile
import re
from typing import List, Dict
from datetime import date

from uuid import uuid4

from ..infrastructure.file_manager import crear_carpeta, guardar_imagen
from ..infrastructure.ocr_reader import read_img_process
from .preprocess_document import classify_document, exec_preprocess

def pipeline_save_pictures(archivos:Dict):
    
    uuid_process = str(uuid4())
    carpeta_documento = Path(settings.MEDIA_ROOT, "documentos" , uuid_process) 
    
    crear_carpeta(ruta=carpeta_documento)
    
    for key, value in archivos.items():
        guardar_imagen(archivo=value, carpeta_destino=carpeta_documento, nombre_archivo=key)

    return carpeta_documento


def pipeline_extract_text_from_img(folder_items:Path):
    
    file_item_list = list(folder_items.iterdir())

    txt_extracted_dictionary = {}

    for item in file_item_list:
        txt_extracted_dictionary[item.name.split('.')[0]] = read_img_process(ruta_archivo=item) 

    return txt_extracted_dictionary


def preprocess_info_from_imgs(content_dictionary: Dict):

    # Paso 1. Clasificar por cédula nueva o cédula antigua

    state_document = classify_document(reverse_content=content_dictionary["reverso"])

    # Paso 2. Ejecutar la extracción de información dependiendo del documento detectado (nuevo "True" o antiguo "False")
    data = exec_preprocess(is_new_document=state_document, content=content_dictionary)

    return data

def compare_id_fields(num_documento_endpoint:str, num_documento_extracted:str):
    return num_documento_extracted == num_documento_endpoint

def pipeline_validate_document_id(num_documento_value: str,  foto_frontal: UploadedFile, foto_reverso: UploadedFile):

    archivos_dict = {
        "frontal": foto_frontal,
        "reverso": foto_reverso
    }

    carpeta_destino = pipeline_save_pictures(archivos = archivos_dict)

    results_from_images = pipeline_extract_text_from_img(carpeta_destino)

    data = preprocess_info_from_imgs(content_dictionary=results_from_images)

    # Se comparan los números de documentos
    flag = compare_id_fields(num_documento_endpoint = num_documento_value, num_documento_extracted = data["num_documento"])
    
    if flag:
        validate_state = True
        return data, validate_state
    
    elif not flag:
        validate_state = True
        return data, validate_state


# def pipeline_validate_document_id(
#     num_documento_value: str,
#     foto_frontal: UploadedFile,
#     foto_reverso: UploadedFile
# ) -> dict:
#     """
#     Pipeline:
#     - crea carpeta por número de documento
#     - guarda imagen frontal y reverso
#     - ejecuta OCR en ambas
#     - retorna texto extraído
#     """


    



#     # 3️⃣ Guardar imagen reverso
#     ext_reverso = Path(foto_reverso.name).suffix
#     ruta_reverso = carpeta_documento / f"reverso{ext_reverso}"

#     with ruta_reverso.open("wb+") as destino:
#         for chunk in foto_reverso.chunks():
#             destino.write(chunk)




#     pipeline_foto_frontal(texto_frontal)

#     return {
#         "num_documento_esperado": num_documento_value,
#         "texto_frontal": texto_frontal.lower(),
#         "texto_reverso": texto_reverso.lower(),
#         "frontal_path": str(ruta_frontal),
#         "reverso_path": str(ruta_reverso),
#     }



# def pipeline_foto_frontal(texto_frontal:str):
    

#     # Se separa por el cáracter \n

#     texto_minusc = texto_frontal.lower()
#     texto_separado = texto_minusc.split('\n')

    
#     def indices_fechas_y_anios(arr: List[str]) -> List[int]:
#         """
#         Retorna los índices que contienen:
#         - fechas tipo: 02 abr 1981
#         - o años sueltos: 2010, 2020
#         """

#         texto_minusc = texto_frontal.lower()
#         texto_separado = texto_minusc.split('\n')

#         patron_fecha = re.compile(
#             r'(0[1-9]|[12][0-9]|3[01])\s*[-]?\s*'
#             r'(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)\s+'
#             r'(19|20)\d{2}'
#         )

#         patron_anio = re.compile(r'\b(19|20)\d{2}\b')

#         encontrados = [
#             linea.strip()
#             for linea in texto_separado
#             if patron_fecha.search(linea) or patron_anio.search(linea)
#         ]

#         return encontrados

#     fecha_separated = indices_fechas_y_anios (arr=texto_separado)


#     def extraer_fechas_y_anios(arr: List[str]) -> List[str]:
#         """
#         Extrae únicamente los fragmentos que cumplen con:
#         - fecha completa: 02 abr 1981
#         - mes + año (OCR): ene 2032
#         - día + mes + año con ruido previo
#         """

#         patron_fecha = re.compile(
#             r'(0[1-9]|[12][0-9]|3[01])\s*[-]?\s*'
#             r'(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)\s+'
#             r'(19|20)\d{2}'
#         )

#         patron_mes_anio = re.compile(
#             r'(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)\s+'
#             r'(19|20)\d{2}'
#         )

#         resultados = []

#         for linea in arr:
#             # 1️⃣ Fecha completa
#             for match in patron_fecha.finditer(linea):
#                 resultados.append(match.group(0))

#             # 2️⃣ Mes + año (si no hubo fecha completa)
#             if not patron_fecha.search(linea):
#                 for match in patron_mes_anio.finditer(linea):
#                     resultados.append(match.group(0))

#         return resultados

#     fechas_extraidas = extraer_fechas_y_anios(arr=fecha_separated)


#     MESES_ES = {
#         "ene": 1,
#         "feb": 2,
#         "mar": 3,
#         "abr": 4,
#         "may": 5,
#         "jun": 6,
#         "jul": 7,
#         "ago": 8,
#         "sep": 9,
#         "oct": 10,
#         "nov": 11,
#         "dic": 12,
#     }

#     def convertir_fechas_a_date(fechas: List[str]) -> List[date]:
#         """
#         Convierte strings tipo:
#         - '02 abr 1981' -> date(1981, 4, 2)
#         - 'ene 2032'    -> date(2032, 1, 1)
#         """

#         resultados: List[date] = []

#         for f in fechas:
#             partes = f.split()

#             try:
#                 # Caso: dd mes yyyy
#                 if len(partes) == 3:
#                     dia = int(partes[0])
#                     mes = MESES_ES.get(partes[1])
#                     anio = int(partes[2])

#                     if mes:
#                         resultados.append(date(anio, mes, dia))

#                 # Caso: mes yyyy
#                 elif len(partes) == 2:
#                     mes = MESES_ES.get(partes[0])
#                     anio = int(partes[1])

#                     if mes:
#                         # decisión explícita: día = 1
#                         resultados.append(date(anio, mes, 1))

#             except ValueError:
#                 # fecha inválida (ej. 31 feb)
#                 continue

#         return resultados
    

#     fechas_convert = convertir_fechas_a_date(fechas=fechas_extraidas)

#     print(fechas_convert)







