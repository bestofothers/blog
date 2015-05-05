from django.conf.urls import include, url
from django.contrib import admin

from .views import IndexView, CategoriesView, PostView, CategoryView

urlpatterns = [

    url(r'^categories/$', CategoriesView.as_view(), name='all_categories'),
    url(r'^post/(?P<slug>[a-zA-Z0-9-]+)/$', PostView.as_view(), name='post'),
    url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/$', CategoryView.as_view(), name='category'),
    url(r'^$', IndexView.as_view(), name='index'),
]