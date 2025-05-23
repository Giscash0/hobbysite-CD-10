from django.db import models
from django.urls import reverse
from user_management.models import Profile

class Commission(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('full', 'Full'),
        ('completed', 'Completed'),
        ('discontinued', 'Discontinued'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='authored_commissions')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('commissions:detail', args=[str(self.pk)])

    class Meta:
        ordering = ['created_on']

class Job(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('full', 'Full'),
    )

    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='jobs')
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveIntegerField()
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f"{self.role} ({self.manpower_required} needed)"

    class Meta:
        ordering = ['status', '-manpower_required', 'role']

class JobApplication(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='job_applications')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['status', '-applied_on']