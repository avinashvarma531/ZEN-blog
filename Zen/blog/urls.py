from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),                                         # url for home page
    path('about/', views.about_view, name='blog-about'),                            # url for about page
    path('contact/', views.contact_view, name='blog-contact'),                      # url for contact page
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),      # url for sepcific article
    path('tag/<str:name>', views.tag_posts, name='tag-posts'),                      # url for tag specific posts
]
