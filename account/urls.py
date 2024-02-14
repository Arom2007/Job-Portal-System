from django.urls import path
from .views import user_logout, UserLoginView, UserRegisterView, UserProfile, UserProfileUpdate

urlpatterns= [
    path('logout/', user_logout, name='user_logout'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('my-profile/<int:pk>/', UserProfile.as_view(), name='user_profile'),
    path('update-profile/<int:pk>/', UserProfileUpdate.as_view(), name='user_profile_update'),
]