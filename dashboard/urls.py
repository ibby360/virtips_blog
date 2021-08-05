from django.urls import path
from dashboard import views

urlpatterns = [
    path('me/', views.dashboard, name='dashboard')
]
