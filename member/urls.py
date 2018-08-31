from django.conf.urls import url
from member import views
from member.views import *
from . import views
app_name="member"
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^user_list/', views.user_list, name="user_list"),
]
