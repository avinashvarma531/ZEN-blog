from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about_view, name='blog-about'),
    path('contact/', views.contact_view, name='blog-contact'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('tag/<str:name>', views.tag_posts, name='tag-posts'),
]