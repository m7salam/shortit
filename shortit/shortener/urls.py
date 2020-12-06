
from django.urls import path
from django.conf.urls import url
from shortit.shortener.views import short_url_redirect_view

app_name = "shortener"

urlpatterns = [
    # url(r"^(?P<shortcode>[\w-]+){6,15}/$", short_url_redirect_view)
    # path("", views.BlogListCreateAPIView.as_view(), name="blog_list"),
    # path("<int:pk>/<str:slug>/", views.BlogDetailAPIView.as_view(), name="blog_detail"),
    # path("comments/", views.CommentsListCreateAPIView.as_view(), name="comments_list"),
    # path("team/", views.TeamListCreateAPIView.as_view(), name="team"),
    # path("technology/", views.TechnologyListCreateAPIView.as_view(), name="technology"),
    # path("project-type/", views.ProjectTypeListAPIView.as_view(), name="project_type_list_api"),
    # path("value-project/", views.ValueProjectListCreateAPIView.as_view(), name="value_project"),


]
