from .preprocess_old_document import PreprocessingOldDocument
from typing import Dict

def classify_document(reverse_content:str):

    """
    Docstring for classify_document
    
    Método encargado de clasificar el tipo de documento

    (tarjeta nueva o tarjeta antigua)

    :param reverse_content: Texto extraído de la parte al reverso del documento cargado
    :type reverse_content: str
    """

    if ("<<" in reverse_content) or ("<<<" in reverse_content):
        return True

    return  False

def exec_preprocess(is_new_document:bool, content:Dict):

    if is_new_document:
        ...
    
    elif not is_new_document :
        preprocess = PreprocessingOldDocument(front_content=content["frontal"], reverse_content=content["reverso"])
        preprocess.exec_preprocess()
