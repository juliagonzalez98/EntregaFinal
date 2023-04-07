from django.urls import path, include
from user.views import login_request, register, agrega_avatar
from django.contrib.auth.views import LogoutView
 
urlpatterns = [
    path('login/', login_request, name="login"),
    path('register/', register, name="registro"),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name="logout"),
    path('agrega-avatar/', agrega_avatar, name="agrega-avatar"),


]
