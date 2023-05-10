from django.urls import path
from .views import (secondpage,LeadListView, LeadDetailView,LeadCreateView,LeadUpdateView,LeadDeleteView)
# from .view import landing_page,Lead_list,lead_detail, lead_create,lead_update, lead_delete
app_name = "leads"

urlpatterns = [
    path('',LeadListView.as_view(),name='lead-list'),
    # path('2/',secondpage),
    path('<int:pk>/',LeadDetailView.as_view(),name='lead-detail'),
    path('<int:pk>/update',LeadUpdateView.as_view(),name='lead-update'),
    path('<int:pk>/delete',LeadDeleteView.as_view(),name='lead-delete'),
    path('create/',LeadCreateView.as_view(),name='lead-create'),
]
