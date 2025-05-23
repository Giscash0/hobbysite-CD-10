from django import forms
from .models import Commission, Job, JobApplication

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']
        widgets = {
            'status': forms.Select(choices=Commission.STATUS_CHOICES),
        }

class JobForm(forms.ModelForm):
    pass

class JobApplicationForm(forms.ModelForm):
    pass