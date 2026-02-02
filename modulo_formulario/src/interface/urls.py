from django.contrib import admin
from django.urls import path, include
from modulo_validacion.src.interface.endpoint import UploadFileView
urlpatterns = [
    path('upload-form/', UploadFileView.as_view()),
]