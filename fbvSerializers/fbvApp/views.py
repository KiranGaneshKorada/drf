from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def student_list(request):

    if request.method=='GET':
        students=models.Student.objects.all()
        serialized_data=serializers.StudentSerializers(students,many=True)
        return Response(serialized_data.data)
    
    elif request.method=='POST':
        serialized_data=serializers.StudentSerializers(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def student_details(request,pk):
    try:
        student=models.Student.objects.get(pk=pk)
    except models.Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serilized_data=serializers.StudentSerializers(student)
        return Response(serilized_data.data)
    
    elif request.method=='PUT':
        serilized_data=serializers.StudentSerializers(student,data=request.data)
        if serilized_data.is_valid():
            serilized_data.save()
            return Response(serilized_data.data)
        return Response(serilized_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)