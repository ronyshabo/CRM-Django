from django.urls import path
from .views import (secondpage,
    LeadListView, 
    LeadDetailView,
    LeadCreateView,
    LeadUpdateView,
    LeadDeleteView, 
    LandingPageView, 
    AssignAgentView,
    CategoryListView,
    CategoryDetailView,
    LeadCategoryUpdateView
)
# from .view import landing_page,Lead_list,lead_detail, lead_create,lead_update, lead_delete
app_name = "leads"

urlpatterns = [
    path('',LeadListView.as_view(),name='lead-list'),
    # path('2/',secondpage),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete',LeadDeleteView.as_view(),name='lead-delete'),
    path('<int:pk>/assign-agent/',AssignAgentView.as_view(),name='assign-agent'),
    path('create/',LeadCreateView.as_view(),name='lead-create'),
    path('landing-page/', LandingPageView.as_view(), name='landing-page'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/category/',LeadCategoryUpdateView.as_view(),name='lead-category-update'),
]
