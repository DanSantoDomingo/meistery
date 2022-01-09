

from django.urls import path, include

from core import views
from core.api import v1_api

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('api/', include(v1_api.urls)),
]