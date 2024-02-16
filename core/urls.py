from django.urls import path
from .views import HomeView, job_application

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('job-application/<int:id>/', job_application, name='job_application')
]