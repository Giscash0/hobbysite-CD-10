from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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
    jobs = commission.jobs.all()
    
    total_manpower = sum(job.manpower_required for job in jobs)
    accepted_applications = JobApplication.objects.filter(
        job__in=jobs,
        status='accepted'
    ).count()
    open_manpower = total_manpower - accepted_applications
    
    if request.method == 'POST' and 'apply_job' in request.POST:
        job_pk = request.POST.get('job_pk')
        job = get_object_or_404(Job, pk=job_pk)
        if job.status == 'open':
            JobApplication.objects.create(
                job=job,
                applicant=request.user.profile,
                status='pending'
            )
            return redirect('commissions:detail', pk=pk)

    context = {
        'commission': commission,
        'jobs': jobs,
        'total_manpower': total_manpower,
        'open_manpower': open_manpower,
        'job_form': JobForm(),
        'application_form': JobApplicationForm(),
    }
    
    return render(request, 'commissions_detail.html', context)

@login_required
def commissions_create(request):
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid():
            commission = form.save(commit=False)
            commission.author = request.user.profile
            commission.save()
            return redirect(commission.get_absolute_url())
    else:
        form = CommissionForm()
    
    return render(request, 'commissions_create.html', {'form': form})

@login_required
def commissions_update(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    
    if request.user.profile != commission.author:
        return redirect('commissions:list')
    
    if request.method == 'POST':
        form = CommissionForm(request.POST, instance=commission)
        job_form = JobForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            if job_form.is_valid():
                job = job_form.save(commit=False)
                job.commission = commission
                job.save()
            
            if not commission.jobs.filter(status='open').exists():
                commission.status = 'full'
                commission.save()
            
            return redirect(commission.get_absolute_url())
    else:
        form = CommissionForm(instance=commission)
        job_form = JobForm()
    
    context = {
        'form': form,
        'job_form': job_form,
        'commission': commission,
    }
    
    return render(request, 'commissions_update.html', context)

def job_manage(request):
    pass