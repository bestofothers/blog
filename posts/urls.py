from django.conf.urls import include, url
from django.contrib import admin

from .views import IndexView, CategoryView, PostView

urlpatterns = [

    url(r'^categories/$', CategoryView.as_view(), name='all_categories'),
    url(r'^post/(?P<pk>[a-zA-Z0-9-]+)/$', PostView.as_view(), name='post'),
    url(r'^$', IndexView.as_view(), name='index'),
]