from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view for the root path
    path('create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/answer/', views.add_answer, name='add_answer'),
    path('register/', views.register, name='register'),
]
