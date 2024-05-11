from django.shortcuts import render, redirect
from .models import Category, Post
from django.db.models import Q


def homepage(request) :
    # categories = Category.objects.all()[0:3]
    # featured = Post.objects.filter(featured=True)
    # latest = Post.objects.order_by('-timestamp')[0:3]

    # context= {
    #     'object_list': featured,
    #     'latest': latest,
    #     'categories':categories,
    # }

    # posts = Post.objects.order_by('-timestamp')
    posts = Post.objects.order_by('-created_at')
    context = {
        'posts': posts,
    }

    return render(request, 'postes/index.html', context)


def post(request,slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'postes/post.html', context)


def about(request):
    return render(request, 'postes/about.html')


def category_Post (request, slug):
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(categories__in=[category])
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'postes/category.html', context)


def search(request) :
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    else :
        return redirect('homepage')

    context = {
        'posts': queryset,
        'query': query,
    }
    return render(request, 'postes/search.html', context)


def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)