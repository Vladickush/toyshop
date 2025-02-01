"""
URL configuration for toyshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from tempfile import template

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
#from task2.views import func_templates, ClassTemplates
#from task3.views import platform, games, cart
from task1.views import platform, games, cart, sign_up_by_html, sign_up_by_django
#from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path("html_forms/", sign_up_by_html),
    path("django_forms", sign_up_by_django),
    #path('func/', func_templates),
    #path('class/', ClassTemplates.as_view()),
    path('platform/', platform),
    path('platform/games/', games),
    path('platform/cart/', cart),

]