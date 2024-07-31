from django.urls import path, include
from .views import home, UpdateArticle, DeleteArticle, CreateArticle, ArticleViewSet, single_article
from .sitemaps import ArticleSitemap
from rest_framework import routers
from django.contrib.sitemaps.views import sitemap

app_name = 'article'

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
# router.register(r'<int:pk>', single_article, basename='single')

sitemaps = {
    'article': ArticleSitemap,
}


urlpatterns = [
    path('', home,name='home'),
    path('<int:pk>/', UpdateArticle.as_view(), name='show_article'),
    path('create/', CreateArticle.as_view(), name='create_article'),
    path('<int:pk>/delete', DeleteArticle.as_view(), name='delete_article'),
    path('', include(router.urls)),
    path('single/<int:pk>', single_article, name='single'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]