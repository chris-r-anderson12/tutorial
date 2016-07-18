from django.conf.urls import url

from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='blog_index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
