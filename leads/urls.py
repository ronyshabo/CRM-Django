from django.urls import path
from .views import Lead_list,secondpage,lead_detail

app_name = "leads"

urlpatterns = [
    path('',Lead_list),
    # path('2/',secondpage),
    path('<pk>/',lead_detail),
]
