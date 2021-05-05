from django.contrib import admin

from .models import post, comment


@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at')
