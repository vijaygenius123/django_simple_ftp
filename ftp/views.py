from django.shortcuts import render
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from os import listdir, remove
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    files = listdir('./files')
    return render(request, 'ftp/home.html', {'files': files})


class DeleteFileView(DestroyAPIView):
    permission_classes = []

    def delete(self, request, *args, **kwargs):
        filename = request.data.get('filename')
        if filename:
            try:
                remove('./files/' + filename)
                return Response({'Msg': 'Success'})
            except OSError:
                return Response({'Msg': 'Error'}, HTTP_404_NOT_FOUND)
        else:
            return Response({'Msg': 'Error'}, HTTP_404_NOT_FOUND)
