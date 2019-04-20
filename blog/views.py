from django.shortcuts import render, get_object_or_404 ,redirect
from django.utils import timezone
from .models import Post , Comment , Fungo
from .forms import PostForm , CommentForm , FungoForm
from django.contrib.auth.decorators import login_required
import uuid

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def publish(self):
    self.published_date = timezone.now()
    self.save()

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})




@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)





#############################################################################################

def fungo_list(request):
    fungos = Fungo.objects.filter().order_by('genere')
    return render(request, 'blog/fungo_list.html', {'fungos': fungos})



def fungo_remove(request, pk):
    fungo = get_object_or_404(Fungo, pk=pk)
    fungo.delete()
    return redirect('fungo_list')



def fungo_new(request):
    if request.method == "POST":
        form = FungoForm(request.POST)
        if form.is_valid():
            fungo = form.save(commit=False)
            fungo.save()
            return redirect('fungo_list')#, pk=fungo.pk)
    else:
        form = FungoForm()
    return render(request, 'blog/fungo_edit.html', {'form': form})


def fungo_edit(request, pk):
    fungo = get_object_or_404(Fungo, pk=pk)
    if request.method == "POST":
        form = FungoForm(request.POST, instance=fungo)
        if form.is_valid():
            fungo = form.save(commit=False)
            fungo.save()
            return redirect('fungo_list' )#, pk=fungo.pk)
    else:
        form = FungoForm(instance=fungo)
    return render(request, 'blog/fungo_edit.html', {'form': form})


def fungo_detail(request, pk):
    fungo = get_object_or_404(Fungo, pk=pk)
    return render(request, 'blog/fungo_detail.html', {'post': post})