from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    # Ieder blogartikel zou een aparte titel moeten hebben (vandaar dat "unique") om de gebruikers niet in verwarring te brengen
    title = models.CharField(max_length=200, unique=True)
    # In de uitgeverijwereld is een slug een artikel dat nog opgesteld wordt (nog niet af)
    slug = models.SlugField(max_length=200, unique=True)
    # De naam van de gebruiker is een one-to-many Foreign Key, daar een gebruiker meerdere posts kan schrijven
    # on_delete=models.CASCADE houdt in, dat wanneer een gebruiker een post verwijdert, al zijn posts verwijderd worden
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
        )
    # Dit is de eigenlijke inhoud van de post
    content = models.TextField()
    # Dit zet de aanmaaktijd van de post op het daadwerkelijke tijdstip waarop de post is gepubliceerd
    created_on = models.DateTimeField(auto_now_add=True)
    # Iedere post heeft een STATUS, die d.m.v. een integer wordt uitgedrukt
    # Bij default staat de STATUS op 0 (draft/concept); wanneer deze gepubliceerd wordt, wordt de STATUS op 1 gezet
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    # auto_now_add => updatet alleen bij aanmaak (dus letterlijk als je op "post" drukt)
    # auto_now => updatet het veld iedere keer (bij iedere wijziging)
    update_on = models.DateTimeField(auto_now = True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    # Het post-veld verwijst naar de Post, vandaar dat de ForeignKey "Post" is
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comment"
    )
    # De auteur verwijst natuurlijk naar de gebruiker en heeft als ForeignKey de User
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.author}"
