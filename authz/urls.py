from django.urls import path, include
from .views import Register, main, Login, LogoutUser

app_name = 'authz'
urlpatterns = [
    path('', main, name='main'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', LogoutUser, name='logout'),
]