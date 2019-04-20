from django.urls import path
from . import views
import uuid

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

    
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    path('', views.fungo_list, name='fungo_list'),
    path('fungo/new/', views.fungo_new, name='fungo_new'),
    path('fungo/<int:pk>/edit/', views.fungo_edit, name='fungo_edit'),
    path('fungo/<int:pk>/remove/', views.fungo_remove, name='fungo_remove'),

    path('csv_file/new/', views.csv_file_new, name='csv_file_new'),
    path('csv_file/<int:pk>/edit/', views.csv_file_edit, name='csv_file_edit'),
]