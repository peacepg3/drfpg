
from django.urls import path,include
from rest_framework import routers
from .views import uploadview
from apithone import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('songrout',SongViewset)


urlpatterns = [
    path('api/',views.uploadview,name='objzero'),
    path('objone/',views.serializerview,name='objone'),
    path('objtwo/',songview.as_view(),name='objtwo'),
    path('objthree/<int:s_id>/',SongListView.as_view(),name='objthree'),
    path('mixins/',ListMixinsView.as_view(),name='mix'),
    path('songmix/<int:pk>/',AllDetailsMixins.as_view(),name='songmix'),
    path('generic/',SongGenericViews.as_view(),name='generic'),
    path('detgen/<int:pk>/',SongGenericDetailView.as_view(),name='detgen'),
]+router.urls

