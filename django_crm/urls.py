from django.contrib import admin
from django.urls import path,include
from leads.views import LandingPageView, SignupView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls',namespace="leads")),
    path('agents/', include('agents.urls',namespace="agents")),
    path('signup/', SignupView.as_view(), name='signup'),
    path('',LandingPageView.as_view(),name='landing_page'),
    path('reset-password/',PasswordResetView.as_view(),name='reset_password'),
    path('password-reset-done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<udib64>/<token>',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
    ]

