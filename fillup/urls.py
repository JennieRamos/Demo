from django.conf.urls import url, include
from . import views
from . import models

urlpatterns = [
    url(r'^fillup/', views.fillup),
]
