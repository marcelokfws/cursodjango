# from django.contrib.auth import views as auth_views

from django.contrib.auth import views as auth_views
from django.urls import path

from authors import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_create, name='register_create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),  # noqa
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(),  # noqa
         name='password_reset_complete'),


    path(
        'dashboard/recipe/new/',
        views.DashboardRecipe.as_view(),
        name='dashboard_recipe_new'
    ),

    path(
        'dashboard/recipe/delete/',
        views.DashboardRecipeDelete.as_view(),
        name='dashboard_recipe_delete'
    ),
    path(
        'dashboard/recipe/<int:id>/edit/',
        views.DashboardRecipe.as_view(),
        name='dashboard_recipe_edit'
    ),
    path(
        'profile/<int:id>/',
        views.ProfileView.as_view(),
        name='profile'
    ),

]
