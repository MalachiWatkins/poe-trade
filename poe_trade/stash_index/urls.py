from django.urls import path
from stash_index import views
from django.conf.urls import include
from django.conf.urls import url
urlpatterns = [
    # path('', views., name=''),
    path('', views.home, name='home'),
    path('currencyview', views.currencyView, name='currencyView'),
    url(r'', views.bootstrap4_index, name="base"),

]
