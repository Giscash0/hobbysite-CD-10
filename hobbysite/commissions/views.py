from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobForm, JobApplicationForm
