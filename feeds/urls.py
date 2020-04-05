from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreatePost

urlpatterns = {
    path('post', CreatePost.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
