from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from shortit.users.api.views import UserViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"

schema_view = get_schema_view(
   openapi.Info(
      title="Short it API",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # path('', include(router.urls)),
    path("", include("shortit.shortener.api.urls", namespace="shortener_api")),
    path("analytics/", include("shortit.analytics.api.urls", namespace="analytics_api")),
    path("docs/", schema_view)
]

urlpatterns += router.urls
