from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'datetime_creation',
        'datetime_modified',
        'status',
    ] 
    ordering = ('-datetime_modified','-status')