from django.urls import path, include
from user.views import login_request
 
urlpatterns = [
    path('login/', login_request, name="login"),
      
]
