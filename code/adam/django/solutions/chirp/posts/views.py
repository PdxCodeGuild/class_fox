from django.shortcuts import render,redirect
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/home.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})



def create_post(request):
    if request.method == 'GET':
        return render(request, 'posts/post_create.html')
    if request.user.is_authenticated:
        request.method == 'POST'
        form = request.POST
        content = form['content']

        post = Post.objects.create(
            content=content,
            author=request.user
        )
        return redirect('post-detail', pk=post.pk)
    else:
        return redirect('login')
    
def edit_post(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == "GET":
        return render(request, 'posts/edit_post.html', {'post': post})
    if request.user.is_authenticated:
        request.method == "POST"
        form = request.POST
        post.content = form['content']
        post.save()

        return redirect('post-detail', pk=post.pk)
    
    else:
        return redirect('login')
    

def delete_post(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)

        post.delete()
        return redirect('home')
    else:
        return redirect('login')
