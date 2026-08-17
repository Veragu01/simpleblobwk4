from django.shortcuts import render

from blog.models import Category


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories})