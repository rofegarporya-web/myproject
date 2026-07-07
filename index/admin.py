from django.contrib import admin
from .models import Continent, Country, Post, Image

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Image)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'is_featured', 'created_at')
