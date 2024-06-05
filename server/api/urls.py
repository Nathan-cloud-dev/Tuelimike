from django.urls import path
from . import views

urlpatterns = [
    # user routes
    path('users/', views.User_ListCreate.as_view(), name='users'),
    path('users/<int:pk>/', views.User_RetrieveUpdateDestroy.as_view(), name='user'),
    path('profiles/', views.Profile_ListCreate.as_view(), name='profiles'),
    path('profiles/<int:pk>/', views.Profile_RetrieveUpdateDestroy.as_view(), name='profile'),

]