from django.urls import path
from stash_index import views
from stash_index.views import MainClass
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    # path('', views., name=''),
    path('', views.home, name='home'),
    # #    path('buyorder', views.buyorder, name='buyorder'),
    # path('formsub', views.formsub, name='formsub'),
    # # path('search', views.search, name='search'),
    # path('about', views.about, name='about'),
    # path('allview', views.allview, name='allview'),
    # # path('search/  ', classview.as_view()),
    url(r'', MainClass.as_view()),

]
