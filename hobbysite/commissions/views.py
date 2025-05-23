from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobForm, JobApplicationForm

def commission_list(request):
    commissions = Commission.objects.all().order_by('status', '-created_on')
    
    context = {'commissions': commissions,}
    
    if request.user.is_authenticated:
        profile = request.user.profile
        context['my_commissions'] = profile.commissions.all()
        context['applied_commissions'] = Commission.objects.filter(jobs__applications__applicant=profile).distinct()

    return render(request, 'commissions_list.html', context)

def commission_detail(request):
    pass

def commission_create(request):
    pass

def commission_update(request):
    pass

def job_apply(request):
    pass