from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Trying to pass a dictionnary 
posts = [
    {
        'author' : 'Alexis',
        'title'  : 'Blog Post 1',
        'content' : 'First Post',
        'date_posted' : 'September 11 2020'
    },
    {
        'author' : 'Alexis',
        'title'  : 'Blog Post 2',
        'content' : 'Second Post',
        'date_posted' : 'October 11 2020'
    }
]

def home(request):
    context = {
        'title' : 'home',
        'test' : posts
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html', {'title' : 'about'})