from django.shortcuts import render, reverse, HttpResponseRedirect
from homepage.forms import AddPostForm
from homepage.models import Post
from datetime import datetime



def homepage_view(request):
    posts = Post.objects.all()

    return render(request, 'home_view.html', {'posts': posts})

def upvote_view(request, post_id):
    posts = Post.objects.get(id=post_id)

    posts.up_votes += 1

    posts.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def downvote_view(request, post_id):
    posts = Post.objects.get(id=post_id)

    posts.down_votes += 1

    posts.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add_post_view(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                content = data.get('body'),
                post_type = data.get('post_type'),
                up_votes = 0,
                down_votes = 0,
                post_time = datetime.now(),
            )
            return HttpResponseRedirect(reverse('home'))

    form = AddPostForm()
    return render(request, 'post_form.html', {'form': form})

def boasts_view(request):
    posts = Post.objects.filter(post_type=False)
    
    return render(request, 'home_view.html', {'posts': posts})

def roasts_view(request):
    posts = Post.objects.filter(post_type=True)
    
    return render(request, 'home_view.html', {'posts': posts})

def by_votes_view(request):
    sorted_posts = sorted(Post.objects.all(), key=Post.votescore, reverse=True)

    return render(request, 'home_view.html', {'posts': sorted_posts})






