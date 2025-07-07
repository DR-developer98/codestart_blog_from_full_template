from django.contrib import admin
# ↓↓↓ Deze klasse definieert de textbewerker en verschaft je 
# ↓↓↓ toegang tot de functionaliteiten voor je posts in het adminpaneel 
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    # de tuple met de enkele waarde "title" vergt een afsluitende komma
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
# admin.site.register(Post) 
admin.site.register(Comment)
