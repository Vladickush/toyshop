from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
#from task2.views import func_templates, ClassTemplates
#from task3.views import platform, games, cart
from task1.views import platform, games, cart, sign_up_by_html, sign_up_by_django, news
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
    path('platform/news/', news),

]
