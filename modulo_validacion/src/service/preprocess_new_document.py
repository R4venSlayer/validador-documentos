import re 
from typing import List
from datetime import date

class PreprocessingNewDocument:

    def __init__(self, front_content:str, reverse_content:str):
        self.front_content = front_content
        self.reverse_content = reverse_content
    
    def exec_preprocess(self):

        num_document_extracted = self.get_document_number()
        date_issue_extracted = self.get_date_issue()

        data_from_document = {
            "num_documento" : num_document_extracted,
            "fecha_expedicion" : date_issue_extracted
        }

        return data_from_document
    

    def get_document_number(self):

        lowered_text = self.front_content.lower()
        removed_symbols_text = lowered_text.replace(',','').replace('.','') 
        splited_text = removed_symbols_text.split('\n')

        # Se detecta la cadena que contiene un patrón que represente un documento
        document_detected = [ item for item in splited_text if re.search(r'\b\d{8,10}\b', item)]

        
        if len(document_detected) > 0:
            # Se extrae únicamente los números encontrados en la cadena encontrada previamente
            num_document_from_front = re.search(r'\d{8,10}', document_detected[0]).group()
            return num_document_from_front
                


    def get_document_number(self):
        
    
        # Se retiran . y , de la cadena extraída
        replaced_text = self.front_content.replace('.','').replace(',','')
        
        # Se separan los caractares por cada salto de línea
        splited_text = replaced_text.split('\n')
        
        # Se eliminan espacios entre las cadenas
        striped_items_text = [re.sub(r'(\d)\s+(\d)', r'\1\2', item).strip()for item in splited_text]
        
        # Se detecta la cadena que contiene un patrón que represente un documento
        document_detected = [ item for item in striped_items_text if re.search(r'\b\d{8,10}\b', item)]

        if len(document_detected) > 0:
            # Se extrae únicamente los números encontrados en la cadena encontrada previamente
            num_document_from_front = re.search(r'\d{8,10}', document_detected[0]).group()
            return num_document_from_front

        

    def get_date_issue(self):

        MONTH_MAP = {
            "ene": 1, "feb": 2, "mar": 3, "abr": 4,
            "may": 5, "jun": 6, "jul": 7, "ago": 8,
            "sep": 9, "oct": 10, "nov": 11, "dic": 12
        }

        DATE_WITH_TEXT_MONTH = re.compile(
            r'''
            (0?[1-9]|[12][0-9]|3[01])   # día
            \s*                        # espacios opcionales
            (ene|feb|mar|abr|may|jun|
            jul|ago|sep|oct|nov|dic)  # mes
            \s*                        # espacios opcionales
            (\d{4})                    # año
            ''',
            re.IGNORECASE | re.VERBOSE
        )
    

        text = self.front_content.lower()
        text = text.replace(',', '').replace('.', '')
        lines = text.split('\n')

        parsed_dates = []

        for line in lines:
            match = DATE_WITH_TEXT_MONTH.search(line)
            if match:
                day, month_text, year = match.groups()
                try:
                    parsed_dates.append(
                        date(
                            int(year),
                            MONTH_MAP[month_text],
                            int(day)
                        )
                    )
                except ValueError:
                    continue  # descarta fechas imposibles (ej: 43 ene 2032)

        # lógica de negocio: segunda fecha = expedición
        if len(parsed_dates) >= 2:
            return parsed_dates[1]

        return None