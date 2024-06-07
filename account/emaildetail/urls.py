# urls.py
from django.urls import path
from .views import CustomLoginView, acc

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('accounts/profile/',acc),
]
