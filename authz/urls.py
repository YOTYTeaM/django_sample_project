from django.urls import path, include
from .views import Register, main, Login, LogoutUser, UserViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'register', UserViewSet)


app_name = 'authz'
urlpatterns = [
    path('', main, name='main'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', LogoutUser, name='logout'),
    path('', include(router.urls)),
    path('token/', obtain_auth_token)
]