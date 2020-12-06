from django.urls import path
from shortit.analytics.api import views

app_name = "analytics_api"

urlpatterns = [
    path('count/', views.CountHits.as_view(), name="count"),

]
