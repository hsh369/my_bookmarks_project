from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import models
from . import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpView(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name: str = 'accounts/signup.html'

class UserDetailsView(generic.DetailView):
    model = models.User
    template_name: str = 'accounts/user_details.html'   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context
    

