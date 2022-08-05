from django.views import generic
from .models import Link
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.urls import reverse_lazy
from django.http import Http404
from  django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from . import forms
# Create your views here.

class LinksListView(LoginRequiredMixin,generic.ListView):
    model = Link
    template_name: str = 'links/links_list.html'
    context_object_name = 'listoflinks' 
    def get_queryset(self):
        queryset = Link.objects.select_related('package').filter(package__slug__iexact=self.kwargs.get('slug'))
        return queryset
    
class LinkCreateView(LoginRequiredMixin,generic.CreateView):
    model = Link
    fields = ('name', 'url','description')
    template_name: str = 'links/link_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.package = self.request.get
        self.object.save()
        return super().form_valid(form)

class LinkUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Link
    template_name: str = 'links/link_update.html'
    redirect_field_name = '/'
    form_class = forms.LinkForm   

class LinkDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Link
    template_name: str = 'links/link_delete.html'
    messages = ()
    success_url = reverse_lazy("home")

    def get_queryset(self):
        queryset = Link.objects.select_related('package').filter(package__slug__iexact=self.kwargs.get('slug'))
        return queryset

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Link Deleted")
        return super().delete(*args, **kwargs)
     

