
from django.urls import path, include
from .views import *

urlpatterns = [
    path('create-section', create_section, name="createseccion"),
    path('<int:pk_s>/create-topic', create_to_topic, name="createtopic")
]