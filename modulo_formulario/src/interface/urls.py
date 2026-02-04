from django.contrib import admin
from django.urls import path, include

from ..interface.endpoint import UploadFormRecordView, ReturnDepartamentoView, ReturnMunicipioView, ReturnBasicInformationView, ReturnLocalidadesView

urlpatterns = [
    path('upload-form/', UploadFormRecordView.as_view()),
    path('get-departments/', ReturnDepartamentoView.as_view()),
    path('get-municipio/<str:departamento>/',ReturnMunicipioView.as_view()),
    path('get-affiliate/<str:numero_documento>/', ReturnBasicInformationView.as_view()),
    path('get-localidad/<str:municipio>/', ReturnLocalidadesView.as_view())
    
]