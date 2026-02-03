from modulo_database.src.infrastructure.repository.repositories_manager import MunicipioRepository
from modulo_database.src.service.database_operations import ObtenerMunicipioPorDepartamentoUseCase


def pipeline_get_municipios_por_departamentos(departamento_value:str):

    obtener_registros_service = ObtenerMunicipioPorDepartamentoUseCase(repository=MunicipioRepository())
    queryset = obtener_registros_service.execute({"descripcion_dep":departamento_value})

    return queryset