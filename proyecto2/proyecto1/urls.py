"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from proyecto1.views import saludar, despedir
#from proyecto1.views import despedir
from proyecto1.views import ver_fecha

urlpatterns = [
    path('admin/', admin.site.urls),
#    path("saludo/", saludar),     # Forma de enlazar la url con la funcion creada en el view
#    path("despedir/", despedir),
    path("fecha/", ver_fecha),
]


