from django.urls import path
from stash_index import views
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    # path('', views., name=''),
    path('', views.home, name='home'),
    path('buyorder', views.buyorder, name='buyorder'),
    path('formsub', views.formsub, name='formsub'),
    path('search', views.search, name='search'),
    url(r'', views.bootstrap4_index, name="base"),

]
