from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<int:post_id>/', views.delete, name="delete"),
    path('addLike/<int:post_id>/', views.addLike, name="add like"),
    path('edit/<int:post_id>/', views.edit, name="edit")
]
