
from PIL import Image
from pathlib import Path
from django.conf import settings
from django.core.files.uploadedfile import UploadedFile
import re
from typing import List, Dict
from datetime import date

from uuid import uuid4

from ...infrastructure.file_manager import crear_carpeta, guardar_imagen
from ...infrastructure.ocr_reader import read_img_process
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
   
    preprocess_info_from_imgs(content_dictionary=results_from_images)
    
    data = preprocess_info_from_imgs(content_dictionary=results_from_images)

    if None in data.values():
        
        return data, None
     
    # Se comparan los números de documentos
    flag = compare_id_fields(num_documento_endpoint = num_documento_value, num_documento_extracted = data["num_documento"])

    if flag:
        validate_state = True
        return data, validate_state
    
    elif not flag:
        validate_state = False
        return data, validate_state









