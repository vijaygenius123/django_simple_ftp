from django.shortcuts import render
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from os import listdir, remove

# Create your views here.

def home(request):
    files = listdir('./files')
    return render(request, 'ftp/home.html', {'files': files})

class DeleteFileView(DestroyAPIView):
    permission_classes = []

    def delete(self, request, *args, **kwargs):
        filename = request.data.get('filename')
        if filename:
            remove('./files/' + filename)
            return Response({'Msg': 'Success'})
        else:
            return Response({'Msg': 'Error'})
