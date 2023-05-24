from django.shortcuts import render,redirect

# Create your views here.
from .models import Post


def home(request):

    # Get all posts from database, ordered by creation date, and limit the results to 10
    posts = Post.objects.all().order_by('-created_at')[:10]

    return render(request, 'posts/home.html', {'posts': posts})


def post_detail(request, pk):

    # Get the post with the given primary key (id)
    post = Post.objects.get(pk=pk)

    return render(request, 'posts/post_detail.html', {'post': post})


def post_create(request):
    if request.method == "GET":
        return render(request, 'posts/post_create.html')
    if request.user.is_authenticated:
        request.method == 'POST'
        form = request.POST
        title = form['title']
        content = form['content']
    


        # If the user is not logged in, redirect to login page.

        
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user
         )

        return redirect('post-detail', pk=post.pk)
    else:
        return redirect('login')

    


def post_edit(request, pk):
    # Implement logic to check if the user is logged in. If not, redirect to login page.
    # You can use request.user.is_authenticated to check if the user is logged in. This is a boolean value so a simple if statement will do.

    post = Post.objects.get(pk=pk)

    if request.method == "GET":
    # If the user is not logged in, redirect to login page.
        return render(request, 'posts/post_edit.html', {'post': post})
    if request.user.is_authenticated:
        request.method == 'POST'
        form = request.POST
        post.title = form['title']
        post.content = form['content']
        post.save()

        return redirect('post-detail', pk=post.pk)

    else:
        return redirect('login')



def post_delete(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)

        # Implement logic to check if the user is logged in. If not, redirect to login page.
        # You can use request.user.is_authenticated to check if the user is logged in. This is a boolean value so a simple if statement will do.

        # If the user is not logged in, redirect to login page.

        post.delete()

        return redirect('home')
    else:
        return redirect('login')