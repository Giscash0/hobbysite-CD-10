from django.urls import path
from .views import commissions_list, commissions_detail, commissions_create, commissions_update, job_manage

urlpatterns = [
    path('list/', CommentListView.as_view(), name = 'comment_list'), 
    path('detail/<int:pk>/', CommentDetailView.as_view(), name = 'comment_detail'),
]

app_name = "commissions"