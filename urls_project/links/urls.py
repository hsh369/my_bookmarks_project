from tkinter import N
from django.urls import path
from . import views


app_name = 'links'

urlpatterns = [
    path('<username>/<slug>', views.LinksListView.as_view(),name='list'),
    path('create/', views.LinkCreateView.as_view(),name='create'),
    path('update/<username>/<slug>', views.LinkUpdateView.as_view(),name='update'),
    path('delete/<username>/<slug>', views.LinkDeleteView.as_view(),name='delete'),
]
