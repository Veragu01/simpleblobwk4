from django.urls import path
from blog.views import home, categories

urlpatterns = [
    path("", home, name="home"),

    path("categories/", categories, name="categories")
]