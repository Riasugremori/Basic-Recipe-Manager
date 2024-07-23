from django.urls import path
from .views import main_view, Add_view, Edit_view, Delete_view

urlpatterns = [
    path('main/', main_view, name='main'),
    path('add/', Add_view, name='add'),
    path('edit/<str:title>/', Edit_view, name='edit'),  
    path('delete/<str:title>/', Delete_view, name='delete'),  
]
