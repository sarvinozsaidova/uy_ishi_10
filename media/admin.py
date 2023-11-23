from django.contrib import admin
from .models import Post, MediaUser
from django.utils.html import format_html
# admin.site.register(Post)
# admin.site.register(MediaUser)

@admin.register(Post)
class PostAdim(admin.ModelAdmin):
    def rename_blog_title(self, obj):
        return obj.text[:150]
    rename_blog_title.short_description = 'text'
    list_display = ['owner', 'rename_blog_title', 'image_tag']


@admin.register(MediaUser)
class MediaUserAdmin(admin.ModelAdmin):


    list_display = ['last_name', 'first_name', 'image_tag', ]
    list_filter = ['first_name', 'last_name']
    ordering = ['last_name']
