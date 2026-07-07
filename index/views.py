from django.shortcuts import render, get_object_or_404
from .models import Post, Continent, Country

def home(request):
    featured_post = Post.objects.filter(is_featured=True).first()
    posts = Post.objects.all()
    continents = Continent.objects.all()
    countries = Country.objects.all()
    context = {
        'featured_post': featured_post,
        'posts': posts,
        'continents': continents,
        'countries': countries,
    }
    return render(request, 'index/home.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    images = post.images.all()
    context = {
        'post': post,
        'images': images,
    }
    return render(request, 'index/post_detail.html', context)

def continent_posts(request, continent_id):
    continent = get_object_or_404(Continent, id=continent_id)
    posts = Post.objects.filter(
        country__continent=continent
    )
    context = {
        'continent': continent,
        'posts': posts,
    }
    return render(request, 'index/continent_posts.html', context)

def country_posts(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    posts = Post.objects.filter(
        country=country
    )
    context = {
        'country': country,
        'posts': posts,
    }
    return render(request, 'index/country_posts.html', context)
