from modulo_database.src.infrastructure.repository.repositories_manager import AfiliadosRepository
from modulo_database.src.service.database_operations import ObtenerInformacionAfiliadoUseCase

def pipeline_validate_affiliate_existance(numero_documento:str):


    obtener_info_use_case = ObtenerInformacionAfiliadoUseCase(repository=AfiliadosRepository())
    queryset_execute = obtener_info_use_case.execute({"numero_documento":numero_documento})

    if len(queryset_execute) > 0:    
        
        return {"num_documento": numero_documento}, True
    
    else:
        return {"num_documento": None}, False