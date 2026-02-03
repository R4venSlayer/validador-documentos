from modulo_database.src.infrastructure.repository.repositories_manager import MunicipioRepository
from modulo_database.src.service.database_operations import ObtenerDepartamentosUnicosUseCase


def pipeline_get_records_departamento():

    obtener_registros_use_case = ObtenerDepartamentosUnicosUseCase(repository=MunicipioRepository())
    queryset_execute = obtener_registros_use_case.execute(filters_dictionary={})

    return queryset_execute
