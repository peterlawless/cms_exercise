from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost
from .forms import BlogForm, Register


# Create your views here.
def index(request):
    if request.method == 'POST':
        description = request.POST['post']
        post = BlogPost(description=description)
        post.save()
    #
    # dict_ = {
    #     "ready": 1,
    #     "doing": 2,
    #     "backlog": 3,
    #     "done": 4
    # }
    posts = BlogPost.objects.all()  # key=lambda x: dict_[x.status])

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)


# def registration(request):
#     if request.method == 'POST':
#         form = Register(request.POST)
#         username = form.get('username', None)
#         first_name = form.get('first name', None)
#         last_name = form.get('last name', None)
#         password = form.get('password', None)
#         email = form.get('email', None)
#     if username and password and email:
