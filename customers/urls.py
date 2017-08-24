from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^libraries/$', views.LibraryList.as_view()),
    url(r'^authors/', views.AuthorList.as_view()),
    url(r'^author/(?P<pk>[0-9]+)/$', views.AuthorDetail.as_view()),

    url(r'^login/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]