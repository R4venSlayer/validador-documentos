from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from rest_framework.request import Request

from ..service.pipeline import pipeline_validate_document_id

class UploadFileView(APIView):

    def post(self, request:Request):

        num_documento_value = request.POST.get("num_documento")
        foto_frontal_value = request.FILES.get("foto_frontal")
        foto_reverso_value = request.FILES.get("foto_reverso")
    
        data, validate_state = pipeline_validate_document_id(num_documento_value, foto_frontal_value, foto_reverso_value)


        if None in data.values():
            return Response(
                {
                    "ok": False,
                    "msg": "No se pudo extraer la información del documento",
                    "data": data
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        elif not validate_state:

            return Response(
                {
                    "ok": False,
                    "msg": "El documento ingresado por el usuario no coincide con el extraido",
                    "data": data
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        elif validate_state:
            return Response(
                {
                    "ok": True,
                    "data": data
                },
                status=status.HTTP_200_OK
            )
        




    
    




