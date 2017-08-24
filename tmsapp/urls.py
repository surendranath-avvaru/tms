from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^books/$', views.BookList.as_view()),
]