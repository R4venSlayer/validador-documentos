from .base_repository import BaseRepository
from ..models.modelo import Informacionpersona, Municipio

class InformacionCotizanteRepository(BaseRepository):
    model = Informacionpersona 

class MunicipioRepository(BaseRepository):
    model = Municipio
    
    def filter_distinct_departamentos(self, **filters):
        return (
            self.model.objects
            .filter(**filters)
            .values("descripcion_dep")
            .distinct()
        )