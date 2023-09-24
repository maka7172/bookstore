from django.urls import path
from django.views.generic.base import TemplateView


urlpatterns =[ 
    path('home/',HomePageViwe.as_view(),name='home')
]
