from django.urls import path
from .views import commissions_list, commissions_detail, commissions_create, commissions_update, job_manage

urlpatterns = [
    path('list/', commissions_list, name='list'),
    path('detail/<int:pk>/', commissions_detail, name='detail'),
    path('add/', commissions_create, name='create'),
    path('<int:pk>/edit/', commissions_update, name='update'),
    path('jobs/<int:job_pk>/manage/', job_manage, name='manage'),
]

app_name = "commissions"