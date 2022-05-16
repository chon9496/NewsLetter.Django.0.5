from django.urls import path
from .views import DashboardHomeView,NewslettersDashboardHomeView,NewsletterCreateView

app_name="dashboard"

urlpatterns = [
    path('',DashboardHomeView.as_view(),name="home"),
    path('list/',NewslettersDashboardHomeView.as_view(),name="list"),
    path('create/',NewsletterCreateView.as_view(),name="create"),
    
]