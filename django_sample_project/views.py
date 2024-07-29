from django.shortcuts import render
from django.template import loader

def main(request):
    user = request.user
    return render(request, 'home.html', {'user':user})