from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Answer
from .forms import PostForm, AnswerForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Display posts in descending order by date
    return render(request, 'home.html', {'posts': posts})

# Create a post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# View post details with answers
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    answers = post.answers.all()
    answer_form = AnswerForm()
    return render(request, 'post_detail.html', {'post': post, 'answers': answers, 'answer_form': answer_form})

# Add an answer to a post
@login_required
def add_answer(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.post = post
            answer.save()
            return redirect('post_detail', post_id=post.id)

# User registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
        messages.error(request, 'Registration failed. Please check the details and try again.')
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

