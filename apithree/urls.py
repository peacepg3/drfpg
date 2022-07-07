from django.urls import path,include
from .views import *

urlpatterns = [
    path('category/',CategReadView.as_view(),name='category'),
    path('category/<int:pk>/',DetailCategView.as_view(),name='category'),
    path('songs/',SongReadView.as_view(),name='songs'),
    path('songs/<int:pk>/',DetailSongView.as_view(),name='songs')
]

