from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('item/<int:pk>', views.edit, name="edit_todo"),
    path('delete/<int:pk>', views.delete, name="delete_todo"),
]