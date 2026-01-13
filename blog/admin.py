from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'publish']
    list_filter = ['author', 'status', 'publish']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']