from django.urls import path
from inicio.views import inicio, vista_datos1


urlpatterns = [
    path('', inicio),
    path('vista-datos1/<nombre>/', vista_datos1),
]