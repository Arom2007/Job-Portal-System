from django.urls import path
from .views import HomeView, job_application, MyJobsView, JobDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('job-application/<int:id>/', job_application, name='job_application'),
    path('my-jobs/', MyJobsView.as_view(), name='my_jobs'),
    path('job-detail/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
]