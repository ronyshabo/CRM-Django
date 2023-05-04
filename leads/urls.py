from django.urls import path
from .views import Lead_list,secondpage,lead_detail,lead_create

app_name = "leads"

urlpatterns = [
    path('',Lead_list),
    # path('2/',secondpage),
    path('<int:pk>/',lead_detail),
    path('create/',lead_create),
]
