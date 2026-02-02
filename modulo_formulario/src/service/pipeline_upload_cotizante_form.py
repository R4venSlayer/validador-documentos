from ..domain.dtos import InformacionPersonaDTO

from modulo_database.src.infrastructure.repository.repositories_manager import InformacionCotizanteRepository

from modulo_database.src.service.database_operations import CrearRegistroUseCase

def pipeline(dto_object:InformacionPersonaDTO):

    crear_registro_formulario_use_case = CrearRegistroUseCase(repository=InformacionCotizanteRepository())
    crear_registro_formulario_use_case.execute(data=dto_object.__dict__)


