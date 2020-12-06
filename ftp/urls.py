from django.urls import path
from .views import home, DeleteFileView
urlpatterns = [
    path('', home),
    path('delete/', DeleteFileView.as_view())
]


