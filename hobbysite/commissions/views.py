from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobForm, JobApplicationForm

def commissions_list(request):
    commissions = Commission.objects.all().order_by('status', '-created_on')
    
    context = {'commissions': commissions,}
    
    if request.user.is_authenticated:
        profile = request.user.profile
        context['my_commissions'] = profile.commissions.all()
        context['applied_commissions'] = Commission.objects.filter(jobs__applications__applicant=profile).distinct()

    return render(request, 'commissions_list.html', context)

def commissions_detail(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    jobs = commission.commission.all()
    
    total_manpower = sum(job.manpower_required for job in jobs)
    accepted_applications = JobApplication.objects.filter(
        job__in=jobs,
        status='accepted'
    ).count()
    open_manpower = total_manpower - accepted_applications
    
    context = {
        'commission': commission,
        'jobs': jobs,
        'total_manpower': total_manpower,
        'open_manpower': open_manpower,
        'job_form': JobForm(),
        'application_form': JobApplicationForm(),
    }
    
    return render(request, 'commissions_detail.html', context)

def commissions_create(request):
    pass

def commissions_update(request):
    pass

def job_apply(request):
    pass