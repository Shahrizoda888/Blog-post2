from django.urls import path
from .views import (
    home,
    login,
    add_post,
    delete_post,
    update_post,
    logout,
    detail_post,
    all_post
    )

urlpatterns = [
    path('',home.as_view(),name='home'),
    
    path('login/',login,name='login'),
    path('add-post/',add_post,name='add_post'),
    path('delete-post/<int:pk>/',delete_post,name='delete_post'),
    path('update-post/<int:pk>/',update_post,name='update_post'),
    path('detail-post/<int:pk>/',detail_post,name='detail_post'),
    path('all-post/',all_post,name='all_post'),
    path('logout/',logout,name='logout'),

]

