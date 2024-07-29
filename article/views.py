from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.http.response import HttpResponseNotAllowed, HttpResponseForbidden
from .models import Article
from .forms import ArticleForm
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    articles = Article.objects.order_by('-updated_at')
    user = request.user
    return render(request, 'home.html', {'articles': articles, 'user': user})

class BaseArticle(View):
    title = "Article"
    template = 'form.html'

    def get(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        form = ArticleForm(instance=article)
        is_owner = self.request.user == article.author and self.request.user.is_authenticated
        return render(request, self.template, {'form': form, 'article': article, 'title': self.title, 'is_owner': is_owner})

class UpdateArticle(BaseArticle, LoginRequiredMixin):
    title = "Update Article"

    def post(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        form = ArticleForm(request.POST, instance=article)
        is_owner = self.request.user == article.author and self.request.user.is_authenticated
        if form.is_valid() and is_owner:
            form.author = request.user.id
            form.save()
            return HttpResponseRedirect(reverse_lazy('article:home'))
        else:
            return render(request, self.template, {'form': form, 'article': article, 'title': self.title})

class DeleteArticle(BaseArticle, LoginRequiredMixin):
    title = "Delete Article"

    def post(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        is_owner = self.request.user == article.author and self.request.user.is_authenticated
        if is_owner:
            article.delete()
            return HttpResponseRedirect(reverse_lazy('article:home'))
        else:
            return HttpResponseForbidden()

class CreateArticle(BaseArticle, LoginRequiredMixin):
    title = "Create Article"

    def get(self, request, pk=None):
        form = ArticleForm()
        is_owner = True
        return render(request, self.template, {'form': form, 'article': None, 'title': self.title, 'is_owner': is_owner})

    def post(self, request:HttpRequest, pk=None):
        form = ArticleForm(request.POST)
        if request.user.is_authenticated:
            form.instance.author = request.user
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return HttpResponseRedirect(reverse_lazy('article:home'))
        else:
            return render(request, self.template, {'form': form, 'title': self.title})