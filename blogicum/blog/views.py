from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from blog.models import Post, Category


def post_object(slug=None):
    posts = Post.objects.select_related(
        'location', 'category', 'author',
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lt=now(),
    )
    if slug is not None:
        posts = posts.filter(category__slug=slug)
    return posts


def index(request):
    template = 'blog/index.html'
    posts = post_object()[:5]
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(post_object(), pk=pk)
    context = {"post": post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category.objects.values(
        'title', 'description', 'id'
    ), slug=category_slug, is_published=True)
    posts = post_object(category_slug)
    context = {'post_list': posts, 'category': category}
    return render(request, template, context)
