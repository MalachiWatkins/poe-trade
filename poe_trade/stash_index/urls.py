from django.urls import path
from stash_index import views
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
    # path('test', MainClass.as_view()),
    # url(r'', views.main_view, name='mainview'),
    path('view/', views.allview),
    path('view/<str:collection>/<str:type>/', views.main_view)
]
