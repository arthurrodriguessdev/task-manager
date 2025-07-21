from django.urls import path
from accounts.views import login_view, cadastro_view

urlpatterns = [
    path('', login_view, name="login_view"),
    path('cadastro/', cadastro_view, name="cadastro_view"),
]