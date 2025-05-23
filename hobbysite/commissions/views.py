from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobForm, JobApplicationForm

class CommentListView(ListView):
    model = Commission
    template_name = 'comment_list.html'
    context_object_name = 'commissions'

class CommentDetailView(DetailView):
    model = Commission
    template_name = 'comment_entry.html'
    
    def get_context_data(self, **args):
        context = super().get_context_data(**args)
        context['comments'] = Comment.objects.filter(commission=self.object)
        return context