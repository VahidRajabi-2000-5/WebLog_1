from django.urls import path

from . import views


urlpatterns = [
    # path('', views.posts_list_view, name='posts_list'),
    path('', views.PostListView.as_view(), name='posts_list'),
    
    path('<int:pk>/', views.post_detail_view, name='post_detail'),
    # path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # path('create/', views.post_create_view, name='post_create'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    
    # path('update/<int:pk>/', views.post_update_view,name ='post_update'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    
    # path('delete/<int:pk>/', views.post_delete_view,name ='post_delete'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(),name ='post_delete'),
    
    
]
