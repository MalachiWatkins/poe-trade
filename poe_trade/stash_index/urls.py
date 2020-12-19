from django.urls import path
from stash_index import views
from django.conf.urls import include
from django.conf.urls import url
urlpatterns = [
    path('', views.stash_index, name='stash_index'),
    path('test', views.test, name='test'),
    url(r'', views.bootstrap4_index, name="index"),

]
