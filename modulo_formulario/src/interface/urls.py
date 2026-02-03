from django.contrib import admin
from django.urls import path, include
from ..interface.endpoint import UploadFormRecordView, ReturnDepartamentoView

urlpatterns = [
    path('upload-form/', UploadFormRecordView.as_view()),
    path('get-departments/', ReturnDepartamentoView.as_view())
]