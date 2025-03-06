from django.contrib import admin
from django.urls import path, include
from main import views
from django.contrib.auth import views as auth_views

from main.views import (
    KorisnickiProfilListView, KorisnickiProfilDetailView,
    FitnessCiljListView, FitnessCiljDetailView,
    VjezbaListView, VjezbaDetailView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('create-user/', views.create_user, name='create_user'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profili/', KorisnickiProfilListView.as_view(), name='profil-list'),
    path('profil/<int:pk>/', KorisnickiProfilDetailView.as_view(), name='profil-detail'),
    path('fitness-cilj/create/', views.create_fitness_goal, name='create-fitness-goal'),
    path('vjezbe/create/', views.create_exercise, name='create-exercise'),
    path('ukloni-cilj/<int:cilj_id>/', views.ukloni_cilj, name='ukloni-cilj'),
    path('ciljevi/', FitnessCiljListView.as_view(), name='cilj-list'),
    path('cilj/<int:pk>/', FitnessCiljDetailView.as_view(), name='cilj-detail'),
    path('vjezbe/', VjezbaListView.as_view(), name='vjezba-list'),
    path('vjezba/<int:pk>/', VjezbaDetailView.as_view(), name='vjezba-detail'),
]