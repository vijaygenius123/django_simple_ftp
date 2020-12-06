from django.shortcuts import render
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from os import listdir

# Create your views here.

def home(request):
    files = listdir('./files')
    return render(request, 'ftp/home.html', {'files': files})

class DeleteFileView(DestroyAPIView):
    permission_classes = []

    def delete(self, request, *args, **kwargs):

        print(request.data)

        return Response({'Msg': 'Success'})