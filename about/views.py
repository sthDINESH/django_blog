from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import About

# Create your views here.


def about_me(request):
    # return HttpResponse("This will include About me")
    about = About.objects.order_by("-updated_on").first()

    return render(
        request=request,
        template_name="about/about.html",
        context={"about": about},
    )


