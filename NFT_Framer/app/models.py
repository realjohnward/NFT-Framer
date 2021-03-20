from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
# Create your models here.

class Template(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    value = models.TextField(max_length=5000)
    styles = models.TextField(max_length=5000, null=True, blank=True)
    variables = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse("template", kwargs={"pk": self.pk})

class Frame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    template = models.ForeignKey(Template, null=True, on_delete=models.SET_NULL)
    variables = models.TextField(max_length=1000, null=True, blank=True)
    file = models.FileField(null=True, blank=True)
