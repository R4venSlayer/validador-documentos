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
    
        data = pipeline_validate_document_id(num_documento_value, foto_frontal_value, foto_reverso_value)

        return Response(
            {
                "ok": True,
                "data": data
            },
            status=status.HTTP_201_CREATED
        )
    
    




