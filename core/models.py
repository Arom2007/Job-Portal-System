from django.db import models
from commons.models import BaseModel

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