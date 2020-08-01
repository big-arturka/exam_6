"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from webapp.views import index_view, entry_create, entry_update, entry_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('entry/add/', entry_create, name='entry_create'),
    path('entry/<int:pk>/edit/', entry_update, name='entry_update'),
    path('entry/<int:pk>/delete/', entry_delete, name='entry_delete'),
]