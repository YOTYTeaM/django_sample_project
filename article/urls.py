from django.urls import path
from .views import home, UpdateArticle, DeleteArticle, CreateArticle

app_name = 'article'

urlpatterns = [
    path('', home,name='home'),
    path('<int:pk>/', UpdateArticle.as_view(), name='show_article'),
    path('create/', CreateArticle.as_view(), name='create_article'),
    path('<int:pk>/delete', DeleteArticle.as_view(), name='delete_article'),
]