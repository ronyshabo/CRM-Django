from django.urls import path
from .views import (Lead_list,secondpage,lead_detail,lead_create,lead_update,
lead_delete, LeadListView, LeadDetailView)

app_name = "leads"

urlpatterns = [
    path('',LeadListView.as_view(),name='lead-list'),
    # path('2/',secondpage),
    path('<int:pk>/',LeadDetailView.as_view(),name='lead-detail'),
    path('<int:pk>/update',lead_update,name='lead-update'),
    path('<int:pk>/delete',lead_delete,name='lead-delete'),
    path('create/',lead_create,name='lead-create'),
]
