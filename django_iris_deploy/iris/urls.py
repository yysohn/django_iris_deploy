from django.urls import path
from .views import iris_home, predict

urlpatterns = [
    # /
    path('', iris_home , name='iris_home'),
    path('predict/', predict , name='predict'),
 
]