from django.urls import path
from accounts.views import login_view

urlpatterns = [
    path('', login_view, name="login_view")
]