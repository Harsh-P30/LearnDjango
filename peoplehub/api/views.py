from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer, PersonModelSerializer
from rest_framework.renderers import JSONRenderer
# from django.http import JsonResponse
# from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,DestroyModelMixin
# Create your views here.

# @csrf_exempt
@api_view(['GET','PUT','PATCH'])
def singleobj(request,id):
    data = get_object_or_404(Person,id=id)
    if request.method == "PUT":
        parsed_data = request.data
        serializer = PersonModelSerializer(data,data = parsed_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"update":"successfully"},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


    if request.method == "PATCH":
        parsed_data = request.data
        serializer = PersonModelSerializer(data, data= parsed_data,partial=True) # add partial data = True because here we change only partially 
        if serializer.is_valid():
            serializer.save()
            return Response({"updated":"Successfully"},status= status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        dikha = PersonModelSerializer(data)
        return Response(dikha.data)
    
# @csrf_exempt
# @api_view(['GET','POST'])
def multipleobj(request):
    if request.method == "POST":
        parsed_data = request.data
        serializer = PersonModelSerializer(data = parsed_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"created":"successfull"},status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    data = Person.objects.all()
    dikha = PersonModelSerializer(data, many= True)
    return Response(dikha.data)

 
class MultipleObjView(ListCreateAPIView,RetrieveUpdateDestroyAPIView):

    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer