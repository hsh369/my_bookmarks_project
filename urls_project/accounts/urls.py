from django.urls import re_path, path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('details/<pk>/',views.UserDetailsView.as_view(),name='user_details'),
    path('',include('packs.urls')),
]