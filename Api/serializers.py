from rest_framework import serializers
from .models import Todo_Model
class Todo_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Todo_Model
        fields="__all__"