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
    path('buyorder', views.buyorder, name='buyorder'),
    path('search', views.search, name='search'),
    path('view/', views.allview),
    path('view/<str:type>/<str:collection>/', views.main_view)
]
