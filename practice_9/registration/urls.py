from django.urls import path

from .views import register, stub_page


urlpatterns = [
    path('', register, name='home'),
    path('stub-page', stub_page, name='stub-page'),
]
