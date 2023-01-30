from django.urls import path

from recipes.views import my_home

# URLS SERÃO NO PADRÃO: site.com/final_do_URL
urlpatterns = [
    path('', my_home),  # Home
]
