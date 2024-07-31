from django.contrib.sitemaps import Sitemap
from .models import Article

class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'
    i18n = True
    alternate = True

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return '/article/%s/' % obj.slug