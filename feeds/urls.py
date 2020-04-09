from django.urls import include, path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreatePost, PostDetails

urlpatterns = {
    path('post', CreatePost.as_view(), name="post_create"),
    url(r'^post/(?P<pk>[0-9]+)/$',
        PostDetails.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
