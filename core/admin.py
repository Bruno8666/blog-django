from django.contrib import admin
from .models import Post, Tag, Category, LandingPage
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'slug')
    list_editable = ('slug', )
    search_fields = ('title', )


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_editable = ('category', )


class LandingPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'finished_project', 'ongoing_project', 'text_alt_project', 'text_alt_project_in_progress')
    list_editable = ('finished_project', 'ongoing_project', 'text_alt_project', 'text_alt_project_in_progress')


admin.site.register(Category)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(LandingPage, LandingPageAdmin)