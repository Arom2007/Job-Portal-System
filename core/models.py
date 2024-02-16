from django.db import models
from commons.models import BaseModel
from django.contrib.auth.models import User

class Category(BaseModel):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"



class Job(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    application_deadline = models.DateField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class JobApplication(BaseModel):
    status_choices = [
        ("APPLIED", "Applied"),
        ("SCREENING", "Screening"),
        ("SHORT_LISTED", "Short_Listed"),
        ("REJECTED", "Rejected"),
        ("SELECTED", "Selected"),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_application")
    interview_data = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=status_choices, max_length=20)

    def __str__(self):
        return f"Job application from {self.user.email}"
