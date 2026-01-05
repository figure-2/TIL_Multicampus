from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts' : posts,
    }
    return render(request,'index.html',context)

def detail(request,id):
    post = Post.objects.get(id=id)

    context = {
        'post':post
    }
    return render(request,'detail.html', context)

def new(request):
    return render(request,'new.html')

def create(request):
    title = request.POST.get('title')  # post에 데이터가 들어있어서 GET 아님
    content = request.POST.get('content')

    # post = Post()
    # post.title = title
    # post.content = content
    # post.save()

    post = Post(title=title, content = content)
    post.save()
    return redirect('posts:detail', id=post.id)

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('posts:index') # 지웠으니 메인 페이지로 이동

def edit(request,id):
    post = Post.objects.get(id=id)

    context = {
        'post' : post
    }
    return render(request,'edit.html',context)

def update(request,id):
    # new data
    title = request.POST.get('title')
    content = request.POST.get('content')

    # old data
    post = Post.objects.get(id=id)
    post.title = title
    post.content = content
    post.save()

    return redirect('posts:detail', id=post.id)