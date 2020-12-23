from django.urls import path
from stash_index import views
from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    # path('', views., name=''),
    path('', views.home, name='home'),
    path('currencyview', views.currencyView, name='currencyView'),
    path('cardview', views.cardView, name='cardView'),
    path('jewelsview', views.jewelsView, name='jewelsView'),
    path('mapview', views.mapsView, name='mapsView'),
    path('accessoriesview', views.accessoriesView, name='accessoriesView'),
    path('armourview', views.armourView, name='armourView'),
    path('flaskview', views.flaskView, name='flaskView'),
    path('gemsview', views.gemsView, name='gemsView'),
    path('weaponsview', views.weaponsView, name='weaponsView'),
    url(r'', views.bootstrap4_index, name="base"),

]
