from django.conf.urls import url

from . import views
from post.views import *

app_name="post"
urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url(r'^add/$',PostCreateView.as_view(), name="add", ),

    url(r'^my_post/$',views.my_post_list, name="my_post",),

    # Example: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$',PostUpdateView.as_view(), name="update", ),
    # Example: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$',PostDeleteView.as_view(), name="delete",),

    url(r'^(?P<post_pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_pk>\d+)/like-toggle/$', views.post_like_toggle, name='post_like_toggle'),

    # Comment
    url(r'^(?P<post_pk>\d+)/comment/create/$', views.comment_create, name='comment_create'),

    url(r'^member/(?P<user_pk>\d+)/$', views.user_detail, name='user_detail'),
    
]
