from django.urls import path
from .views import home_page_view, ElevenListView, ElevenAboutView, ElevenContactView, ElevenDetailView
urlpatterns = [
    path('', home_page_view, name='home'),
    path('shop', ElevenListView.as_view(), name='shop'),
    path('shop/<int:pk>', ElevenDetailView.as_view(), name='detail'),
    path('about', ElevenAboutView.as_view(), name='about'),
    path('contact', ElevenContactView.as_view(), name='contact')
]
