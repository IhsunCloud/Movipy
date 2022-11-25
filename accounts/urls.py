from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('sign-in/', views.LoginView.as_view(), name='sign-in'),
    path('sign-out/', views.logout_view, name='sign-out'),
]
 
