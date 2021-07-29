from django.urls import path
from stash_index import views
from stash_index.views import genView
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    # class view
    # path('', CLASS.as_view()),
    # function view
    # path('', views., name=''),
    path('', views.home, name='home'),
    path('gview/<str:type>/', genView.as_view()),
    # path('h', CLASS.as_view()),
    # #    path('buyorder', views.buyorder, name='buyorder'),
    # path('formsub', views.formsub, name='formsub'),
    # # path('search', views.search, name='search'),
    # path('about', views.about, name='about'),
    # path('allview', views.allview, name='allview'),
    # path('test', MainClass.as_view()),
    # url(r'', views.main_view, name='mainview'),
    path('view/', views.allview),
    path('view/<str:type>/<str:collection>/', views.main_view)
]
