from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    passwd = models.CharField(max_length=15)
    organization = models.CharField(max_length=50)
    visit_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.visit_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name