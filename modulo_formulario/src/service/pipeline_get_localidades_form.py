from modulo_database.src.infrastructure.repository.repositories_manager import LocalidadesRepository
from modulo_database.src.service.database_operations import  ObtenerLocalidadesUseCase

def pipeline_get_localidades_por_id(localidad_value:str):
    
    obtener_informacion_use_case = ObtenerLocalidadesUseCase(repository=LocalidadesRepository())
    queryset_execute = obtener_informacion_use_case.execute({"municipio":localidad_value})

    return queryset_execute

