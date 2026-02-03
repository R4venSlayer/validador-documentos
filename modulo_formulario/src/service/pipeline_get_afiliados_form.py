from modulo_database.src.infrastructure.repository.repositories_manager import AfiliadosRepository
from modulo_database.src.service.database_operations import  ObtenerInformacionAfiliadoUseCase

def pipeline_get_afiliado_por_id(numero_documento_value:str):
    
    obtener_informacion_use_case = ObtenerInformacionAfiliadoUseCase(repository=AfiliadosRepository())
    queryset_execute = obtener_informacion_use_case.execute({"numero_documento":numero_documento_value})

    return queryset_execute

