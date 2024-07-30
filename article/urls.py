from django.urls import path, include
from .views import home, UpdateArticle, DeleteArticle, CreateArticle, ArticleViewSet, single_article
from rest_framework import routers

app_name = 'article'

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
# router.register(r'<int:pk>', single_article, basename='single')


urlpatterns = [
    path('', home,name='home'),
    path('<int:pk>/', UpdateArticle.as_view(), name='show_article'),
    path('create/', CreateArticle.as_view(), name='create_article'),
    path('<int:pk>/delete', DeleteArticle.as_view(), name='delete_article'),
    path('', include(router.urls)),
    path('single/<int:pk>', single_article, name='single'),
]