import pytesseract
from PIL import Image
from pathlib import Path

def read_img_process(ruta_archivo:Path):

    """
    Docstring for read_img_process
    
    Método utilizado para realizar la extracción de la imagen

    :param ruta_archivo: Ruta de la imagen
    :type ruta_archivo: Path
    
    """
    
    img = Image.open(ruta_archivo)
    txt_extracted = pytesseract.image_to_string( img )
    

    return txt_extracted