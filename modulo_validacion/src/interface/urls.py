from django.contrib import admin
from django.urls import path, include
from modulo_validacion.src.interface.endpoint import UploadFileView, ValidateAffiliate
urlpatterns = [
    path('ocr/verify-id/', UploadFileView.as_view()),
    path('data/affiliate-id/<str:numero_documento_afiliado>', ValidateAffiliate.as_view())

]