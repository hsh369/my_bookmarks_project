from django.urls import path

from . import views

app_name = 'packs'

urlpatterns = [
    path("<str:username>/", views.PackageListView.as_view(), name="package_list"),
    path("delete/<int:pk>", views.PackageDeleteView.as_view(), name="package_delete"),
    path("update/<int:pk>", views.PackageUpdateView.as_view(), name="package_update"),
    path("create/<str:username>/", views.PackageCreateView.as_view(), name="package_create"),
]
