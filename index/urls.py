from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('country/<int:id>/', views.country_posts, name='country_posts'),
    path('continent/<int:id>/', views.continent_posts, name='continent_posts'),
]
