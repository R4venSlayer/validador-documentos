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
            .distinct().order_by("descripcion_dep")
        )
    
    def filter_municipios_by_departamento(self, **filters):
        return (
            self.model.objects
            .filter(**filters)
            .values("descripcion_mun")
            .order_by("descripcion_mun")
        )