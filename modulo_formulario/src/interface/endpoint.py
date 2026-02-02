from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from rest_framework.request import Request


class UploadFormRecordView(APIView):

    def post(self, request:Request):

        num_documento_value = request.POST.get("num_documento")
        foto_frontal_value = request.FILES.get("foto_frontal")
        foto_reverso_value = request.FILES.get("foto_reverso")
    
     

        return Response(
            {
                "ok": False,
                "msg": "No se pudo extraer la información del documento",
                "data": None
            },
            status=status.HTTP_400_BAD_REQUEST
        )


    
    




