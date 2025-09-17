from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.


def about_me(request):
    """
    Renders the most recent information on the website author
    and allows user collaboration
    Displays an individual instance of :model:`about.About`
    **Context**
    ``about``
        The most recent instance of :model:`about.About`
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`
    :template:`about/about.html`
    """
    # return HttpResponse("This will include About me")
    about = About.objects.order_by("-updated_on").first()

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaboration = collaborate_form.save(commit=False)
            collaboration.read = False
            collaboration.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )

    collaborate_form = CollaborateForm()

    return render(
        request=request,
        template_name="about/about.html",
        context={
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )
