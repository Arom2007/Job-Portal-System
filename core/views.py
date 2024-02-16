from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Category, Job, JobApplication
from django.shortcuts import redirect
from django.contrib import messages
class HomeView(ListView):
    template_name = 'core/home.html'
    queryset = Job.objects.exclude(
        job_applications__status__in=["APPLIED", "SCREENING", "SHORT_LISTED", "REJECTED", "SELECTED"]
    )
    context_object_name = 'jobs'


def job_application(request, id):
    if request.method == "POST":
        resume = request.user.userprofile.resume
        try:
            resume = request.user.userprofile.resume
        except:
            messages.error(request, "Please complete your profile")
            return redirect('home')
        if not resume:
            messages.error(request, "Please upload your resume to apply for a job.")
            return redirect('home')
        JobApplication.objects.create(user=request.user, job_id=id, status="APPLIED")
        messages.success(request, "Successfully applied for the job.")
    return redirect('home')
