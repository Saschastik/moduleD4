from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view(), name='new_s'),
    path('add', PostCreateView.as_view(), name='add_post'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('search', SearchList.as_view(), name='search'),
]