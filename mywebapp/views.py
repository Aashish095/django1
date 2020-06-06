from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse  ##any program return the response
from django.shortcuts import get_object_or_404   ##when object doesnot exist then this show 404
from rest_framework.views import APIView      ##normal views can reutrn an api data
from rest_framework.response import Response   ##get ,put response it will get 200 response
from rest_framework import status      ##send back status
from .models import info
from .serializers import infoserializer
from .forms import RegistrationForm
#get method its return all the info in our model
#post method its help you to create a new info

def home(request):
    return render(request,'home.html',{'name':'navin'})


def add(request):
    return render(request,'result.html')


class infolist(APIView):
    def get(self,request):
        info1=info.objects.all()
        serializer=infoserializer(info1,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = infoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


