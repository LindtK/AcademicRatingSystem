from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("capture_marks/", views.captureMarks, name="capture_marks"),
    path("capture_details/", views.captureDetails, name="capture_details")
]