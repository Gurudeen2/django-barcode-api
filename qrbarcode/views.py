from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from qrcode import *
import time
from rest_framework import status

# Create your views here.

class Barcode(APIView):
   

    def post(self, request):
        data = request.data
        value=""
        for i in data:
            value = i
            
        img = make(value)
        imgn = "qr"+str(time.time())+".png"
        img.save("media/"+imgn)
        return Response(status=status.HTTP_200_OK)