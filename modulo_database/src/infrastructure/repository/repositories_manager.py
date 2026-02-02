from .base_repository import BaseRepository

from ..models.modelo import Informacionpersona, Municipio


class InformacionCotizanteRepository(BaseRepository):
    model = Informacionpersona 

class MunicipioRepository(BaseRepository):
    model = Municipio
