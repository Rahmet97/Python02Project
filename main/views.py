from django.shortcuts import render

from .models import Form, Project

def home(request):
    projects = Project.objects.all()[:5]

    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        description = request.POST["description"]

        form = Form.objects.create(full_name=name, email=email, project_description=description)
        form.save()

    return render(request, "index.html", {"projects": projects})


def about(request):
    return render(request, "about.html")