

from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('alterar-dados/<int:pk>/', views.UpdateUserView.as_view(), name='update_user'),
    path('alterar-senha/<int:pk>/', views.UpdatePasswordView.as_view(), name='update_password'),
    path('registro/', views.RegisterView.as_view(), name='register'),
]