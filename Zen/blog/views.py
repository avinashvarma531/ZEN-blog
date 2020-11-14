from django.shortcuts import render, redirect
from .models import Post, Tag
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.contrib import messages


# helper fns
def get_page(req):
    paginator = Paginator(posts, 6)
    page_num = req.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return page_obj
# end helper fns

# Home page
def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    tags = Tag.objects.all().order_by('name')
    popular = Post.objects.all().order_by('-claps')[:3]
    page_obj = get_page(request)
    
    context = {
        'posts': page_obj,
        'tags': tags,
        'popular_posts': popular
    }
    return render(request, 'blog/post_list.html', context)

# specific article page
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

# About page
def about_view(request):
    return render(request, 'blog/about.html')

# Contact page
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email-id")
        message = request.POST.get("message")
        print(f'\n{name}\n{email}\n{message}\n')
        
        messages.success(request, 'Thank you for your message! You will be replied quickly :)')
        return redirect('blog-contact')
    
    return render(request, 'blog/contact.html')

# filter by tag name
def tag_posts(request, **kwargs):
    tag_name = kwargs['name']
    posts = Tag.objects.get(name=tag_name).post_set.all().order_by('-date_posted')
    all_tags = Tag.objects.all().order_by('name')
    popular_posts = Post.objects.all().order_by('-claps')[:3]
    page_obj = get_page(request)

    context = {
        'posts': page_obj,
        'tags': all_tags,
        'popular_posts': popular_posts
    }
    return render(request, 'blog/post_list.html', context)
