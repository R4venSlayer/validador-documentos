import re 
class PreprocessingOldDocument:

    def __init__(self, front_content:str, reverse_content:str):
        self.front_content = front_content
        self.reverse_content = reverse_content
    
    def exec_preprocess(self):

        num_document_extracted = self.get_document_number()
        date_issue_extracted = self.get_date_issue()

    def get_document_number(self):
        
    
        # Se retiran . y , de la cadena extraída
        replaced_text = self.front_content.replace('.','').replace(',','')
        
        # Se separan los caractares por cada salto de línea
        splited_text = replaced_text.split('\n')
        
        # Se eliminan espacios entre las cadenas
        striped_items_text = [re.sub(r'(\d)\s+(\d)', r'\1\2', item).strip()for item in splited_text]
        
        # Se detecta la cadena que contiene un patrón que represente un documento
        document_detected = [ item for item in striped_items_text if re.search(r'\b\d{8,10}\b', item)]

        # Se extrae únicamente los números encontrados en la cadena encontrada previamente
        num_document_from_front = re.search(r'\d{8,10}', document_detected[0]).group()

        return num_document_from_front
        

    def get_date_issue(self):

        splited_text = self.reverse_content.split('\n')
        print(splited_text)

