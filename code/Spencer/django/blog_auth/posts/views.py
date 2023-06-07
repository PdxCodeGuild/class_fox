from django.shortcuts import render, redirect
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
    if request.method == 'POST':

        # Implement logic to check if the user is logged in. If not, redirect to login page.
        # You can use request.user.is_authenticated to check if the user is logged in. This is a boolean value so a simple if statement will do.

        # If the user is not logged in, redirect to login page.
        if request.user.is_authenticated:
            form = request.POST
            title = form['title']
            content = form['content']

            post = Post.objects.create(
                title=title,
                content=content,
                author=request.user
            )

        # Redirect to post-detail view
            return redirect('post-detail', pk=post.pk)
        else:
            return redirect('login')

    return render(request, 'posts/post_create.html')


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)

    # Implement logic to check if the user is logged in. If not, redirect to login page.
    # You can use request.user.is_authenticated to check if the user is logged in. This is a boolean value so a simple if statement will do.

    # If the user is not logged in, redirect to login page.
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = request.POST
            post.title = form['title']
            post.content = form['content']
            post.save()

            return redirect('post-detail', pk=post.pk)

        else: 
            return redirect('login')
    return render(request, 'posts/post_edit.html', {'post': post})
    


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)

    # Implement logic to check if the user is logged in. If not, redirect to login page.
    # You can use request.user.is_authenticated to check if the user is logged in. This is a boolean value so a simple if statement will do.

    # If the user is not logged in, redirect to login page.
    if request.user.is_authenticated:
        post.delete()
        return redirect('home')
    else:
        return redirect('login')
