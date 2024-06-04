from django.urls import path
from . import views

urlpatterns = [
    path('accounts/<int:user_id>/', views.profile),
]