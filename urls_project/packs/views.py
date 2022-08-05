from struct import pack
from django.shortcuts import get_object_or_404
from django.views import generic

from links.models import Link
from .models import Package
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib import messages
from . import forms
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


class PackageListView(LoginRequiredMixin, SelectRelatedMixin, generic.ListView):
    model = Package
    select_related = ('user', 'package')
    template_name: str = 'package_list.html'

    def get_queryset(self):
        try:
            self.package_user = User.objects.prefetch_related("packages").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.package_user.packages.all()

class PackageCreateView(generic.CreateView):
    model = Package
    fields = ('name', 'description')
    template_name: str = 'packs/package_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class PackageUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Package
    template_name: str = 'packs/package_update.html'
    redirect_field_name = '/'
    form_class = forms.PackageForm

class PackageDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Package
    template_name: str = 'packs/package_delete.html'
    messages = ()
    success_url = reverse_lazy("home")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
