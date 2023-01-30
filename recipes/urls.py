from django.urls import path

from recipes.views import about_me, my_contact, my_home

# URLS SERÃO NO PADRÃO: site.com/final_do_URL
urlpatterns = [
    path('', my_home),  # Home
    path('contact/', my_contact),  # Contact
    path('about/', about_me),  # About
]
