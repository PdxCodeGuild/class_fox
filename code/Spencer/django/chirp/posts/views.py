from django.shortcuts import render, redirect
from .models import posts


def home(request):
    post = posts.objects.all()
    return render(request, 'posts/home.html',)



def post_create(request):
    if request.method == 'POST':

        if request.user.is_authenticated:
            form = request.POST
            title = form['title']
            content = form['content']

            post = posts.objects.create(
                title=title,
                content=content,
                author=request.user
            )

            return redirect('post-detail', pk=post.pk)
        else:
            return redirect('login')

    return render(request, 'posts/post_create.html')


def post_delete(request, pk):
    post = posts.objects.get(pk=pk)

    if request.user.is_authenticated:
        post.delete()
        return redirect('home')
    else:
        return redirect('login')