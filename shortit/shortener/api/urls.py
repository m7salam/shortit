from django.urls import path
from shortit.shortener.api import views

app_name = "shortener_api"

urlpatterns = [
    path('shortit/', views.CreateShortUrl.as_view(), name="shortit"),

]
