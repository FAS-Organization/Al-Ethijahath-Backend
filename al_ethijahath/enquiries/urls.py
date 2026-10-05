from django.urls import path
from .views import enquiry_submit

urlpatterns = [
    path("enquiry-sumbmit/",enquiry_submit ),
]