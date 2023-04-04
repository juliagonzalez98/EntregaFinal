from django.urls import path, include
from user.views import login_request, register
 
urlpatterns = [
    path('login/', login_request, name="login"),
    path('register/', register, name="registro"),
      
]
