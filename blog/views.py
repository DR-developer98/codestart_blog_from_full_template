from django.shortcuts import render, get_object_or_404
from django.views import generic
# ↓↓↓ het punt voor "models" refereert aan de huidige directory
# ↓↓↓ uit models.py wordt de klasse "Post" geïmporteerd
from .models import Post
# from django.http import HttpResponse

# Create your views here.
# def my_blog(request):
    # return HttpResponse("Hello, blog!")
class PostList(generic.ListView):
    # model = Post
    # queryset = Post.objects.all()
    queryset = Post.objects.filter(status=1)
    # template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6

# Dit is een functiegebaseerde view
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    # Hiermee zetten we de opmerkingen op oplopende volgorde van aanmaakdatum
    comments = post.comments.all().order_by("-created_on")
    # Filter de opmerkingen op approved=True
    comment_count = post.comments.filter(approved=True).count()
    # comments en comment_count worden dan aan de context toegevoegd en zodoende
    # aan de template doorgegeven
    
    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments": comments,
         "comment_count": comment_count,
         "coder": "Damiano"},
    )