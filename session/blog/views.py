from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm


def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)  # 페이지당 3개의 글이 들어가도록 paginator 객체 생성
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})


def new(request):
    return render(request, 'new.html')


def create(request):
    new_blog = Blog()
    new_blog.title = request.POST.get('title')
    new_blog.content = request.POST.get('content')
    new_blog.image = request.FILES.get('image')
    # get을 쓰는 이유 : image라는 key의 벨류를 가져오는데 없으면 none을 반환함 --> get을 사용한다면 imgae라는 친구에 해당하는게 없어도 에러가 터지지 않는다.
    new_blog.save()
    return redirect('detail', new_blog.id)

# def create(request):
#     form = BlogForm(request.POST)
#     if form.is_valid():
#         new_blog = form.save(commit=False)
#         new_blog.save()
#         return redirect('detail', new_blog.id)
#
#     return render(request, "new.html")


def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'edit_blog': edit_blog})


def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST.get("title")
    old_blog.content = request.POST.get("content")
    old_blog.image = request.FILES.get("image")
    old_blog.save()
    return redirect('detail', old_blog.id)

# def update(request, blog_id):
#     old_blog = get_object_or_404(Blog, pk=blog_id)
#     form = BlogForm(request.POST, instance=old_blog)
#
#     if request.method == "POST":
#
#         if form.is_valid():
#             new_blog = form.save(commit=False)
#             new_blog.save()
#             return redirect("detail", new_blog.id)
#
#     return render(request, "new.html", {"old_blog":old_blog})


def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect("home")
