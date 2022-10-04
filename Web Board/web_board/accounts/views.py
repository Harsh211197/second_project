from audioop import reverse
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View 
from django.contrib.auth.models import User
from .forms import Registrationform
from django.views.generic import CreateView

class Userregister(View):
    def render(self, request):
        return render(request, 'enroll/userregister.html', {'form': self.form})

    def post(self, request):
        self.form = Registrationform(request.POST)
        if self.form.is_valid():
            self.form.save()
            return HttpResponse("Hello")
        return self.render(request)

    def get(self, request):
        self.form = Registrationform()
        return self.render(request)

1234# class Userregister(CreateView):
#     model = User
#     form_class = Registrationform
#     template_name = 'enroll/userregister.html'
#     context_object_name = 'register_form'









