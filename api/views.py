from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET','POST'])
def hello_world(request):
    if request.method =='GET':
        return Response({'msg':'Hello World Get Request'})
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'Hello World POST Request', 'data':request.data})


# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({'msg':'Hello World POST Request'})