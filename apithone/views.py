from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UploadSerilizer,SerialSerializer
from .models import upload,song
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes,parser_classes
from rest_framework.permissions import IsAuthenticated
from tests.objone import serialobj
from .serializer import UploadSerilizer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from .pagination import MyPagination
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.parsers import JSONParser



@api_view(['GET','POST'])
def uploadview(request):
    queryset = song.objects.all()
    serializer_class = UploadSerilizer(queryset,many=True)
    context = {
        'serializer_class_data':serializer_class
    }
    return Response(serializer_class.data)

@api_view(['GET','POST'])
def serializerview(request):
    obj = serialobj(name='pg@peace.com',email='vishnupg')
    serializer_class = SerialSerializer(obj)
    return Response(serializer_class.data)


class songview(APIView):
    def get(self,request):
        quryset = song.objects.all()
        serializer_class = UploadSerilizer(quryset,many=True)
        return Response(serializer_class.data)

    def post(self,request):
        obj = UploadSerilizer(data=request.data)
        if obj.is_valid(raise_exception=True):
            obj.save()
            return Response(status=status.HTTP_200_OK)
        return Response(obj.errors,status=status.HTTP_400_BAD_REQUEST)


class SongListView(APIView):
    def get(self,request,s_id):
        queryset = song.objects.get(song_id=s_id)
        serializer_class = UploadSerilizer(queryset)
        return Response(serializer_class.data)

    def put(self,request,s_id):
        query_obj = song.objects.get(song_id=s_id)
        obj = UploadSerilizer(query_obj,data=request.data)
        if obj.is_valid(raise_exception=True):
            obj.save()
            print('updated')
            return Response(obj.data,status=status.HTTP_200_OK)
        print('not updated')
        return Response(obj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,s_id):
        obj=song.objects.get(song_id=s_id)
        obj.delete()
        return Response(status=status.HTTP_200_OK)


class ListMixinsView(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = song.objects.all()
    serializer_class = UploadSerilizer


    def get(self,request):
        return self.list(request)

class AllDetailsMixins(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):

    queryset = song.objects.all()
    serializer_class = UploadSerilizer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class SongGenericViews(generics.ListCreateAPIView):
    queryset = song.objects.all()
    serializer_class = UploadSerilizer

class SongGenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = song.objects.all()
    serializer_class = UploadSerilizer


@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication,TokenAuthentication])
class SongViewset(viewsets.ModelViewSet):
    # authentication_classes = SessionAuthentication   # bye using classbased authentication is not work in my case
    # permission_classes = IsAuthenticated         # so am gonna use the decorator here but i should learn this working
    queryset = song.objects.all()
    serializer_class = UploadSerilizer
    pagination_class = MyPagination

    parser_classes(JSONParser)

# the reason i am not using the BaseAuthentication class is that it will use the cache of my username and password
# so even i am logged out it will not redirect the login page .... i think this is my problem i dont know its right or not...

