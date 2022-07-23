from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from .models import Form, Project


class Home(LoginRequiredMixin, View):
    template_name = 'index.html'
    context = dict()

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()[:5]
        self.context["projects"] = projects
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        name = request.POST["name"]
        email = request.POST["email"]
        description = request.POST["description"]

        form = Form.objects.create(full_name=name, email=email, project_description=description)
        form.save()
        return redirect('/')


class About(View):
    template_name = 'about.html'
    context = dict()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
