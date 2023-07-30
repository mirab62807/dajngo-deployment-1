from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

posts = [
        {
        'author': 'CoreMS',
        'title': 'Blog Post 1',
        'content': 'Fist post content',
        'date_posted': 'July 27, 2023' } ,
        {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Fist post content',
        'date_posted': 'July 28, 2023' }

]
def home(request):
    context = { 'posts' : posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' :'About'})
