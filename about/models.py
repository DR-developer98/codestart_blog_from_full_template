from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class CollaborateRequest(models.Model):
    # ingevulde naam in het collab formulier
    name = models.CharField(max_length=200)
    # ingevuld e-mailadres in het collab formulier
    email = models.EmailField()
    # ingevulde tekst in het formulier
    message = models.TextField()
    # checkbox voor "read" (als gelezen weergeven). Staat uiteraard bij default op "False", daar het verzoek nog verwerkt moet worden
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"