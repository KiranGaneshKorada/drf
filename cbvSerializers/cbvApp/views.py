from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics,mixins,viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

class StudentPagination(PageNumberPagination):
    page_size=1

# CLASS BASED VIEWS (approach 4 using viewsets)
class StudentViewSet(viewsets.ModelViewSet):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializers

    pagination_class=StudentPagination
    #pagination_class=PageNumberPagination this uses settings pagination (global)

    #filter_backends=[DjangoFilterBackend]
    #filterset_fields=['name','score'] #for filtering data

    #filter_backends=[filters.SearchFilter]
    #search_fields=['^id','^name']  #for searching

    """
    '^' starts-with-search
    '=' exact match
    '@' full text search
    '$' regex search
    """

    filter_backends=[filters.OrderingFilter]
    ordering_fields=['score']






""" CLASS BASED VIEWS (approach 3 using generics)
class StudentsList(generics.ListCreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializers

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializers
"""


""" CLASS BASED VIEWS (approach 2 using mixins)
class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializers

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    

class StudentDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializers

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
"""




""" CLASS BASED VIEWS (approach 1 general)

class StudentsList(APIView):

    def get(self,request):
        students=models.Student.objects.all()
        serialized_data=serializers.StudentSerializers(students,many=True)
        return Response(serialized_data.data)
    
    def post(self,request):
        serialized_data=serializers.StudentSerializers(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)
    

class StudentDetail(APIView):

    def get_object(self,pk):
        try:
            return models.Student.objects.get(pk=pk)
        except models.Student.DoesNotExist:
            raise Http404
        

    def get(self,request,pk):
        student=self.get_object(pk)
        serilized_data=serializers.StudentSerializers(student)
        return Response(serilized_data.data)
    
    def put(self,request,pk):
        student=self.get_object(pk)
        serilized_data=serializers.StudentSerializers(student,data=request.data)
        if serilized_data.is_valid():
            serilized_data.save()
            return Response(serilized_data.data)
        return Response(serilized_data.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pk):
        student=self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""