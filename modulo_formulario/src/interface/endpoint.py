from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from rest_framework.request import Request

from ..domain.dtos import InformacionPersonaDTO

from ..service.pipeline_upload_cotizante_form import pipeline

import uuid

from ..service.pipeline_get_departamento_form import pipeline_get_records_departamento
from ..service.pipeline_get_municipios_form import pipeline_get_municipios_por_departamentos
from ..service.pipeline_get_afiliados_form import pipeline_get_afiliado_por_id

class UploadFormRecordView(APIView):

    def post(self, request:Request):

        id_persona_value = str(uuid.uuid4())
        
        # Identificación personal
        primer_nombre_value = request.POST.get("primer_nombre")
        segundo_nombre_value = request.POST.get("segundo_nombre")
        primer_apellido_value = request.POST.get("primer_apellido")
        segundo_apellido_value = request.POST.get("segundo_apellido")
        numero_documento_value = request.POST.get("numero_documento")
        tipo_documento_value = request.POST.get("tipo_documento")

        # Información Sociodemográfica
        estado_civil_value = request.POST.get("estado_civil")
        direccion_residencia_value = request.POST.get("direccion_residencia")
        zona_value = request.POST.get("zona")
        barrio_value = request.POST.get("barrio")
        localidad_value = request.POST.get("localidad")
        departamento_residencia_value = request.POST.get("departamento_residencia")
        municipio_residencia_value = request.POST.get("municipio_residencia")
        estrato_value = request.POST.get("estrato")

        # Información de Contacto
        correo_electronico_value = request.POST.get("correo_electronico")
        numero_celular_value = request.POST.get("numero_celular")
        telefono_fijo_value = request.POST.get("telefono_fijo")

        # Información Laboral
        departamento_laboral_value = request.POST.get("departamento_laboral")
        municipio_laboral_value = request.POST.get("municipio_laboral")
        secretaria_value = request.POST.get("secretaria")
        institucion_educativa_value = request.POST.get("institucion_educativa")

        # Información de Caracterización
        discapacidad_value = request.POST.get("discapacidad")
        tipo_discapacidad_value = request.POST.get("tipo_discapacidad")
        grupo_etnico_value = request.POST.get("grupo_etnico")
        poblacion_lgbtiq_value = request.POST.get("poblacion_lgbtiq")

        informacion_cotizante_dto = InformacionPersonaDTO(
            id_persona=id_persona_value,

            # Identificación personal
            primer_nombre=primer_nombre_value,
            segundo_nombre=segundo_nombre_value,
            primer_apellido=primer_apellido_value,
            segundo_apellido=segundo_apellido_value,
            numero_documento=numero_documento_value,
            tipo_documento=tipo_documento_value,

            # Información Sociodemográfica
            estado_civil=estado_civil_value,
            direccion_residencia=direccion_residencia_value,
            zona=zona_value,
            barrio=barrio_value,
            localidad=localidad_value,
            departamento_residencia=departamento_residencia_value,
            municipio_residencia=municipio_residencia_value,
            estrato=estrato_value,

            # Información de Contacto
            correo_electronico=correo_electronico_value,
            numero_celular=numero_celular_value,
            telefono_fijo=telefono_fijo_value,

            # Información Laboral
            departamento_laboral=departamento_laboral_value,
            municipio_laboral=municipio_laboral_value,
            secretaria=secretaria_value,
            institucion_educativa=institucion_educativa_value,

            # Información de Caracterización
            discapacidad=discapacidad_value,
            tipo_discapacidad=tipo_discapacidad_value,
            grupo_etnico=grupo_etnico_value,
            poblacion_lgbtiq=poblacion_lgbtiq_value
        )

        pipeline(dto_object=informacion_cotizante_dto)

        return Response(
            {
                "ok": True,
                "msg": "Se ha guardado correctamente la información del cotizante en la base de datos",
                "data": id_persona_value
            },
            
            status=status.HTTP_200_OK
        )

class ReturnDepartamentoView(APIView):
    def get(self, request:Request):
        
        data = pipeline_get_records_departamento()

        return Response(
            {
                "ok": True,
                "msg": "Se han consultado exitosamente los departamentos",
                "data": data
            },
            
            status=status.HTTP_200_OK
        )
    

class ReturnMunicipioView(APIView):

    def get(self, request:Request, departamento:str):
        
        data = pipeline_get_municipios_por_departamentos(departamento_value=departamento)

        
        return Response(
            {
                "ok": True,
                "msg": "Se han consultado exitosamente los municipios",
                "data": data
            },
            
            status=status.HTTP_200_OK
        )
    
class ReturnBasicInformationView(APIView):

    def get(self, request:Request, numero_documento:str):

        data = pipeline_get_afiliado_por_id(numero_documento_value=numero_documento)

        return Response(
            {
                "ok": True,
                "msg": "Se han consultado exitosamente los municipios",
                "data": data
            },
            
            status=status.HTTP_200_OK
        )