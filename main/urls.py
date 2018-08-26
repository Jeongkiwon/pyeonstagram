from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin


from . import views


urlpatterns = [
    url(r'^$', views.login_yet, name='login_yet'),
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),

    url(r'^post/', include('post.urls', namespace='post')),
    url(r'^member/', include('member.urls', namespace='member')),
    url(r'^member/user_list/', views.user_list, name="user_list"),
]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)