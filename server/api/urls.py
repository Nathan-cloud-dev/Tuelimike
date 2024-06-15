from django.urls import path
from . import views

urlpatterns = [
    # user routes
    path('users/', views.User_ListCreate.as_view(), name='users'),
    path('users/<int:pk>/', views.User_RetrieveUpdateDestroy.as_view(), name='user'),


    path('profiles/', views.Profile_ListCreate.as_view(), name='profiles'),
    path('profiles/<int:pk>/', views.Profile_RetrieveUpdateDestroy.as_view(), name='profile'),


    path('course/', views.Course_ListCreate.as_view(), name='courses list create'),
    path('course/<int:pk>', views.Course_RetrieveUpdateDestroy.as_view(), name="Course RUD"),


    path('cart/', views.Cart_ListCreate.as_view(), name= 'Cart'),
    path('cart/<int:pk>/', views.Cart_RetrieveUpdateDestroy.as_view(), name="Cart RUD"),


    path('Feedback/', views.Feedback_ListCreate.as_view(), name= 'feedback'),
    path('Feedback/<int:pk>/', views.Feedback_RetrieveUpdateDestroy.as_view(), name="Feedback RUD"),


    path('UserCourse/', views.UserCourse_ListCreate.as_view(), name= 'UserCourse'),
    path('UserCourse/<int:pk>/', views.UserCourse_RetrieveUpdateDestroy.as_view(), name="UserCourse RUD"),

]