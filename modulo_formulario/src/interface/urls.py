from django.contrib import admin
from django.urls import path, include
from ..interface.endpoint import UploadFormRecordView

urlpatterns = [
    path('upload-form/', UploadFormRecordView.as_view())
]