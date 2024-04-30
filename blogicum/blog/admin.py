from django.contrib import admin

from blog.models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'pub_date', 'location',
                    'category', 'is_published', 'created_at')
    list_editable = ('category', 'is_published', 'location',)
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug',
                    'is_published', 'created_at')
    list_editable = ('description', 'is_published',)


class BlogLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)


admin.site.register(Category, BlogCategoryAdmin)
admin.site.register(Location, BlogLocationAdmin)
admin.site.register(Post, BlogPostAdmin)
