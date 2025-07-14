from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
# We moeten onderstaand importeren, zodat we success messages kunnen tonen
from django.contrib import messages

def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    if request.method == "POST":
        # De formulierdata is de collabrequest tekst
        # Hier creëren we een instantie van de CollaborateForm-klasse
        collaborate_form = CollaborateForm(data=request.POST)
        # Hier checken we of het formulier correct en volledig is ingevuld
        if collaborate_form.is_valid():
            # Indien het formulier correct is ingevuld, dan kan het de database ingestuurd worden
            collaborate_form.save()
            # Wanneer je het formulier indient, dan toon je het volgende bericht
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )
    
    # Dit zorgt ervoor dat het formulier leeg wordt gehaald, nadat je het ingevuld en ingestuurd hebt.
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form": collaborate_form,},
    )
