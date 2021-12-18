from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register-users'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('home/', views.main_home, name='main-home'),
    path('follow/<str:follow_username>/', views.user_follow, name='user-follow'),
    path('profile/', views.profile, name='profile'),
    path("search/", views.searchposts, name="search"),
    path("upload-post/", views.uploadpost, name="upload-post"),
]
