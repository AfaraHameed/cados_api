from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Advocates
from . serializers import AdvocateSerializer,CompanySerializer
from django.db.models import Q
from rest_framework.views import APIView
from . models import Company
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# GET /advocates
# POST/advocates

# GET/advocates/:id
# PUT/advocates/:id
# DELETE/advocates/:id

@api_view(['GET','POST'])
def endpoints(request):
    data=['/advocates','advocates/:username']
    return Response(data)

@api_view(['GET','POST'])
def  advocates_list(request):
    if request.method == 'GET':
        query=request.GET.get('query')
        if query==None:
            query=''
        
        advocates = Advocates.objects.filter(Q(username__icontains=query)|Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
         advocates = Advocates.objects.create(username=request.data['username'],bio=request.data['bio'])
         serializer = AdvocateSerializer(advocates)
         return Response(serializer.data)
    
@api_view(['POST'])
def add_advocates(request):
    Advocates.objects.create(username=request.data('username'))

    return Response({'added'})

# @api_view(['GET','PUT','DELETE'])
# def advocates_details(request,username):
   
#     advocate = Advocates.objects.get(username=username)
#     if request.method == 'GET':
#         serializer=AdvocateSerializer(advocate,many=False)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#        advocate.username = request.data['username']
#        advocate.bio = request.data['bio']
#        advocate.save()

#        serializer=AdvocateSerializer(advocate,many=False)
#        return Response(serializer.data)
    
#     if request.method == 'DELETE':
#         advocate.delete()
#         return redirect('advocates')
    


class AdvocateDetail(APIView):
    def get_object(self,username):
        try:
            return Advocates.objects.get(username=username)
        except Advocates.DoesNotExist:
            raise JsonResponse('Advocate does not exist')
        
    def get(self,request,username):
        advocate=self.get_object(username)
        serializer=AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)
    
    def put(self,request,username):
        advocate=self.get_object(username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()

        serializer=AdvocateSerializer(advocate,many=False)
        return Response(serializer.data) 
    
    def delete(self,request,username):
        advocate=self.get_object(username)
        advocate.delete()
        return Response('user deleted')
    
@api_view(['GET'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)



