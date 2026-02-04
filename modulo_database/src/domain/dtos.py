from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass
class InformacionPersonaDTO:
    id_persona: UUID

    # Información Sociodemográfica
    estado_civil: Optional[str] = None
    direccion_residencia: Optional[str] = None
    zona: Optional[str] = None
    barrio: Optional[str] = None
    localidad: Optional[str] = None
    departamento_residencia: Optional[str] = None
    municipio_residencia: Optional[str] = None
    estrato: Optional[int] = None

    # Información de Contacto
    correo_electronico: Optional[str] = None
    numero_celular: Optional[str] = None
    telefono_fijo: Optional[str] = None

    # Información Laboral
    departamento_laboral: Optional[str] = None
    municipio_laboral: Optional[str] = None
    secretaria: Optional[str] = None
    institucion_educativa: Optional[str] = None

    # Información de Caracterización
    discapacidad: Optional[str] = None
    tipo_discapacidad: Optional[str] = None
    grupo_etnico: Optional[str] = None
    poblacion_lgbtiq: Optional[str] = None


@dataclass(frozen=True)
class LocalidadDTO:
    municipio: Optional[str]
    codigo_barrio: Optional[str]
    barrio: Optional[str]
    localidad: Optional[str]
    codigo_localidad: Optional[int]
