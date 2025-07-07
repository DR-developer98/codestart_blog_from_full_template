from django.contrib import admin
# ↓↓↓ Deze klasse definieert de textbewerker en verschaft je 
# ↓↓↓ toegang tot de functionaliteiten voor je posts in het adminpaneel 
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    #↓↓↓ Deze regel slaat op de postlijs ↓↓↓
    list_display = ('title', 'slug', 'status', 'created_on')
    #↑↑↑ Deze regel slaat op de postlijs ↑↑↑
    # Onderstaande regel staat snellere zoekopdrachten toe
    search_fields = ['title', 'content']
    # Onderstaande regel beheert de "filter"-zijbalk in de post view pagina
    # We kunnen nu posts filteren op 'status' en op aanmaakdatum (created_on)
    list_filter = ('status', 'created_on',)
    # de tuple met de enkele waarde "title" vergt een afsluitende komma
    #↓↓↓ Deze regels slaan op de Add Post pagina ↓↓↓
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    #↑↑↑ Deze regels slaan op de Add Post pagina ↑↑↑

# Register your models here.
# admin.site.register(Post) 
admin.site.register(Comment)
