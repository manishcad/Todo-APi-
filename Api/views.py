from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo_Model
from .serializers import Todo_Serializer
from rest_framework import status
# Create your views here.

class Details(APIView):
    def get(self,request):
        data={
            "View All Todo":"api/all",
            "View Single Todo":"api/todo/<str:pk>",
            "Create A Todo":"api/create",
            "Update Todo":"api/todo/<str:pk>",
            "Delete Todo":"api/todo/<str:pk>",
        }
        return Response(data)
    
class All_Todo(APIView):
    def get(self,request):
        objs=Todo_Model.objects.all()
        serializer=Todo_Serializer(objs,many=True)
        return Response(serializer.data)
    
class Create_Todo(APIView):
    def post(self,request):
        data=request.data
        serializer=Todo_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class Single_Todo(APIView):
    def get(self,request,pk):
        try:
            todo_obj=Todo_Model.objects.get(id=pk)
            serializer=Todo_Serializer(todo_obj)
        except Todo_Model.DoesNotExist:
            return Response({"Error":"Id Does Not Exists"},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
    def put(self,request,pk):
        try:
            todo_obj=Todo_Model.objects.get(id=pk)
        except Todo_Model.DoesNotExist:
            return Response({"Error":"Id Does Not Exists"})
        
        data=request.data
        serializer=Todo_Serializer(todo_obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)
    def delete(self,request,pk):
        try:
            todo_obj=Todo_Model.objects.get(id=pk)
        except Todo_Model.DoesNotExist:
            return Response({"Error":"Id Does Not Exists"})
        todo_obj.delete()
        return Response({"OK":"Item is Deleted"})