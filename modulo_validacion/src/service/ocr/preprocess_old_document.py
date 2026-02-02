import re 
from typing import List
from datetime import date
class PreprocessingOldDocument:

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


        def parse_to_date(date_str:str):

            MONTH_MAP = {
                "ene": "01",
                "feb": "02",
                "mar": "03",
                "abr": "04",
                "may": "05",
                "jun": "06",
                "jul": "07",
                "ago": "08",
                "sep": "09",
                "oct": "10",
                "nov": "11",
                "dic": "12"
            }


            day = int(date_str[0:2])
            month = date_str[2:5]
            year = int(date_str[5:])

            return date(year, int(MONTH_MAP[month]), day) 
      
        DATE_WITH_TEXT_MONTH = re.compile(
            r'''
            \b
            \d{1,2}                    # día
            [\s\-\+/]*                 # separador OCR sucio
            (ene|feb|mar|abr|may|jun|
            jul|ago|sep|oct|nov|dic)  # mes en letras
            [\s\-\+/]*                 # separador
            \d{4}                      # año
            \b
            ''',
            re.IGNORECASE | re.VERBOSE
        )


        DATE_TEXT_MONTH_COMPACT = re.compile(
            r'\b\d{1,2}(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)\d{4}\b',
            re.IGNORECASE
        )

        lower_text = self.reverse_content.lower()
        splited_text = lower_text.split('\n')

        
        date_detected = [ item for item in splited_text if DATE_WITH_TEXT_MONTH.search(item)]

        date_without_symbols_detected = [
            item.replace('+','').replace('-','')
            for item in date_detected
            if DATE_TEXT_MONTH_COMPACT.search(item.replace('+','').replace('-',''))
        ]

        final_date_detected = [re.search(DATE_TEXT_MONTH_COMPACT, item).group() for item in date_without_symbols_detected]

        parsed_date = [parse_to_date(date_str=item) for item in final_date_detected]

        
        if len(parsed_date) == 2:
            date_issue_from_reverse = parsed_date[1]
            return date_issue_from_reverse
        
        if len(parsed_date) == 1:
            date_issue_from_reverse = parsed_date[0]
            return date_issue_from_reverse