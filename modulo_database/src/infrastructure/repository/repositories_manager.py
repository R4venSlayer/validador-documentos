from .base_repository import BaseRepository
from ..models.modelo import Informacionpersona, Municipio, Afiliados, Localidades

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
    
class AfiliadosRepository(BaseRepository):
    model = Afiliados


    def get_afiliado_by_id(self, **filters):
        return(
            self.model.objects
            .filter(**filters)
            .values("primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido", "tipo_documento", "numero_documento", "tipo_cotizante")
        )

class LocalidadesRepository(BaseRepository):
    model = Localidades

    def get_localidad_by_municipio(self, **filters):
        return(
            self.model.objects
            .filter(**filters)
            .values("municipio","localidad","barrio")
        )
