from django.db import models
from django.urls import reverse

class Commission(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('full', 'Full'),
        ('completed', 'Completed'),
        ('discontinued', 'Discontinued'),
    )

    title = models.CharField(max_length = 255)
    description = models.TextField(blank = False)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='open')
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('commissions:comment_detail', args=[str(self.pk)])

    class Meta:
        ordering = ['created_on']

class Job(models.Model):
    commission = models.ForeignKey(Commission, on_delete = models.CASCADE)
    role = models.CharField(max_length = 255)
    manpower_required = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['-created_on']