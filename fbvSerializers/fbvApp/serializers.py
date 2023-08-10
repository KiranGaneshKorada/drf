from rest_framework import serializers
from . import models

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields='__all__'