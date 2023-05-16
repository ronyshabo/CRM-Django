from django.contrib import admin
from django.urls import path,include
from leads.views import LandingPageView, SignupView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LandingPageView.as_view(),name='landing_page'),
    path('leads/', include('leads.urls',namespace="leads")),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
    ]

